from flask import Flask, render_template, request, jsonify, send_file
import qrcode
import os
import uuid

app = Flask(__name__)

QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_qr():
    data = request.json.get("url")

    if not data:
        return jsonify({"error": "URL is required"}), 400

    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(QR_FOLDER, filename)

    img = qrcode.make(data)
    img.save(filepath)

    return jsonify({
        "qr_url": f"/{filepath}"
    })

@app.route("/download/<filename>")
def download(filename):
    path = os.path.join(QR_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
