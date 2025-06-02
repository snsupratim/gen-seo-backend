# 🔥 AI Content Generator – Frontend & Backend Setup Guide

This project consists of two separate repositories:

- **Frontend**: React app hosted on Vercel
- **Backend**: Node.js + Python server hosted on Render

---

## 📁 Project Repositories

### 🌐 Frontend Repo

```
https://github.com/snsupratim/gen-seo-frontend
```

### ⚙️ Backend Repo

```
https://github.com/snsupratim/gen-seo-backend
```

---

## 🛠️ Setup Instructions (Local Development)

### ✅ Clone Both Repositories

```bash
git clone https://github.com/snsupratim/gen-seo-frontend.git
cd gen-seo-frontend
npm install

# In a second terminal
git clone https://github.com/snsupratim/gen-seo-backend.git
cd gen-seo-backend
npm install
pip install -r requirements.txt
```

### 🔐 Add Environment Variables

#### For Backend (`gen-seo-backend/.env`):

```
GOOGLE_API_KEY=your_gemini_api_key
```

#### For Frontend (`gen-seo-frontend/.env`):

```
REACT_APP_API_BASE_URL=http://localhost:5000
```

### ▶️ Run Locally

#### Backend:

```bash
cd aicontentgen-backend
npm start
```

#### Frontend:

```bash
cd aicontentgen-frontend
npm start
```

Visit: `http://localhost:3000`

---

## ☁️ Deployment Instructions

### 🔵 Frontend on Vercel

1. Go to [https://vercel.com](https://vercel.com)
2. Import the `gen-seo-frontend` GitHub repo
3. In **Project → Settings → Environment Variables**:

```
Key: REACT_APP_API_BASE_URL
Value: https://your-backend.onrender.com
```

4. Click **Deploy**

---

### 🟢 Backend on Render

1. Go to [https://render.com](https://render.com)
2. Click **New Web Service**
3. Import `genseo--backend` from GitHub
4. Set the following:

   - Runtime: Node
   - Build Command: `npm install`
   - Start Command: `./start.sh`

5. In **Environment Variables**:

```
Key: GOOGLE_API_KEY
Value: your_gemini_api_key
```

6. Click **Deploy**

✅ Make sure the `start.sh` and `requirements.txt` are present in the backend repo root.

---

## 🔄 API Endpoints for Testing

| Endpoint     | Method | Input Field | Description                |
| ------------ | ------ | ----------- | -------------------------- |
| /api/keyword | POST   | keyword     | Get 5 keyword suggestions  |
| /api/title   | POST   | keyword     | Generate 2–3 SEO titles    |
| /api/topic   | POST   | title       | Get 1–2 topic outlines     |
| /api/content | POST   | topic       | Generate 100–200 word blog |

---

## 🧪 Postman Sample

```json
POST /api/title
{
  "keyword": "AI writing tools"
}
```

---

## 📋 License

MIT – Free to use and modify.

---

## 👨‍💻 Developed by You

- React + Node.js + Python + Gemini AI
- Deploy: Vercel (frontend) + Render (backend)
