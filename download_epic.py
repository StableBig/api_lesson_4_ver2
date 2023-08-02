import argparse
from datetime import datetime
import os
import requests
from dotenv import load_dotenv
from space_image_utils import download_image


def get_image_urls(api_key, count):
    params = {
        "api_key": api_key
    }

    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=params)
    response.raise_for_status()

    epic_response_content = response.json()

    image_urls = []
    for epic_image in epic_response_content[:count]:
        request = requests.Request("GET",
                                   f"https://api.nasa.gov/EPIC/archive/natural/{get_date_from_iso(epic_image['date'])}/png/{epic_image['image']}.png",
                                   params=params)
        prepared_request = request.prepare()
        image_urls.append(prepared_request.url)
    return image_urls


def get_date_from_iso(iso_date):
    date_object = datetime.fromisoformat(iso_date.replace("T", " ").split(".")[0])
    return date_object.strftime("%Y/%m/%d")


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")

    parser = argparse.ArgumentParser(
        description="Скрипт для скачивания фотографий Earth Polychromatic Imaging Camera (EPIC) с сайта NASA.")
    parser.add_argument("--count", help="Количество изображений для загрузки", default=10, type=int)
    args = parser.parse_args()

    image_urls = get_image_urls(api_key, args.count)

    if image_urls:
        os.makedirs("images", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        for index, image_url in enumerate(image_urls, start=1):
            download_image(image_url, "images", "epic", timestamp, index)
    else:
        print("Не найдено ссылок на изображения.")
