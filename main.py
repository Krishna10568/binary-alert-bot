
import time
from ai_predictor import get_prediction
from telegram_bot import send_telegram_message

BOT_TOKEN = '7985173188:AAFb9z40_LGAZDvgo2cIvWoZ8gN43fnB3wM'
CHAT_ID = '949767869'

def create_message():
    prediction = get_prediction()
    message = f"""⚡ AI Signal Alert ⚡
Pair: {prediction['pair']}
Action: {prediction['action']}
Confidence: {prediction['confidence']}%
"""
    return message

if __name__ == '__main__':
    while True:
        msg = create_message()
        send_telegram_message(BOT_TOKEN, CHAT_ID, msg)
        time.sleep(900)  # 15 minutes gap
