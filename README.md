<div align="center">

# 📦 Instagram Saved Library

### Delete Instagram without losing your saved posts and Reels.

**Turn your Instagram data export into a private, searchable visual library.**

[![Website](https://img.shields.io/badge/Website-Visit%20Site-8a6f5a.svg)](https://sthakur369.github.io/instagram-saved-library-site/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Privacy: Local & Offline](https://img.shields.io/badge/Privacy-Local%20%26%20Offline-purple.svg)](#privacy)
[![Platform: Windows · Mac · Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-orange.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Your Instagram Saved folder is not a good archive. This turns it into one.**

</div>

---

![Instagram Saved Library — searchable saved posts, Reels, collections and music](public/screenshots/1.png)

## Why this exists

Maybe you want to **delete Instagram**.

But you have years of saved posts and Reels: recipes, workouts, tutorials, travel ideas, design inspiration, products, references, and things you planned to come back to.

So you request your **Instagram data export**.

Then you open it and find **HTML files, text and links**.

Where is the visual gallery?  
Where are your collections?  
How do you search thousands of saves?

**Instagram Saved Library is the missing step between the Instagram export and a usable archive.**

It reads your exported saved data and turns it into a visual library you can browse, search and revisit on your computer.

> **Export from Instagram → Open with this app → Browse your saved library.**

---

## What you get

- 🎬 **Saved Reels & videos** — open saved Reels and video posts from your library
- 🖼️ **Visual saved-post gallery** — see your saved content instead of browsing raw HTML
- ⚡ **Large libraries** — designed to handle 10,000+ saved posts
- 🔒 **Local & private** — your exported data stays on your computer

---

## You don't need to be technical

If you can download a ZIP file, open a folder and double-click a file, you can use this app.

You don't need to know:

- Python
- coding
- Git
- databases
- command-line tools

The technical setup is optional for the people who want the easiest repeat use.

## Who is this for?

### “I want to delete Instagram, but I don't want to lose my saved posts.”

That's the main use case.

### “I downloaded my Instagram data, but the export is just HTML.”

That's exactly the problem this app solves.

### “I have thousands of Instagram saves and can't find anything.”

Search your captions, creators and hashtags instead of endlessly scrolling.

### “I want my Instagram saves outside Instagram.”

Keep a local library you can browse without logging into Instagram.

---

## How to use it

You only need to do this once to get your Instagram export ready.

### 1. Get your Instagram data

Request your Instagram information and include your **Saved items**.

On Instagram:

1. Open **Settings → Accounts Center**.
2. Go to **Your information and permissions → Download your information**.
3. Choose your Instagram account.
4. Choose **Some of your information**.
5. Select:
   - **Saved posts**
   - **Saved collections**
   - **Saved music**
6. Choose **HTML** format and **All time**.
7. Request the download and download the ZIP when Instagram is ready.

Then unzip the downloaded file.

### 2. Find your `saved` folder

Inside the extracted Instagram data, find the folder named:

```text
saved/
├── saved_posts.html
├── saved_collections.html
└── saved_music.html
```

You don't need to open or understand these HTML files.

### 3. Download this app

On this GitHub page, click:

**Code → Download ZIP**

Unzip the downloaded app.

You do **not** need a GitHub account to download it.

### 4. Put the app beside your Instagram export

Move the extracted app folder into Instagram's `saved` folder:

```text
saved/
├── saved_posts.html
├── saved_collections.html
├── saved_music.html
└── instagram-saved-library/
      ├── app.py
      ├── run.bat
      ├── config.env.example
      └── public/
          └── ...
```

That's the main setup.

---

## Two ways to open your library

### ⭐ Recommended: install Python once

If you're going to use your library regularly, this is the easiest option.

You install Python **one time**. After that, you simply double-click:

```text
run.bat
```

and your library opens in your browser.

You don't need to know Python or write code.

**Install Python from the official website:**  
https://www.python.org/downloads/

During installation, if you see:

> **Add Python.exe to PATH**

make sure it is checked.

After Python is installed, double-click `run.bat`.

**You do not need to install Python again every time.**

### No Python? That's okay.

You can also use the app directly in your browser.

Open:

```text
public/index.html
```

Then select or drag & drop your Instagram HTML files:

```text
saved_posts.html
saved_collections.html
saved_music.html
```

The library will load directly in your browser.

**The trade-off:** you'll need to select the files again whenever you use browser mode.

So, in simple terms:

| | Recommended | Browser mode |
|---|---|---|
| Python needed | Once | No |
| Setup | One-time | None |
| Open later | Double-click `run.bat` | Open `index.html` + select files |
| Select files every time | No | Yes |
| Best for | Regular use | Quick / no-install use |

If you're not technical, **we recommend the Python option** because after the one-time setup it is much simpler.

## What happens to your Instagram export?

The app does **not** turn your export into another complicated database.

It reads the saved data you already downloaded from Instagram and presents it as a library:

```text
Instagram data export
        ↓
   saved/ folder
        ↓
Instagram Saved Library
        ↓
┌──────────────────────────────┐
│ Collections                  │
│ All Saved                    │
│ Music                        │
│                              │
│ Search captions / creators   │
│                              │
│ [Post] [Reel] [Post] [Reel]  │
└──────────────────────────────┘
```

---

## Common questions

### How do I save my Instagram posts before deleting my account?

Request your Instagram data export first and include your **Saved items**. Then use Instagram Saved Library to turn the exported saved data into a browsable local library.

### What happens to my saved posts if I delete Instagram?

Your Instagram account and its saved content may no longer be available to you after deletion. If you want to keep a record of what you saved, request your data export before deleting your account and use this app to organize the exported saved data.

### I downloaded my Instagram data, but it's just HTML. What do I do?

That's exactly what this app is for. Put the app inside the exported `saved` folder and open it. It turns the saved data into a visual, searchable library instead of making you browse raw HTML files.

### How do I view Instagram saved posts from an HTML export?

Use the exported `saved` folder with Instagram Saved Library. The app reads the saved-post HTML and presents it as a visual gallery.

### Can I keep my saved Instagram Reels after deleting Instagram?

The library keeps the saved Reel/post information contained in your export organized on your computer so you can revisit the saved links.

### Can I search my Instagram saved posts?

Yes. Search captions, `@creators`, and `#hashtags`.

### Can I keep my Instagram saved collections?

Yes. The app reads saved collection information from the export and lets you browse your collections.

### Do I need to upload my Instagram data?

No. The app is designed to run locally. Your exported files stay on your computer.

### Do I need Python?

**Only for the recommended one-click experience.** Install it once, then double-click `run.bat` whenever you want to open your library.

If you don't want to install Python, use the browser mode by opening `public/index.html` and selecting your exported HTML files.

### Do I need a GitHub account?

No. You can download the project using **Code → Download ZIP** without creating a GitHub account.

## Privacy

Everything runs locally on your machine.

- 🔒 No Instagram password
- ☁️ No cloud archive
- 🚫 No account required
- 🚫 No tracking
- 💻 Your exported files stay on your computer
- 🌐 Instagram's public embed/CDN may be contacted when the app displays post previews

 > **Important: The saved posts themselves belong to their original creators. This project helps you organize your own exported saved-content data; it does not grant rights to redistribute third-party content.**

---

## Requirements

- Python **3.10+**
- Windows, macOS, or Linux
- Your Instagram data export containing Saved items

**No third-party Python packages are required.**

---

## Tech

- Python standard library
- Vanilla JavaScript
- HTML / CSS
- Local HTTP server
- Instagram data export HTML

The frontend is intentionally lightweight: no framework and no package installation required.

---

## Why not just keep the Instagram export?

Because an export is useful as **data**, but it is not necessarily a useful **library**.

If your goal is:

> “I'm leaving Instagram, but I want to keep the things I spent years saving.”

then this project is the visual layer between the raw export and the library you actually wanted.

---

## Contributing

Issues, improvements and pull requests are welcome.

If Instagram changes its export structure, please open an issue with an example of the changed structure (without uploading private personal data).

---

## License

This project is licensed under the [MIT License](LICENSE).

<div align="center">

**Built for people who want to leave Instagram without leaving their saved knowledge behind. ❤️**

</div>
