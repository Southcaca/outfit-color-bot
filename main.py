import os
import random
from datetime import datetime
import requests

# 五行對應顏色與加持效果
wuxing_colors = {
    "木": {
        "colors": ["綠色", "青色"],
        "boost": "招貴人、拓展人脈",
        "outfit": "綠色襯衫＋白色褲裙，清新又有朝氣"
    },
    "火": {
        "colors": ["紅色", "粉紅色"],
        "boost": "提升桃花、人緣魅力",
        "outfit": "紅色連身裙＋玫瑰金耳環，自信又吸睛"
    },
    "土": {
        "colors": ["黃色", "棕色"],
        "boost": "穩定氣場、開運避煞",
        "outfit": "米黃針織＋卡其褲，穩重又溫柔"
    },
    "金": {
        "colors": ["白色", "銀色"],
        "boost": "提升判斷力、業績能量",
        "outfit": "白襯衫＋金屬配飾，專業又幹練"
    },
    "水": {
        "colors": ["藍色", "黑色"],
        "boost": "靜心避煞、提升智慧",
        "outfit": "深藍上衣＋灰褲，沉穩有思考力"
    }
}

# 推薦配飾 & 歌曲
accessories = ["玫瑰金耳環", "銀色手鍊", "珍珠髮飾", "金色項鍊", "琥珀戒指"]
songs = [
    ("笑一個吧 – 吳汶芳", "https://youtu.be/DKn6lR_GQZs"),
    ("Walking on Sunshine – Katrina & The Waves", "https://youtu.be/iPUmE-tne5U"),
    ("紅色高跟鞋 – 蔡健雅", "https://youtu.be/HQgJgDU3vv0"),
    ("綠光 – 孫燕姿", "https://youtu.be/Ju6UW35lAr4")
]

# 簡單取流日主五行（以天干為主）
def get_daily_wuxing():
    day = datetime.now().day
    wuxing_order = ["木", "火", "土", "金", "水"]
    return wuxing_order[day % 5]

def generate_message():
    today = datetime.now().strftime("%Y/%m/%d")
    main_wuxing = get_daily_wuxing()
    wuxing_list = list(wuxing_colors.keys())

    # 排序：主五行 → 次喜五行 → 中立
    ranked = [main_wuxing] + random.sample([w for w in wuxing_list if w != main_wuxing], 2)
    levels = ["大吉", "次吉", "吉"]
    emojis = ["🌟", "✨", "✅"]

    lines = [f"👗 {today} 的貝卡穿搭日報來囉：\n", "建議貝卡今天可以穿這些顏色：\n"]

    for i in range(3):
        w = ranked[i]
        info = wuxing_colors[w]
        color = random.choice(info["colors"])
        boost = info["boost"]
        outfit = info["outfit"]
        lines.append(f"{emojis[i]} {color}（{levels[i]}）：{boost}\n穿搭建議：{outfit}\n")

    acc = random.choice(accessories)
    song_title, song_link = random.choice(songs)

    lines.append(f"\n💍 幸運配飾：{acc}")
    lines.append(f"🎵 今日推薦歌曲：{song_title}\n🔗 {song_link}")
    lines.append("\n建議貝卡從衣櫃裡找找這些顏色，今天 vibe 穩穩的 🍀")

    return "\n".join(lines)

def send_to_line(text):
    token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
    user_id = os.environ["LINE_CHANNEL_USER_ID"]
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    body = {
        "to": user_id,
        "messages": [{
            "type": "text",
            "text": text
        }]
    }
    r = requests.post(url, headers=headers, json=body)
    print("Status:", r.status_code)
    print(r.text)

if __name__ == "__main__":
    message = generate_message()
    send_to_line(message)