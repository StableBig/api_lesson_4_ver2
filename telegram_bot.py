import os
import time
import random
import argparse
from dotenv import load_dotenv
from telegram import Bot


def post_image_to_channel(image_path, channel_id, bot_token):
    bot = Bot(token=bot_token)
    with open(image_path, 'rb') as image_file:
        bot.send_photo(chat_id=channel_id, photo=image_file)


def get_all_images_from_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                yield os.path.join(root, file)


if __name__ == "__main__":
    load_dotenv()

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID")

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="Директория с изображениями для публикации", default="images")
    parser.add_argument("--hours", help="Интервал между публикациями", default=4, type=float)
    parser.add_argument("--image", help="Укажите определенную фотографию для публикации", default=None)
    args = parser.parse_args()

    all_images = list(get_all_images_from_directory(args.dir))
    random.shuffle(all_images)

    image_index = 0
    while True:
        post_image_to_channel(all_images[image_index % len(all_images)], channel_id, bot_token)
        time.sleep(args.hours * 60 * 60)
        image_index += 1
