# YouTube Trending Video Filter

## 📌 프로젝트 개요
YouTube 트렌딩 비디오 페이지에 영상 길이 필터 기능을 추가하는 프로젝트입니다. Python 자동화 스크립트를 활용하여 데이터를 크롤링하고, Flask를 이용해 웹 서버를 제공합니다.

---

## 📂 파일 구성
- `ytcrawler.py` : YouTube 트렌딩 데이터를 크롤링하는 스크립트
- `ytapp.py` : Flask 서버를 실행하는 애플리케이션
- `index.html` : 웹 페이지의 프론트엔드 파일

---

## ⚙️ 설치 및 실행 방법

### 1️⃣ 필수 파일 다운로드
먼저, 아래 3개의 파일을 다운로드합니다.
```
📄 ytcrawler.py
📄 ytapp.py
📄 index.html
```

### 2️⃣ `ytcrawler.py` 실행 및 `templates` 폴더 생성
`ytcrawler.py`를 실행하여 필요한 JSON 파일을 생성하고, `templates` 폴더를 만듭니다.
```bash
python ytcrawler.py
```

### 3️⃣ `index.html` 파일 이동
생성된 `templates` 폴더 안으로 `index.html` 파일을 이동시킵니다.
```bash
mv index.html templates/
```

### 4️⃣ `ytapp.py`의 JSON 파일 경로 수정
`ytapp.py` 파일 내 `JSON_FILE_PATH` 경로를 JSON 파일이 저장된 위치로 변경합니다.

```python
JSON_FILE_PATH = "your/json/file/path/trending_videos.json"
```

### 5️⃣ Flask 서버 실행 및 접속
이제 Flask 서버를 실행하고, 웹 브라우저에서 페이지를 확인합니다.
```bash
python ytapp.py
```
서버가 실행되면 브라우저에서 아래 URL에 접속합니다.
```
http://127.0.0.1:5000/
```

---

## 🚀 추가 사항
- GitHub Actions를 활용하여 `trending_videos.json` 파일을 일정 간격으로 자동 업데이트할 예정입니다.
- 더 나은 UI/UX를 위해 프론트엔드 스타일링을 개선할 계획입니다.

---

## 🛠 기술 스택
- **Backend** : Python, Flask
- **Frontend** : HTML, CSS, JavaScript
- **Automation** : GitHub Actions, Python Script

---

## 📌 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다. 자유롭게 사용 및 수정 가능합니다.

