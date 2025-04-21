message = f"👗 {today} 的穿搭幸運色提醒來囉～\n\n建議貝卡今天可以穿點這些顏色：\n"

for color in recommendations:
    color_name = color["color"]
    level = color["level"]
    suggestion = color["suggestion"]
    emoji = {"大吉": "❤️", "次吉": "💗", "吉": "🤍"}.get(level, "")
    message += f"\n- {color_name}（{level} {emoji}）：{suggestion}"

message += f"\n\n💍 幸運配飾建議：{accessory}\n"

message += f"\n🎵 今日推薦歌曲：\n{song['title']} – {song['artist']}\n{song['url']}\n"
message += "\n今天也穿得剛剛好，氣場滿分唷～🌟"