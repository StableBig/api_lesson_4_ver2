from telegram import Bot
from dotenv import load_dotenv
import os

def post_text_to_channel(message, channel_id, bot_token):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=channel_id, text=message)

def post_image_to_channel(image_path, channel_id, bot_token):
    bot = Bot(token=bot_token)
    with open(image_path, "rb") as image_file:
        bot.send_photo(chat_id=channel_id, photo=image_file)

if __name__ == "__main__":

    load_dotenv()

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    channel_id = os.getenv("CHANNEL_ID")
    message = "Привет"
    image_path = "images/apod_20230730222658_1.jpg"
    post_text_to_channel(message, channel_id, bot_token)
    post_image_to_channel(image_path, channel_id, bot_token)
