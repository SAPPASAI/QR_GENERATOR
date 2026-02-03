🔗 **QR Code Generator – Flask Web App**

A simple and modern web application that allows users to generate QR codes from any URL.
The backend is built using Flask, and the frontend provides a clean UI for instant preview and download of QR codes.

📸 **Project Preview**

Paste a URL → Click Generate → View QR → Download Image

🚀 **Features**

🔗 Accepts any valid URL

⚙️ Generates QR code on the backend

🖼️ Displays QR instantly on the frontend

⬇️ Allows user to download QR image

🎨 Modern glass-style UI

📱 Mobile responsive

☁️ Ready for cloud deployment (Render, Railway, etc.)
**
🧱 **Tech Stack**
Layer	Technology
Backend	Flask (Python)
QR Library	qrcode, Pillow
Frontend	HTML, CSS, JavaScript
Server	Gunicorn
Hosting	Render / Railway
📁 Project Structure
qr-generator/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── qrcodes/        # Generated QR images (ignored in git)
│
└── templates/
    └── index.html     # UI page

⚙️ **Setup Instructions (Local)**
1️⃣ Clone Repository
git clone https://github.com/your-username/qr-generator.git
cd qr-generator

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the App
python app.py


Open in browser:
👉 http://127.0.0.1:5000

🌍 Deployment (Render)

Push code to GitHub

Go to https://render.com

Click New → Web Service

Connect your GitHub repository

Build Command

pip install -r requirements.txt


Start Command

gunicorn app:app


Click Deploy

🛡️ .gitignore (Important)
venv/
static/qrcodes/
__pycache__/
*.pyc
.env