import argparse
from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from space_image_utils import download_image


def fetch_spacex_last_launch(launch_id):
    base_url = f"https://api.spacexdata.com/v4/launches/{launch_id}"
    response = requests.get(base_url)
    response.raise_for_status()
    spacex_response_content = response.json()

    return spacex_response_content.get("links", {}).get("flickr", {}).get("original", [])


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Скрипт для скачивания фотографий запусков с сайта SpaceX.")
    parser.add_argument("--launch_id", help="ID запуска SpaceX", default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()

    image_urls = fetch_spacex_last_launch(args.launch_id)

    if image_urls:
        os.makedirs("images", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        for index, image_url in enumerate(image_urls, start=1):
            download_image(image_url, "images", "spacex", timestamp, index)
    else:
        print("Не найдено ссылок на изображения.")
