import os
import requests
import random
from datetime import datetime

# LINE Bot 資訊
ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
USER_ID = os.environ['LINE_CHANNEL_USER_ID']
URL = 'https://api.line.me/v2/bot/message/push'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# 模擬吉色分級推薦
colors = [
    ("紅色", "大吉 ❤️"),
    ("粉紅", "大吉 💗"),
    ("藍色", "次吉 💙"),
    ("白色", "次吉 🤍"),
    ("黃色", "吉 💛"),
    ("綠色", "吉 💚"),
]

# 模擬幸運配飾
accessories = [
    "金色耳環",
    "銀色手環",
    "珍珠項鍊",
    "圓形戒指",
    "玫瑰金手錶",
    "小香風別針",
]

# 模擬歌曲推薦（可換連結）
songs = [
    ("Daylight – Taylor Swift", "https://youtu.be/NutJRqqY6hE"),
    ("Walking on Sunshine – Katrina & The Waves", "https://youtu.be/iPUmE-tne5U"),
    ("笑一個吧 – 吳汶芳", "https://youtu.be/DKn6lR_GQZs"),
    ("青空 – aiko", "https://youtu.be/ncX2SBIaVuY"),
]

# 產生今天訊息
today = datetime.now().strftime("%Y/%m/%d")
color, fortune = random.choice(colors)
accessory = random.choice(accessories)
song_title, song_link = random.choice(songs)

message = f"""👗 {today} 的穿搭幸運色提醒來囉！

建議貝卡今天可以穿「{color}」✨
▶ 幸運等級：{fortune}

幸運配飾: {accessory} 💍

🎵 今日推薦歌曲：
{song_title}
{song_link}

祝妳一整天順順順，走到哪裡都有好運氣 💖
"""

body = {
    "to": USER_ID,
    "messages": [{
        "type": "text",
        "text": message
    }]
}

response = requests.post(URL, headers=headers, json=body)
print("Status Code:", response.status_code)
print("Response:", response.text)