import argparse
from dotenv import load_dotenv
import os
import requests
from space_image_utils import download_images_from_urls


def fetch_nasa_images(date, api_key):
    params = {
        "api_key": api_key,
        "date": date
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    image_info_from_api = response.json()

    if not ("url" in image_info_from_api and image_info_from_api["media_type"] == "image"):
        print("Не найдено ссылок на изображения.")
        return

    image_links = [image_info_from_api["url"]]
    save_folder = "images"
    filename_prefix = "apod"
    download_images_from_urls(image_links, save_folder, filename_prefix)

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")

    parser = argparse.ArgumentParser(description="Скрипт для скачивания фотографий Astronomy Picture of the Day (APOD) с сайта NASA.")
    parser.add_argument("--date", help="Дата изображения APOD (YYYY-MM-DD)", default="2023-07-30")
    args = parser.parse_args()

    fetch_nasa_images(args.date, api_key)
