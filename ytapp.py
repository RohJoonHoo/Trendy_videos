from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# JSON 파일 경로 설정 (현재 디렉토리에서 직접 로드)
JSON_FILE_PATH = "C:/Users/kccistc/Desktop/workspace/data/trending_videos.json"

# 1️⃣ index.html 렌더링
@app.route("/")
def home():
    return render_template("index.html")

# 2️⃣ JSON 데이터를 API로 제공
@app.route("/api/videos")
def get_videos():
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
        video_data = json.load(file)
    return jsonify(video_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
