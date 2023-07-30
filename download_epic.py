import argparse
from datetime import datetime
import os
import requests
from dotenv import load_dotenv
from space_image_utils import download_images_from_urls

load_dotenv()

def get_image_urls(count):
    api_key = os.getenv("EPIC_API_KEY")
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}")
    response.raise_for_status()

    data = response.json()
    image_urls = [f"https://api.nasa.gov/EPIC/archive/natural/{get_date_from_iso(item['date'])}/png/{item['image']}.png?api_key={api_key}" for item in data][:count]
    return image_urls

def get_date_from_iso(iso_date):
    date_object = datetime.fromisoformat(iso_date.replace("T", " ").split(".")[0])
    return date_object.strftime("%Y/%m/%d")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="Количество изображений для загрузки", default=10, type=int)
    args = parser.parse_args()

    image_urls = get_image_urls(args.count)

    if image_urls:
        print("Список изображений:", image_urls)
        download_images_from_urls(image_urls, "images", 'epic')
    else:
        print("Не найдено ссылок на изображения.")
