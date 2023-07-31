import argparse
from dotenv import load_dotenv
import requests
from space_image_utils import download_images_from_urls


def fetch_spacex_last_launch(launch_id):
    base_url = f"https://api.spacexdata.com/v4/launches/{launch_id}"
    response = requests.get(base_url)
    response.raise_for_status()
    launch_info_from_api = response.json()

    image_links = launch_info_from_api.get("links", {}).get("flickr", {}).get("original", [])

    if image_links:
        save_folder = "images"
        download_images_from_urls(image_links, save_folder, "spacex")
    else:
        print("Не найдено ссылок на изображения.")

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Скрипт для скачивания фотографий запусков с сайта SpaceX.")
    parser.add_argument("--launch_id", help="ID запуска SpaceX", default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()

    fetch_spacex_last_launch(args.launch_id)
