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
    image_name = f"{filename_prefix}_{timestamp}_{index}{image_extension}"
    save_path = os.path.join(save_folder, image_name)

    save_image(image_url, save_path)


def create_directory_if_not_exists(directory):
    os.makedirs(directory, exist_ok=True)


def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def download_images_from_urls(image_urls, save_folder, filename_prefix):
    create_directory_if_not_exists(save_folder)
    timestamp = get_current_timestamp()

    for index, image_url in enumerate(image_urls, start=1):
        download_image(image_url, save_folder, filename_prefix, timestamp, index)
