import os
import requests
import datetime
import random

def get_today_color():
    today = datetime.date.today()
    weekday = today.weekday()  # 0=Monday, 6=Sunday
    color_map = {
        0: "紅色",     # Monday
        1: "粉紅色",   # Tuesday
        2: "綠色",     # Wednesday
        3: "橘色",     # Thursday
        4: "藍色",     # Friday
        5: "紫色",     # Saturday
        6: "黃色"      # Sunday
    }
    return color_map.get(weekday, "未知")

def get_color_grade(color):
    # 根據顏色提供分級建議
    grade_map = {
        "紅色": "大吉",
        "粉紅色": "次吉",
        "綠色": "吉",
        "橘色": "吉",
        "藍色": "次吉",
        "紫色": "大吉",
        "黃色": "吉"
    }
    return grade_map.get(color, "吉")

def get_accessory(color):
    # 根據顏色推薦配飾
    accessory_map = {
        "紅色": "紅寶石項鍊",
        "粉紅色": "玫瑰金耳環",
        "綠色": "翡翠手鐲",
        "橘色": "琥珀戒指",
        "藍色": "藍寶石胸針",
        "紫色": "紫水晶手鍊",
        "黃色": "黃金髮夾"
    }
    return accessory_map.get(color, "幸運配飾")

def get_song_recommendation(color):
    # 根據顏色推薦歌曲
    song_map = {
        "紅色": ("紅色高跟鞋 - 蔡健雅", "https://www.youtube.com/watch?v=example1"),
        "粉紅色": ("粉紅色的回憶 - 小虎隊", "https://www.youtube.com/watch?v=example2"),
        "綠色": ("綠光 - 孫燕姿", "https://www.youtube.com/watch?v=example3"),
        "橘色": ("橘子汽水 - 南拳媽媽", "https://www.youtube.com/watch?v=example4"),
        "藍色": ("藍色的愛 - 張學友", "https://www.youtube.com/watch?v=example5"),
        "紫色": ("紫色 - 范逸臣", "https://www.youtube.com/watch?v=example6"),
        "黃色": ("黃色的玫瑰 - 張信哲", "https://www.youtube.com/watch?v=example7")
    }
    return song_map.get(color, ("今日無推薦歌曲", ""))

def send_line_notify(message):
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = os.getenv("LINE_CHANNEL_USER_ID")
    if not token:
        print("Error: LINE_CHANNEL_ACCESS_TOKEN not set.")
        return
    if not user_id:
        print("Error: LINE_CHANNEL_USER_ID not set.")
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "to": user_id,
        "messages": [{
            "type": "text",
            "text": message
        }]
    }
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)
    print("LINE response:", response.status_code, response.text)

if __name__ == "__main__":
    today = datetime.date.today()
    color = get_today_color()
    grade = get_color_grade(color)
    accessory = get_accessory(color)
    song, song_link = get_song_recommendation(color)
    message = f"""今天是 {today.strftime('%Y年%m月%d日')} 🎉
建議貝卡今天穿點「{color}」喔！✨
幸運等級：{grade}
幸運配飾：{accessory} 💍
推薦歌曲：{song} 🎶
{song_link}
祝你今天心情愉快！😊"""
    send_line_notify(message)