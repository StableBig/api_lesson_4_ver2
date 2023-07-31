import argparse
from dotenv import load_dotenv
import os
import requests
from space_image_utils import download_images_from_urls

load_dotenv()

def fetch_nasa_images(date):
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)
    response.raise_for_status()
    image_data = response.json()

    if "url" in image_data and image_data["media_type"] == "image":
        image_links = [image_data["url"]]
        save_folder = "images"
        filename_prefix = "apod"
        download_images_from_urls(image_links, save_folder, filename_prefix)
    else:
        print("Не найдено ссылок на изображения.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Дата изображения APOD (YYYY-MM-DD)", default="2023-07-30")
    args = parser.parse_args()

    fetch_nasa_images(args.date)
