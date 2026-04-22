from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def read_logs():
    logs = []
    try:
        with open("logs.json") as f:
            for line in f:
                logs.append(json.loads(line))
    except:
        pass
    return logs

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs")
def get_logs():
    return jsonify(read_logs())

if __name__ == "__main__":
    app.run(debug=True, port=5001)

