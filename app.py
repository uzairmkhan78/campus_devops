from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Campus DevOps Project",
        "status": "Running",
        "technology": "Docker + Kubernetes",
        "message": "Welcome to my campus project!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
