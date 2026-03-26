from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# ใส่ค่าที่ได้จาก LINE Developer
LINE_CHANNEL_SECRET = "adcba3ccbe9d12f50132b9dd16148837"
LINE_CHANNEL_ACCESS_TOKEN = "x9oPzFDsRBybM+xv/TmkUNRyhG32lKCcvbWni64UTNBTRDB0Hjv46ROUXij/Lh4W3m2oa+eq1LiJ9JPWiOz4GnPtkhc7hMfMuMdIIrUFOejBHE5o1wftGN63vwL8cnTqrwVKKqB3J72jmaXD3DIr3AdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

# ตรงนี้คือสมองของ bot
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()

    if user_text == "ขอราคา" or user_text == "สวัสดี":
        reply = "สวัสดีครับเราจะรีบแจ้งกลับโดยไวที่สุดครับ"
    else:
        reply = "สวัสดีครับเราจะรีบแจ้งกลับโดยไวที่สุดครับ"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )