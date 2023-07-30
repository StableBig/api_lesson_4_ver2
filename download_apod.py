import os
import requests
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv


load_dotenv()

def get_file_extension_from_url(url):
    url_components = urlsplit(url)
    path = unquote(url_components.path)
    _, file_extension = os.path.splitext(path)
    return file_extension

def download_images_from_urls(image_urls, save_folder):
    os.makedirs(save_folder, exist_ok=True)

    for index, image_url in enumerate(image_urls):
        image_extension = get_file_extension_from_url(image_url)
        image_name = f"nasa_image_{index + 1}{image_extension}"
        save_path = os.path.join(save_folder, image_name)

        response = requests.get(image_url)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"Скачано изображение {image_name}")

def fetch_nasa_images(count=10):
    base_url = "https://api.nasa.gov/planetary/apod"
    api_key = os.getenv("APOD_API_KEY")

    params = {
        "api_key": api_key,
        "count": count
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()

    image_links = [item["url"] for item in data]

    if image_links:
        save_folder = "images"
        download_images_from_urls(image_links, save_folder)
    else:
        print("Ссылки на фотографии не найдены.")

if __name__ == "__main__":
    fetch_nasa_images(count=10)
