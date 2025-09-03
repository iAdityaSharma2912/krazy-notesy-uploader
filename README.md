<p align="center">
  <img src="https://github.com/iAdityaSharma2912/Files/blob/main/Krazy%20Notesy%20Logo.png" alt="Krazy Notesy Logo" width="200"/>
</p>

<h1 align="center"> Krazy Notesy </h1>

<p align="center">
  <img src="https://github.com/iAdityaSharma2912/Files/blob/main/Krazy%20Notesy%20Banner.png" alt="Krazy Notesy Banner"/>
</p>
<h2 align="center"> Krazy Notesy </h2>

**Krazy Notesy** is an **AI-powered social media automation system** built to make life easier for **content creators**.

It can handle **any type of media file** (videos, images, GIFs, reels, shorts, memes, animations, etc.) and automatically:

* Generates **captions & hashtags** using AI 🤖
* **Schedules posts** across multiple platforms
* Formats & optimizes media for each platform
* Tracks performance with an **analytics dashboard** 📊

Krazy Notesy = Your **hands-free posting assistant** 🕒

---

## ✨ Features

* 🎬 Upload any media file (videos, images, GIFs, reels, memes…)
* 🤖 Auto-generate creative captions & trending hashtags
* 📅 Schedule posts in advance (set it & forget it)
* 📊 Analytics dashboard (views, likes, comments, engagement)
* 🔄 Automatic resizing & formatting for each platform
* 🌐 Multi-platform posting (Instagram, YouTube, Reddit, X/Twitter)
* ⚙️ Automated daily posting via **GitHub Actions + CRON jobs**

---

## 🏗️ Tech Stack

### **Frontend**

* React.js (Vite)
* Tailwind CSS
* ShadCN / Material UI
* Recharts (analytics graphs)
* Framer Motion (animations)

### **Backend**

* Node.js + Express
* MongoDB Atlas / Firebase Firestore
* REST API with JWT Authentication

### **AI & Automation**

* OpenAI API → Captions & Hashtags
* Python → Automation Scripts (MoviePy, FFmpeg, PRAW, Tweepy)
* GitHub Actions → Scheduled posting & automation

### **Deployment**

* Frontend → Vercel / Netlify
* Backend → Render / Railway
* Database → MongoDB Atlas / Firebase
* Secrets → GitHub Actions Encrypted Secrets

---

## 📂 Project Structure

```
krazy-notesy/
├── frontend/    # React + Tailwind (Dashboard UI)
├── backend/     # Node.js + Express API
├── scripts/     # Python automation scripts
├── database/    # MongoDB / Firebase config
└── .github/
    └── workflows/   # GitHub Actions automation
```

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/your-username/krazy-notesy.git
cd krazy-notesy
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

👉 Runs at: `http://localhost:5173`

### 3. Backend Setup

```bash
cd ../backend
npm install
npx nodemon server.js
```

👉 Runs at: `http://localhost:5000`

### 4. Python Scripts Setup

```bash
cd ../scripts
python -m venv venv
venv\Scripts\activate   # Windows
pip install openai moviepy praw tweepy
```

---

## 🚀 Roadmap

* [x] Project setup (frontend, backend, scripts)
* [ ] Build dashboard UI (upload panel, schedule, analytics)
* [ ] Connect backend API & database
* [ ] AI caption & hashtag generator
* [ ] Multi-platform posting automation
* [ ] Scheduler with GitHub Actions
* [ ] Deployment (Vercel + Railway + MongoDB Atlas)
* [ ] Analytics integration (views, likes, comments)
* [ ] Extra features (auto watermarking, subtitle generation, SaaS model)

---

## 📜 License

This project is licensed under the MIT License – free to use, modify, and share.

---
