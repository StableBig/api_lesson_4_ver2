from datetime import datetime
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def get_image_urls():
    api_key = os.getenv("EPIC_API_KEY")
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}")

    if response.status_code == 200:
        data = response.json()
        image_urls = [f"https://api.nasa.gov/EPIC/archive/natural/{get_date_from_iso(item['date'])}/png/{item['image']}.png?api_key={api_key}" for item in data]
        return image_urls
    else:
        print(f"Не удалось загрузить адрес изображения. Код статуса: {response.status_code}")
        return None

def get_date_from_iso(iso_date):
    # Преобразование даты
    date_object = datetime.fromisoformat(iso_date.replace("T", " ").split(".")[0])
    return date_object.strftime("%Y/%m/%d")

def download_images(image_urls):
    for url in image_urls:
        print("Загрузка изображений из:", url)
        response = requests.get(url)

        if response.status_code == 200:
            filename = os.path.basename(url.split('?')[0])
            with open(f'images/{filename}', 'wb') as f:
                f.write(response.content)
            print("Изображение загружено успешно")
        else:
            print(f"Не удалось загрузить изображение. Код статуса: {response.status_code}")

if __name__ == "__main__":
    image_urls = get_image_urls()

    if image_urls:
        print("List of image URLs:", image_urls)
        download_images(image_urls)
    else:
        print("No image URLs found.")
