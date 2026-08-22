<div align="center">

# 📦 Instagram Saved Library

### *Delete Instagram without losing a single saved post.*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Privacy: 100% Offline](https://img.shields.io/badge/Privacy-100%25%20Offline-purple.svg)](#%EF%B8%8F-privacy)
[![Platform: Windows · Mac · Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-orange.svg)](#)

**Browse, search, and watch your saved Instagram reels, posts & collections — completely offline, no login required.**

</div>

---

![App Screenshot](public/screenshots/1.png)

---


## Why does this exist?

You want to delete Instagram. But you have saved thousands of posts — recipes, workouts, tutorials, ideas.

When you download your data from Instagram, you get raw HTML files with plain text links. No thumbnails. No players. Basically useless.

**This app fixes that.** Drop your exported files in one folder, double-click to launch, and your entire saved library opens as a clean visual gallery — playable reels, searchable captions, organized collections, everything.

---

## How to use it

### Step 1 — Download your saved posts from Instagram

> ⏱️ Takes about 2 minutes to request. Instagram sends the file in 15–30 minutes.

1. Go to **Instagram.com** on your computer
2. Click **More** → **Settings** → **Accounts Center**
3. Go to **Your information and permissions** → **Download your information**
4. Click **Download or transfer information** → select your account → **Some of your information**
5. Scroll to **Saved items** and check:
   - ✅ Saved posts
   - ✅ Saved collections
   - ✅ Saved music
6. Set format to **HTML** *(not JSON)*, date range to **All time**, then click **Create files**
7. Instagram emails you a download link. Download and unzip the file.

---

### Step 2 — Set up the app

1. Open the unzipped folder and go to: `your_instagram_activity / saved`
2. Clone this repository **directly into that `saved` folder**:
   ```
   git clone https://github.com/sthakur369/instagram-saved-library
   ```
   Or download as a ZIP and extract it there.

Your folder structure should look like this:
```
saved/
├── saved_posts.html
├── saved_collections.html
├── saved_music.html
└── instagram_saved_library/   ← this repo goes here
    ├── run.bat
    └── app.py
```

---

### Step 3 — Launch

- **Windows:** Double-click `run.bat` — that is it.
- **Mac / Linux:** Open a terminal in the folder and run:
  ```bash
  python app.py
  ```

The app opens in your browser at `http://127.0.0.1:8765` automatically.

> **No Python installed?** Open `public/index.html` directly in your browser and drag-drop your export files.

---

## What you get

- 🎬 Watch reels and videos directly inside the app
- 📁 Browse your saved collections as organized folders
- 🔍 Search by caption, @creator, or #hashtag instantly
- 🖼️ Quick View lightbox with keyboard navigation (`←` `→` `Esc`)
- 🎵 Saved music with Spotify & YouTube search links
- ⚡ Handles 10,000+ posts without slowing down
- 🔒 100% offline — your data never leaves your computer

---

## 🛡️ Privacy

Everything runs locally on your machine. The app never asks for your Instagram password, never uploads your data, and never connects to any server except Instagram's own public embed CDN to display post previews.

---

## Tech

Python standard library only — **no pip installs required.** Single-file vanilla JS frontend.

---

<div align="center">
  <sub>Built for people who want to leave Instagram but keep their saved knowledge. ❤️</sub>
</div>
