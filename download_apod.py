import argparse
from dotenv import load_dotenv
import os
import requests
from space_image_utils import download_image
from datetime import datetime


def fetch_nasa_images(date, api_key):
    params = {
        "api_key": api_key,
        "date": date
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    apod_response_content = response.json()

    if not ("url" in apod_response_content and apod_response_content["media_type"] == "image"):
        print("Не найдено ссылок на изображения.")
        return

    image_links = [apod_response_content["url"]]
    save_folder = "images"
    filename_prefix = "apod"

    os.makedirs(save_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    for index, image_url in enumerate(image_links, start=1):
        download_image(image_url, save_folder, filename_prefix, timestamp, index)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")

    parser = argparse.ArgumentParser(
        description="Скрипт для скачивания фотографий Astronomy Picture of the Day (APOD) с сайта NASA.")
    parser.add_argument("--date", help="Дата изображения APOD (YYYY-MM-DD)", default="2023-08-01")
    args = parser.parse_args()

    fetch_nasa_images(args.date, api_key)
