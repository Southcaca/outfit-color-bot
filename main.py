import os
import requests
import datetime

def get_today_color():
    today = datetime.date.today()
    weekday = today.weekday()  # 0=Monday, 6=Sunday
    color_map = {
        0: "紅色",   # Monday
        1: "粉紅色", # Tuesday
        2: "綠色",   # Wednesday
        3: "橘色",   # Thursday
        4: "藍色",   # Friday
        5: "紫色",   # Saturday
        6: "黃色"    # Sunday
    }
    return color_map.get(weekday, "未知")

def send_line_notify(message):
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = os.getenv("LINE_USER_ID")
    
    if not token:
        print("Error: LINE_CHANNEL_ACCESS_TOKEN not set.")
        return
    if not user_id:
        print("Error: LINE_USER_ID not set.")
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
    message = f"今天是 {today.strftime('%Y年%m月%d日')}，貝卡建議的穿搭幸運色是「{color}」！"
    send_line_notify(message)