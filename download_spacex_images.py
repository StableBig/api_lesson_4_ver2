import os
import requests

def download_images_from_urls(image_urls, save_folder):
    os.makedirs(save_folder, exist_ok=True)

    for index, image_url in enumerate(image_urls):
        image_extension = image_url.split(".")[-1]
        image_name = f"spacex_image_{index + 1}.{image_extension}"
        save_path = os.path.join(save_folder, image_name)

        response = requests.get(image_url)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"Скачано изображение {image_name}")

def fetch_spacex_last_launch():
    launch_id = "5eb87d47ffd86e000604b38a"
    base_url = f"https://api.spacexdata.com/v4/launches/{launch_id}"
    response = requests.get(base_url)
    response.raise_for_status()
    launch_data = response.json()

    image_links = launch_data.get("links", {}).get("flickr", {}).get("original", [])

    if image_links:
        save_folder = "images"
        download_images_from_urls(image_links, save_folder)
    else:
        print("Ссылки на фотографии не найдены.")

if __name__ == "__main__":
    fetch_spacex_last_launch()
