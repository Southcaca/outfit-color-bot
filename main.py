import datetime
import random
import requests
import os

# ===== 從 GitHub Secrets 讀取 LINE 資訊 =====
user_id = os.getenv("LINE_CHANNEL_USER_ID")
access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

# ===== 幸運色與分級建議 =====
lucky_colors = [
    {"color": "紅色", "level": "大吉", "emoji": "❤️", "suggest": "紅色連身裙＋紅唇，展現熱情與自信", "accessory": "玫瑰金手鍊"},
    {"color": "粉紅色", "level": "次吉", "emoji": "💗", "suggest": "粉嫩針織上衣＋珍珠耳環，氣質滿分", "accessory": "珍珠耳環"},
    {"color": "白色", "level": "吉", "emoji": "🤍", "suggest": "白襯衫＋米杏色長褲，氣場清爽又專業", "accessory": "珍珠項鍊"}
]

# ===== 歌曲推薦 =====
songs = [
    {"title": "笑一個吧 – 吳汶芳", "url": "https://youtu.be/DKn6lR_GQZs"},
    {"title": "Daylight – Taylor Swift", "url": "https://youtu.be/NutJRqqY6hE"},
    {"title": "青空 – aiko", "url": "https://youtu.be/ncX2SBIaVuY"},
    {"title": "Walking on Sunshine – Katrina & The Waves", "url": "https://youtu.be/iPUmE-tne5U"}
]

# ===== 日期 =====
today = datetime.date.today()
today_str = today.strftime("%Y/%m/%d")

# ===== 組合訊息 =====
header = f"👗 {today_str} 的穿搭幸運色提醒來囉～"
body = "建議貝卡今天可以穿點這些顏色："

for item in lucky_colors:
    body += f"\n\n- {item['color']}（{item['level']} {item['emoji']}）：{item['suggest']}"

accessory = f"\n\n🔮 幸運配飾建議：{lucky_colors[0]['accessory']}"
song = random.choice(songs)
song_msg = f"\n\n🎵 今日推薦歌曲：\n{song['title']}\n{song['url']}"
closing = "\n\n祝妳一整天順順順，走到哪裡都有好運氣 💖"

message = f"{header}\n\n{body}{accessory}{song_msg}{closing}"

# ===== 傳送 LINE 訊息 =====
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "to": user_id,
    "messages": [
        {
            "type": "text",
            "text": message
        }
    ]
}

response = requests.post(
    "https://api.line.me/v2/bot/message/push",
    headers=headers,
    json=data
)

print("Status Code:", response.status_code)
print("Response:", response.text)