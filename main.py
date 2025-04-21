
import requests
import datetime

def get_today_message():
    # 這裡應該是你命盤邏輯生成的幸運色與推薦內容
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"🌈 {today} 的穿搭日報來啦～\n\n✨ 大吉色：紅色\n🌟 次吉色：粉色\n✅ 吉色：橘色\n\n💍 幸運配飾建議：戴上玫瑰金耳環，更有魅力唷！\n\n🎵 今日推薦歌曲：\n《紅色高跟鞋》- 蔡健雅：https://youtu.be/HQgJgDU3vv0\n\n建議貝卡從衣櫃裡找找這些顏色，今天也會是 Lucky Day！🍀"

def send_line_message(token, user_id, message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    body = {
        "to": user_id,
        "messages": [{
            "type": "text",
            "text": message
        }]
    }
    response = requests.post("https://api.line.me/v2/bot/message/push", json=body, headers=headers)
    print("Response:", response.status_code, response.text)

if __name__ == "__main__":
    access_token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = "U0b3096d68edce6d5b38132042362be9d"  # southcaca 的 LINE user ID
    message = get_today_message()
    send_line_message(access_token, user_id, message)
幸運配飾：{accessory} 💍
推薦歌曲：{song} 🎶
{song_link}
祝你今天心情愉快！😊"""
    send_line_notify(message)
