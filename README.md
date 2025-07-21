<p align="center">
  <img src="https://www.dropbox.com/scl/fi/bnlbcwbjpx7uepl6ivji7/Krazy-Notesy-Logo.png?raw=0" alt="Krazy Notesy Logo" width="200"/>
</p>

<h1 align="center">🚀 Krazy Notesy Instagram Auto Uploader</h1>

<p align="center">
  <img src="https://www.dropbox.com/scl/fi/kakbm1mycro7ekts723ey/Krazy-Notesy-Banner.png?raw=0" alt="Krazy Notesy Banner"/>
</p>

---

## 🎉 What is this?

**Krazy Notesy Auto Uploader** is a Python-powered bot that:
- Automatically picks videos/images from Dropbox.
- Generates fun, Hinglish captions automatically.
- Uploads content to your Instagram page **daily**, using GitHub Actions.
- Fully automated. Runs even if your system is off.

---

## 📂 Project Structure

krazy_notesy_uploader/
├── media_links.json
├── uploader.py
├── fetch_dropbox_links.py
├── captions.py
├── .github/
│ └── workflows/
│ └── schedule.yml
├── .env
└── README.md

markdown
Copy
Edit

---

## ⚙️ Setup Guide

1. **Clone the Repo**  
   `git clone https://github.com/yourusername/krazy_notesy_uploader.git`

2. **Add Secrets in GitHub**  
   Go to your repo settings → Secrets → Actions:
   - `INSTAGRAM_USERNAME`
   - `INSTAGRAM_PASSWORD`
   - `DROPBOX_ACCESS_TOKEN`

3. **Prepare Dropbox Folder**
   - Upload your media to a specific Dropbox folder (example: `/krazy_notesy_media`).

4. **Generate `media_links.json`**  
   Run:
   ```bash
   python fetch_dropbox_links.py
This auto-generates direct download links for all media files.

GitHub Actions Automation

The .github/workflows/schedule.yml handles daily posting.

Customizable schedule via cron jobs.

🎬 How It Works
fetch_dropbox_links.py – Scans Dropbox folder, generates links.

uploader.py – Picks unposted file, generates caption, uploads to Instagram.

captions.py – Stores hundreds of pre-generated Hinglish funny captions.

schedule.yml – Automates daily posting via GitHub Actions.

✨ Features
😄 Hinglish Funny Captions

📸 Automatic Uploads

☁️ Dropbox-Powered Storage

🤖 100% Automated via GitHub Actions

🛡️ Secure using GitHub Secrets

📢 Follow the Fun
Stay connected with #KrazyNotesy for more!

<p align="center"> <b>Made with ❤️ for Krazy Notesy</b> </p> ```
