import os
import datetime
import requests

def get_lucky_color():
    today = datetime.datetime.now()
    weekday = "一二三四五六日"[today.weekday()]
    main_color = "深藍色"
    sub_color = "銀色"
    return f"今天是 {today.month}/{today.day}（{weekday}）\n適合穿上 {main_color} 配一點 {sub_color}，穩穩的氣場＋一點閃亮小巧思！\n今天的貴人可能就在妳身邊，記得多微笑～穿得對，運氣就來對！"

def send_line_notify(msg):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('LINE_CHANNEL_ACCESS_TOKEN')}"
    }
    data = {
        "to": os.getenv("USER_LINE_ID"),
        "messages": [{
            "type": "text",
            "text": msg
        }]
    }
    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    message = get_lucky_color()
    send_line_notify(message)