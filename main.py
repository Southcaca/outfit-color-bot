import os
import requests
import random
from datetime import datetime

# LINE API 設定
ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
USER_ID = os.environ.get("LINE_CHANNEL_USER_ID")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# 顏色分級與穿搭建議
color_levels = [
    {
        "color": "紅色",
        "level": "大吉 ❤️",
        "advice": "紅色連身裙＋紅唇，展現熱情與自信"
    },
    {
        "color": "粉紅色",
        "level": "次吉 💗",
        "advice": "粉嫩針織上衣＋珍珠耳環，氣質滿分"
    },
    {
        "color": "白色",
        "level": "吉 🤍",
        "advice": "白襯衫＋米杏色長褲，氣場清爽又專業"
    }
]

# 幸運配飾建議
accessories = [
    "玫瑰金耳環",
    "銀色手環",
    "珍珠項鍊",
    "藍寶石戒指",
    "金色髮夾"
]

# 推薦歌曲（可依五行拓展）
songs = [
    ("笑一個吧 – 吳汶芳", "https://youtu.be/DKn6lR_GQZs"),
    ("Walking on Sunshine – Katrina & The Waves", "https://youtu.be/iPUmE-tne5U"),
    ("綠光 – 孫燕姿", "https://youtu.be/V7fvJ5o2Keg"),
    ("青空 – aiko", "https://youtu.be/ncX2SBIaVuY")
]

# 組裝訊息內容
today = datetime.now().strftime("%Y/%m/%d")
selected_colors = color_levels[:3]
accessory = random.choice(accessories)
song_title, song_link = random.choice(songs)

message = f"👗 {today} 的穿搭幸運色提醒來囉～\\n\\n建議貝卡今天可以穿點這些顏色：\\n"
for item in selected_colors:
    message += f"\\n- {item['color']}（{item['level']}）：{item['advice']}"

message += f"\\n\\n💍 幸運配飾建議：{accessory}"
message += f"\\n\\n🎵 今日推薦歌曲：\\n{song_title}\\n{song_link}"
message += "\\n\\n今天也穿得剛剛好，氣場滿分唷～🌟"

# 傳送 LINE 訊息
body = {
    "to": USER_ID,
    "messages": [{
        "type": "text",
        "text": message
    }]
}

response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
print("Status Code:", response.status_code)
print("Response:", response.text)