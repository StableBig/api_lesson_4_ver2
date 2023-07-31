import os
from datetime import datetime
import requests
from urllib.parse import urlparse


def get_file_extension_from_url(url):
    parsed_url = urlparse(url)
    file_extension = os.path.splitext(parsed_url.path)[1]
    return file_extension


def save_image(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)


def download_image(image_url, save_folder, filename_prefix, timestamp, index):
    image_extension = get_file_extension_from_url(image_url)
    image_name = f"{filename_prefix}_{timestamp}_{index + 1}{image_extension}"
    save_path = os.path.join(save_folder, image_name)

    save_image(image_url, save_path)


def download_images_from_urls(image_urls, save_folder, filename_prefix):
    os.makedirs(save_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    for index, image_url in enumerate(image_urls):
        download_image(image_url, save_folder, filename_prefix, timestamp, index)
