<div align="center">

# 📦 Instagram Saved Library & Vault
### *Break free from Instagram without losing your saved knowledge, reels, and memories.*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Privacy: 100% Local](https://img.shields.io/badge/Privacy-100%25%20Offline%20%26%20Local-purple.svg)](#-privacy--security-guarantee)
[![Platform: Windows | Mac | Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-orange.svg)](#-quick-start-in-3-steps)

<p align="center">
  <b>A lightweight, blazing-fast, private offline viewer and player for your exported Instagram saved posts, collections, and audio.</b>
</p>

</div>

---

## 💡 Why This Project Exists

Thinking about deleting or deactivating your Instagram account, but hesitating because of **hundreds or thousands of saved posts** (recipes, workout routines, tech tutorials, travel guides, book recommendations, and reels)?

When you request your data from Instagram, Meta gives you raw HTML files with plain text links and no visual thumbnails or playable players.

**Instagram Saved Library** transforms your official Instagram export into a modern, visual, interactive personal vault. Browse, search, watch reels with audio, and explore your curated collections—**all 100% offline on your own computer without an active Instagram session.**

---

## ✨ Features

- 🎬 **In-App Reels & Video Playback** — Watch your saved reels and videos with audio directly inside the application.
- 📁 **Collections & Folders** — Automatically organizes your custom Instagram saved collections with item counters.
- 🎵 **Saved Music Vault** — Browse your saved tracks with 1-click links to search on Spotify & YouTube.
- 🔍 **Instant Search & Hashtag Filtering** — Search across captions, `@creator` handles, and `#hashtags` in real time.
- 🖼️ **Quick View Lightbox Modal** — High-resolution media viewer with full formatted captions and keyboard navigation (`←`, `→`, `Esc`).
- 🌙 **Dark & Light Mode** — Seamless theme toggle matching your system preference.
- ⚡ **Ultra-Lightweight & Scalable** — Intelligent memory virtualization keeps frame count low, ensuring smooth 60fps scrolling across 10,000+ posts.
- 🔒 **100% Private & Local** — Zero tracking, zero telemetry, zero cloud uploads. Your data never leaves your computer.

---

## 🚀 Quick Start in 3 Easy Steps

### Step 1: Export your Saved Posts from Instagram (Takes 2 minutes)

> **Tip:** Exporting *only* your saved posts takes **15–30 minutes** for Instagram to generate (compared to several days for a full account export).

1. Open **[Instagram.com](https://www.instagram.com)** on your desktop browser.
2. Click **More** (bottom left corner) ➔ **Settings** ➔ **Accounts Center**.
3. In Accounts Center, click **Your information and permissions** ➔ **Download your information**.
4. Click **Download or transfer information** and select your account.
5. Select **Some of your information** (custom download).
6. Scroll down to the **Saved items** section and check:
   - ✅ **Saved posts**
   - ✅ **Saved collections**
   - ✅ **Saved music**
7. On the format page, configure:
   - **Destination**: *Download to device*
   - **Date range**: *All time*
   - **Format**: **HTML** *(Important: Choose HTML, not JSON)*
   - **Media quality**: *Medium* or *High*
8. Click **Create files**. Instagram will email you a download link when ready.

---

### Step 2: Download & Extract into the `saved` Folder

1. Download the `.zip` file from Instagram's email notification.
2. Unzip the folder to your computer.
3. Open the unzipped folder and navigate to:
   ```
   your_instagram_activity / saved
   ```
   *(You will see `saved_posts.html`, `saved_collections.html`, and `saved_music.html` here)*
4. Clone or extract this **`instagram_saved_library`** folder directly inside that **`saved`** folder!

---

### Step 3: Run the App (Zero Configuration Needed!)

- **Windows:** Double-click **`run.bat`**.
- **Mac / Linux:** Run in terminal:
  ```bash
  python app.py
  ```
- **No Python? No problem!** Double-click **`public/index.html`** in any browser to use direct drag-and-drop browser mode!

The app automatically detects your saved posts in the parent folder and opens in your browser at `http://127.0.0.1:8765`!

---

## ⚙️ Automatic Detection & Configuration

The app automatically searches for your export files in all standard locations:
- Current folder: `./`
- Parent folder: `../` (when placed inside `your_instagram_activity/saved/`)
- Subfolder: `your_instagram_activity/saved/`

If you keep your files in a custom directory, simply specify the path in `config.env`:

```env
# config.env (Optional - works automatically if left blank)
INSTAGRAM_SAVED_FOLDER=
PORT=8765
```

---

## 🛡️ Privacy & Security Guarantee

| Aspect | Guarantee |
| :--- | :--- |
| **Server** | Localhost only (`127.0.0.1`). Not accessible over the network. |
| **Data Storage** | All HTML parsing happens locally on your machine in Python or in your browser. |
| **Media Previews** | Streamed directly from Instagram's official public embed CDN. |
| **Credentials** | Never asks for or requires your Instagram password, cookies, or login. |
| **Open Source** | 100% inspectable code with zero external tracking scripts. |

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| `/` | Focus search bar immediately |
| `Esc` | Close Quick View Lightbox |
| `←` | Previous post in Lightbox |
| `→` | Next post in Lightbox |

---

## 🛠️ Tech Stack & Architecture

- **Backend**: Python 3 standard library (`http.server`, `re`, `json`, `pathlib`) — **0 external pip dependencies required!**
- **Frontend**: Lightweight vanilla HTML5, CSS3 Custom Properties (Variables), and Modern JS (ES6+).
- **Optimization**: `IntersectionObserver` iframe pool manager restricting active memory frames to ensure buttery-smooth scrolling.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

<div align="center">
  <sub>Built with ❤️ for digital wellness and preserving knowledge.</sub>
</div>