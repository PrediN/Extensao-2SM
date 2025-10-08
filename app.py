from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan-result", methods=["POST"])
def scan_result():
    data = request.json
    print("QR Code capturado:", data["qr"])
    return jsonify({"status": "ok", "message": f"Recebido: {data['qr']}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
