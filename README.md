<div align="center">

# 📦 Instagram Saved Library

### Delete Instagram without losing your saved posts and Reels.

**Turn your Instagram data export into a private, searchable visual library.**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Privacy: Local & Offline](https://img.shields.io/badge/Privacy-Local%20%26%20Offline-purple.svg)](#privacy)
[![Platform: Windows · Mac · Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-orange.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Instagram gives you an HTML export. This turns it into the saved-post library you actually wanted.**

</div>

---

![Instagram Saved Library — searchable saved posts, Reels, collections and music](public/screenshots/1.png)

## If you're deleting Instagram, start here

You may want to leave Instagram because you are tired of the scrolling, the distraction, or simply do not want to use it anymore.

But then you remember:

**“What happens to all the posts and Reels I saved?”**

You request your Instagram data.

Then you open the download and find **HTML files, text and links** instead of a normal gallery.

**That's exactly what this app is for.**

It takes the saved-content data from your Instagram export and turns it into a **visual, searchable library** you can keep on your own computer.

> **Instagram export → this app → your saved library.**

---

## You do NOT need to be technical

You do not need to know:

- Python
- coding
- Git
- databases
- command-line tools

If you can **download a ZIP file, open a folder and double-click a file**, you can use this app.

---

# Step-by-step: how to use it

You have **two ways to use the app**.

### ⭐ Recommended: install Python once

This gives you the easiest experience. After the one-time setup, you can open your saved library whenever you want by double-clicking `run.bat`.

### No Python? Use browser mode

You can open `public/index.html` directly and select or drag & drop your Instagram HTML files. This requires no installation, but you will need to select the files again each time you use it.

---

## Step 1 — Download your Instagram data

First, ask Instagram for your data.

On Instagram.com:

1. Click **More**.
2. Open **Settings**.
3. Open **Accounts Center**.
4. Go to **Your information and permissions**.
5. Choose **Download your information**.
6. Choose **Download or transfer information**.
7. Select your Instagram account.
8. Choose **Some of your information**.
9. Select **Saved items**:
   - ✅ Saved posts
   - ✅ Saved collections
   - ✅ Saved music
10. Choose **HTML** as the format.
11. Choose **All time** as the date range.
12. Request the download.

Instagram will prepare your data and give you a download link.

Download the ZIP file and **unzip/extract it**.

### What should I download?

If Instagram gives you a choice between **HTML** and **JSON**, choose:

**HTML**

This project is designed around the HTML export.

---

## Step 2 — Find the `saved` folder

Open the folder you just extracted.

You are looking for a folder named:

```text
saved
```

Inside it, you should see files similar to:

```text
saved/
├── saved_posts.html
├── saved_collections.html
└── saved_music.html
```

You do **not** need to understand or edit these HTML files.

---

## Step 3 — Download this app

At the top of this GitHub page, click:

**Code → Download ZIP**

You do **not** need a GitHub account just to download the ZIP.

Then:

1. Open the downloaded ZIP.
2. Extract/unzip it.
3. You will get the app folder.

---

## Step 4 — Put the app inside your `saved` folder

Take the extracted **Instagram Saved Library** folder and move it inside the `saved` folder from Step 2.

You want the structure to look like:

```text
saved/
├── saved_posts.html
├── saved_collections.html
├── saved_music.html
└── instagram-saved-library/
    ├── run.bat
    ├── app.py
    └── public/
```

This is simply **moving one folder into another**.

You do not need to rename the Instagram HTML files.

---

# ⭐ Recommended: Install Python once

If you want the easiest experience, do this one time.

**You do not need to learn Python or write code.**

Python is simply the small local program that lets `run.bat` start the app automatically.

## 1. Download Python

Use the official Python website:

https://www.python.org/downloads/

Choose a current Python 3 release.

## 2. Open the Python installer

When the installer appears, look near the bottom of the first screen.

If you see:

> ☑ **Add Python.exe to PATH**

**make sure it is checked.**

Then click:

> **Install Now**

## 3. Wait for installation to finish

That's all.

You only need to install Python **once** on that computer.

## 4. Start your library

Go back to:

```text
instagram-saved-library/
```

and double-click:

```text
run.bat
```

A browser window should open automatically with your saved library.

### From now on

You don't need to install Python again.

Whenever you want to use your library:

> **Double-click `run.bat`.**

---

# No Python? Use browser mode instead

If you don't want to install Python, that's completely okay.

The app has a browser-only mode.

## 1. Open

```text
instagram-saved-library/public/index.html
```

You can open `index.html` in your browser.

## 2. Select or drag & drop your Instagram HTML files

Choose the files from your exported `saved` folder:

```text
saved_posts.html
saved_collections.html
saved_music.html
```

You can select them together.

## 3. Your library loads

The files are parsed directly in your browser.

### The one trade-off

With browser-only mode, you will need to select your exported HTML files **again each time you use the app**.

So:

| | Python setup | Browser mode |
|---|---|---|
| Install anything? | Python once | No |
| First setup | A few minutes | Almost immediate |
| Open later | ⭐ Double-click `run.bat` | Open `index.html` + select files |
| Select HTML files every time? | **No** | **Yes** |
| Best for | ⭐ Regular use | Trying it / no-install computers |

**Our recommendation:** if this is your own computer and you plan to use the library more than once, install Python once.

---

## What if I'm completely new to GitHub?

That's okay.

You only need GitHub for **downloading the app**.

You do not need to:

- create a repository
- use Git
- use a terminal
- understand programming
- edit Python code

Just:

**Code → Download ZIP → Extract → Put the folder inside `saved`.**

---

# Requirements

### ⭐ Recommended: Windows + Python

For the easiest one-click experience:

- Windows
- Your Instagram HTML data export
- Python installed once

### No Python?

You can still use browser-only mode:

- Windows, macOS or Linux
- Your Instagram HTML data export
- A modern web browser
- No Python required

No third-party Python packages are required.

---

# Tech

- Python standard library
- Vanilla JavaScript
- HTML / CSS
- Local HTTP server
- Instagram data export HTML

The frontend is intentionally lightweight: no framework and no package installation required.

---

# Is this an Instagram backup?

Not exactly.

This is a **saved-content library built from your Instagram data export**.

It is meant for the specific problem:

> **“I'm leaving Instagram, but I want to keep and browse the things I spent years saving.”**

It does not replace Instagram's own account backup and does not claim ownership of third-party media.

---

# Contributing

Issues, improvements and pull requests are welcome.

If Instagram changes its export structure, please open an issue with an example of the changed structure.

**Please never upload private Instagram exports or personal data to an issue.**

---

# License

Released under the **MIT License**.

<div align="center">

**Built for people who want to leave Instagram without leaving their saved knowledge behind. ❤️**

</div>
