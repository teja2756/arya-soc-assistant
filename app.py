from flask import Flask, jsonify, render_template, request
from soc_engine import analyze_alert

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/analyze")
def analyze():
    payload = request.get_json(silent=True) or {}
    result = analyze_alert(payload)
    return jsonify(result)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "ARYA SOC Assistant"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
