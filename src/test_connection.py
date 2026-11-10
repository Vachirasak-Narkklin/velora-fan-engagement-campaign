import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

if not api_key:
    raise SystemExit("ไม่เจอ YOUTUBE_API_KEY ใน .env")

youtube = build("youtube", "v3", developerKey=api_key)

response = youtube.channels().list(
    part="snippet,statistics",
    forHandle="@YouTube",
).execute()

channel = response["items"][0]
print("✅ เชื่อมต่อสำเร็จ")
print("Channel:", channel["snippet"]["title"])
print("Subscribers:", channel["statistics"].get("subscriberCount"))
