from telegram import Bot
from dotenv import load_dotenv
import os

def post_text_to_channel(message, channel_id, bot_token):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=channel_id, text=message)

if __name__ == "__main__":

    load_dotenv()

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    channel_id = os.getenv("CHANNEL_ID")
    message = "Привет"
    post_text_to_channel(message, channel_id, bot_token)
