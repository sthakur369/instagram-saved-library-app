"""Local, dependency-free viewer for Instagram saved-item HTML exports."""

from __future__ import annotations

import html
import json
import os
import re
import socket
import threading
import webbrowser
from collections import OrderedDict
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

APP_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = APP_DIR / "public"
CACHE_FILE = APP_DIR / "cache" / "library.json"
CONFIG_FILE = APP_DIR / "config.env"
CONFIG_EXAMPLE_FILE = APP_DIR / "config.env.example"
POST_URL = re.compile(
    r'URL\s*<div>\s*<a[^>]+href="(https?://(?:www\.)?instagram\.com/(?:p|reel|tv)/[^"?#]+)',
    re.IGNORECASE,
)
COLLECTION_START = re.compile(
    r'Name</td>\s*<td[^>]*>(?P<name>[^<]+)</td>\s*</tr>\s*<tr>\s*<td[^>]*>Type</td>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")
SHORTCODE_RE = re.compile(r"/(?:p|reel|tv)/([^/?#]+)", re.IGNORECASE)


def read_config() -> dict[str, str]:
    values: dict[str, str] = {}
    if not CONFIG_FILE.exists() and CONFIG_EXAMPLE_FILE.exists():
        CONFIG_FILE.write_text(CONFIG_EXAMPLE_FILE.read_text(encoding="utf-8"), encoding="utf-8")
        if os.name == "nt":
            try:
                os.startfile(str(CONFIG_FILE))
            except OSError:
                pass
    if not CONFIG_FILE.exists():
        return values
    for line in CONFIG_FILE.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def clean(value: str) -> str:
    return SPACE_RE.sub(" ", html.unescape(TAG_RE.sub(" ", value))).strip()


def find_export_files(source: Path | None = None) -> tuple[dict[str, Path], Path]:
    names = ("saved_posts.html", "saved_collections.html", "saved_music.html")
    
    # Candidate search paths in priority order
    candidates: list[Path] = []
    if source and source.exists():
        candidates.append(source)
    
    # Auto-detect relative to APP_DIR and parent directories
    candidates.extend([
        APP_DIR.parent, # If placed inside saved folder (recommended)
        APP_DIR, # If files are inside the app folder
        APP_DIR.parent / "your_instagram_activity" / "saved", # If in root of export
        APP_DIR.parent / "saved",
        APP_DIR / "your_instagram_activity" / "saved",
        APP_DIR / "saved",
        Path.cwd(),
        Path.cwd().parent,
        Path.cwd() / "your_instagram_activity" / "saved",
    ])
    
    for candidate in candidates:
        if not candidate.exists():
            continue
        files: dict[str, Path] = {}
        for name in names:
            direct = candidate / name
            if direct.is_file():
                files[name] = direct
                continue
            matches = list(candidate.glob(f"**/{name}"))
            if matches:
                files[name] = matches[0]
        if "saved_posts.html" in files or "saved_collections.html" in files:
            return files, candidate
            
    return {}, source if source else APP_DIR


def unique_urls(raw: str) -> list[str]:
    seen: OrderedDict[str, None] = OrderedDict()
    for match in POST_URL.finditer(raw):
        seen.setdefault(html.unescape(match.group(1)).strip(), None)
    return list(seen)


def extract_posts_from_raw(raw: str) -> list[dict[str, str]]:
    starts = list(POST_URL.finditer(raw))
    posts: list[dict[str, str]] = []
    for index, match in enumerate(starts):
        block = raw[match.start() : starts[index + 1].start() if index + 1 < len(starts) else len(raw)]
        caption_match = re.search(r'Caption</td>\s*<td[^>]*>(.*?)</td>', block, re.I | re.S)
        username_match = re.search(r'Username</td>\s*<td[^>]*>(.*?)</td>', block, re.I | re.S)
        owner_match = re.search(r'Name</td>\s*<td[^>]*>(.*?)</td>', block, re.I | re.S)
        date_match = re.search(r'class="_3-94 _a6-o">(.*?)</div>', block, re.I | re.S)
        
        # Hashtags block
        hashtags: list[str] = []
        ht_match = re.search(r'Hashtags</h2>(.*?)Owner</h2>', block, re.I | re.S)
        if ht_match:
            hashtags = [clean(t) for t in re.findall(r'<div class="_a6-p">([^<]+)</div>', ht_match.group(1))]

        url = html.unescape(match.group(1)).strip()
        sc_match = SHORTCODE_RE.search(url)
        shortcode = sc_match.group(1) if sc_match else ""
        
        kind = "Reel" if "/reel/" in url else "Video" if "/tv/" in url else "Post"
        posts.append(
            {
                "url": url,
                "shortcode": shortcode,
                "kind": kind,
                "caption": clean(caption_match.group(1)) if caption_match else "",
                "username": clean(username_match.group(1)).lstrip("@") if username_match else "",
                "owner": clean(owner_match.group(1)) if owner_match else "",
                "savedAt": clean(date_match.group(1)) if date_match else "",
                "hashtags": " ".join(hashtags),
            }
        )
    return posts


def extract_collections(raw: str) -> list[dict[str, object]]:
    starts = list(COLLECTION_START.finditer(raw))
    collections: list[dict[str, object]] = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(raw)
        segment = raw[match.start() : end]
        urls = unique_urls(segment)
        collections.append({
            "name": clean(match.group("name")),
            "urls": urls,
            "count": len(urls),
            "covers": urls[:4]
        })
    return collections


def extract_music(raw: str) -> list[dict[str, str]]:
    rows = re.findall(r'<td[^>]*>(Title|Artist)</td>\s*<td[^>]*>(.*?)</td>', raw, re.I | re.S)
    tracks: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for label, value in rows:
        key = label.lower()
        value = clean(value)
        if key == "title" and current.get("title"):
            tracks.append(current)
            current = {}
        current[key] = value
    if current.get("title"):
        tracks.append(current)
    seen: OrderedDict[tuple[str, str], dict[str, str]] = OrderedDict()
    for track in tracks:
        seen.setdefault((track.get("title", ""), track.get("artist", "")), track)
    return list(seen.values())


def fingerprint(files: dict[str, Path]) -> list[dict[str, object]]:
    return [{"parser": 3}] + [
        {"name": name, "path": str(path), "size": path.stat().st_size, "mtime": path.stat().st_mtime_ns}
        for name, path in sorted(files.items())
    ]


def build_library(force: bool = False) -> dict[str, object]:
    config = read_config()
    source_value = config.get("INSTAGRAM_SAVED_FOLDER", "").strip()
    source_path = Path(os.path.expandvars(source_value)).expanduser() if source_value else None
    files, source = find_export_files(source_path)
    if not files:
        return {
            "ready": False,
            "message": "No Instagram saved HTML files were found (saved_posts.html / saved_collections.html). Check INSTAGRAM_SAVED_FOLDER in config.env.",
            "source": str(source),
        }
    signature = fingerprint(files)
    if not force and CACHE_FILE.exists():
        try:
            cached = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            if cached.get("signature") == signature:
                return cached["library"]
        except (OSError, json.JSONDecodeError):
            pass

    posts_raw = files.get("saved_posts.html", Path()).read_text(encoding="utf-8", errors="replace") if "saved_posts.html" in files else ""
    collection_raw = files.get("saved_collections.html", Path()).read_text(encoding="utf-8", errors="replace") if "saved_collections.html" in files else ""
    music_raw = files.get("saved_music.html", Path()).read_text(encoding="utf-8", errors="replace") if "saved_music.html" in files else ""

    # Parse posts from saved_posts.html
    posts = extract_posts_from_raw(posts_raw) if posts_raw else []
    seen_urls = {p["url"].rstrip("/") for p in posts}

    # If any post exists in saved_collections.html that was not in saved_posts.html, add it
    if collection_raw:
        coll_posts = extract_posts_from_raw(collection_raw)
        for cp in coll_posts:
            if cp["url"].rstrip("/") not in seen_urls:
                posts.append(cp)
                seen_urls.add(cp["url"].rstrip("/"))

    collections = extract_collections(collection_raw) if collection_raw else []
    music = extract_music(music_raw) if music_raw else []

    library: dict[str, object] = {
        "ready": True,
        "source": str(source),
        "updatedAt": datetime.now(timezone.utc).isoformat(),
        "stats": {"posts": len(posts), "collections": len(collections), "music": len(music)},
        "posts": posts,
        "collections": collections,
        "music": music,
    }
    CACHE_FILE.parent.mkdir(exist_ok=True)
    CACHE_FILE.write_text(json.dumps({"signature": signature, "library": library}, ensure_ascii=False), encoding="utf-8")
    return library


class AppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC_DIR), **kwargs)

    def do_GET(self):
        if urlparse(self.path).path == "/api/library":
            try:
                payload = build_library(force="refresh=1" in self.path)
                body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except Exception as error:
                body = json.dumps({"ready": False, "message": f"Could not read the export: {error}"}).encode("utf-8")
                self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            return
        return super().do_GET()

    def log_message(self, format, *args):
        return


def find_available_port(start_port: int) -> int:
    for p in range(start_port, start_port + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    return start_port


def main() -> None:
    config = read_config()
    requested_port = int(config.get("PORT", "8765"))
    port = find_available_port(requested_port)
    server = ThreadingHTTPServer(("127.0.0.1", port), AppHandler)
    url = f"http://127.0.0.1:{port}"
    print("=" * 60)
    print(f"  Instagram Saved Library is running at: {url}")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 60)
    if os.getenv("NO_BROWSER") != "1":
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
