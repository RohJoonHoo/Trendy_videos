from googleapiclient.discovery import build
import json
import re
import os

API_KEY = os.getenv("OPENYOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def convert_duration(iso_duration):
    pattern = re.compile(r'PT(\d+H)?(\d+M)?(\d+S)?')
    matches = pattern.match(iso_duration)

    hours = int(matches.group(1)[:-1]) if matches.group(1) else 0
    minutes = int(matches.group(2)[:-1]) if matches.group(2) else 0
    seconds = int(matches.group(3)[:-1]) if matches.group(3) else 0

    return f"{hours}:{minutes:02}:{seconds:02}" if hours > 0 else f"{minutes}:{seconds:02}"

def get_video_categories(region_code="KR"):
    """YouTube API에서 카테고리 ID와 이름을 가져오는 함수"""
    request = youtube.videoCategories().list(
        part="snippet",
        regionCode=region_code
    )
    response = request.execute()

    category_map = {item["id"]: item["snippet"]["title"] for item in response.get("items", [])}
    return category_map

def get_trending_videos(region_code="KR", max_results=42):
    """인기 동영상 목록 가져오기"""
    category_map = get_video_categories(region_code)  # ✅ 카테고리 ID-이름 매핑 가져오기

    request = youtube.videos().list(
        part="id,snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response.get("items", []):
        category_id = item["snippet"].get("categoryId", "0")
        category_name = category_map.get(category_id, "알 수 없음")  # ✅ 카테고리 이름 가져오기

        video_data = {
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "channel_name": item["snippet"]["channelTitle"],
            "category": category_name,  # ✅ 카테고리 추가
            "duration": convert_duration(item["contentDetails"]["duration"]),  
            "view_count": item["statistics"].get("viewCount", "0"),
            "thumbnail_url": item["snippet"]["thumbnails"]["high"]["url"]
        }
        videos.append(video_data)

    return videos

SAVE_DIR = "templates"
os.makedirs(SAVE_DIR, exist_ok=True)  # 폴더가 없으면 생성
SAVE_PATH = os.path.join(SAVE_DIR, "trending_videos.json")  # 최종 파일 경로

trending_videos = get_trending_videos()

with open(SAVE_PATH, "w", encoding="utf-8") as file:
    json.dump(trending_videos, file, ensure_ascii=False, indent=4)

print(f"데이터 저장 완료: {SAVE_PATH}")
