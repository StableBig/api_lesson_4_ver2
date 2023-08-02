# Бот для публикации изображений космоса

Бот для публикации изображений космоса - это проект на Python, который загружает и публикует изображения на космическую тематику от NASA и SpaceX в Telegram-канал. Бот загружает изображения NASA Earth Polychromatic Imaging Camera (EPIC), NASA Astronomy Picture of the Day (APOD) и запусков SpaceX.

## Предварительные требования

Прежде чем начать, убедитесь, что у вас установлено следующее:

* Python 3.7 или выше
* pip - установщик пакетов Python
* Virtualenv - Инструмент для создания изолированных сред Python
* Git - Система контроля версий

Вам также потребуется:

* Подключение к интернету
* Ключ API NASA
* Токен бота Telegram
* Канал в Telegram

## Установка

### 1. Клонируйте репозиторий

Начните с клонирования репозитория на ваш компьютер.

```bash
git clone https://github.com/StableBig/api_lesson_4_ver2.git
cd api_lesson_4_ver2
```

_Обратите внимание, что команда  `cd` (change directory) используется в Unix/Linux системах. Если вы используете Windows, вы можете использовать эту же команду в PowerShell или использовать команду `chdir` в командной строке (cmd)._

### 2. Настройка виртуального окружения

Далее создайте новое виртуальное окружение и активируйте его.

```bash
python3 -m venv venv
source venv/bin/activate  # для Unix систем
.\venv\Scripts\activate  # для Windows
```

### 3. Установите зависимости
С активированным виртуальным окружением установите зависимости проекта:

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Вам нужно настроить некоторые переменные окружения перед запуском бота. Создайте файл .env и добавьте переменные с вашим ключом API NASA, токеном бота Telegram и ID канала Telegram:

```
NASA_API_KEY=ваш_nasa_api_key
TELEGRAM_BOT_TOKEN=ваш_telegram_bot_token
TELEGRAM_CHANNEL_ID=@ваш_telegram_channel_id
```

ID канала Telegram начинается с **@**!

**Как получить ключ API NASA:**

Чтобы получить ключ API NASA, перейдите на https://api.nasa.gov/ и сгенерируйте свой собственный ключ API.

**Создание бота Telegram и получение токена:**

1. Откройте Telegram и найдите `BotFather`.
2. Начните чат и следуйте инструкциям для создания нового бота.
3. Как только бот будет создан, вы получите токен. Этот токен представляет вашего бота и используется для доступа к HTTP API.

**Создание канала Telegram и получение ID канала:**

1. В Telegram нажмите на меню и выберите 'Новый канал'.
2. Следуйте инструкциям для создания нового канала.
3. Как только канал будет создан, перейдите в 'Настройки канала' -> 'Информация о канале'.
4. Здесь вы можете скопировать ID канала (это будет часть после https://t.me/).

### 5. Запуск скриптов

Проект содержит несколько скриптов, которые вам нужно будет запустить:

**download_apod.py:**

Этот скрипт получает изображения APOD от NASA с помощью API и сохраняет его в локальной директории `images/`.

```bash
python download_apod.py --date YYYY-MM-DD
```

Вы можете указать дату изображения (YYYY - год, MM - месяц, DD - день). Если не указана, будет загружено изображение с датой '2023-08-01' по умолчанию.

**download_epic.py:**

Этот скрипт получает изображения EPIC от NASA с помощью API и сохраняет их в локальной директории `images/`.

```bash
python download_epic.py --count 10
```

_Вы можете указать количество фотографий (вместо 10 - любое число от одного). Если не указано, по умолчанию загружается 10 фотографий._

**download_spacex_images.py:**

Этот скрипт получает фотографии запусков SpaceX и сохраняет их в локальной директории `images/`.

```bash
python download_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```

_Вы должны указать ID запуска (5eb87d47ffd86e000604b38a или другой). Если не указан, по умолчанию загружаются фотографии запуска с ID 5eb87d47ffd86e000604b38a._

**telegram_bot.py:**

Скрипт автоматически отправляет изображения в ваш Telegram-канал. Интервал между отправкой изображений по умолчанию составляет 4 часа, но его можно настроить.

```bash
python telegram_bot.py --dir images --hours 4 --image epic_1.png
```

_Команда загружает изображения из папки `images/`, устанавливает интервал автоматической публикации изображений в часах и публикует указанную фотографию. Измените значения в соответствии с вашими потребностями._

## Завершение работы

Чтобы остановить бота, просто остановите скрипт, нажав Ctrl + C в терминале.

## Работа бота без остановки

Если вы хотите, чтобы ваш бот работал постоянно, скрипт должен быть постоянно запущен все это время.

## Дополнительная информация

Обратите внимание, что API NASA может быть недоступен. Если это так, скрипты загрузки изображений (download_apod.py and download_epic.py) будут возвращать ошибку и не будут работать. Если это случилось, попробуйте воспользоваться скриптами позднее.

## Цель проекта

Код написан в образовательных целях.

---

# Space Images Bot

Space Images Bot is a Python project that fetches and posts space-themed images from NASA and SpaceX to a Telegram channel. The bot is designed to automatically fetch images from NASA's Earth Polychromatic Imaging Camera (EPIC), Astronomy Picture of the Day (APOD), and the latest SpaceX launches.

## Prerequisites

Before getting started you should have the following installed and running:

Python 3.7 or higher
pip - Python's package installer
Virtualenv - A tool to create isolated Python environments
Git - Version Control System

You'll also need:

An internet connection
A NASA API key
A Telegram bot token
A Telegram channel

## Setup

### 1. Clone the repository

Start by cloning the repository to your local machine.

```bash
git clone https://github.com/StableBig/api_lesson_4_ver2.git
cd api_lesson_4_ver2
```

_Please note that the `cd` (change directory) command is used in Unix/Linux systems. If you are using Windows, you can use the same command in PowerShell or use the `chdir` command in Command Prompt (cmd)_.

### 2. Setup Virtual Environment

Next, set up a new virtual environment and activate it.

```bash
python3 -m venv venv
source venv/bin/activate  # for Unix systems
.\venv\Scripts\activate  # for Windows
```

### 3. Install dependencies

With your virtual environment activated, install the project dependencies with:

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

You need to set up some environment variables before running the bot. Create a .env file and add the variables with your NASA API key, Telegram bot token, and Telegram channel ID:

```
NASA_API_KEY=your_nasa_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHANNEL_ID=@your_telegram_channel_id
```

Telegram Channel ID starts with **@**!

**Getting a NASA API Key:**

To get a NASA API key, visit https://api.nasa.gov/ and generate your own API key.

**Creating a Telegram bot and getting the token:**

1. Open Telegram and search for `BotFather`.
2. Start chat and follow the instructions to create a new bot.
3. Once the bot is created, you will receive a token. This token represents your bot and is used for HTTP API access.

**Creating a Telegram channel and getting the channel ID:**

1. In Telegram, click on the hamburger menu and select 'New Channel'.
2. Follow the prompts to create a new channel.
3. Once the channel is created, go to 'Channel Settings' -> 'Channel Info'.
4. Here you can copy the channel ID (this will be the part after https://t.me/ in the Link section).

### 5. Running the scripts

The project contains several scripts that you will need to run:

**download_apod.py:**

This script fetches the APOD image from NASA's API and stores it in the local `images/` directory.

```bash
python download_apod.py --date YYYY-MM-DD
```

_You can specify the date of the image (YYYY - year, MM - month, DD - day). If not specified, the image of the day '2023-08-01' will be downloaded by default._

**download_epic.py:**

This script fetches the latest EPIC images from NASA's API and stores them in the local `images/` directory.

```bash
python download_epic.py --count 10
```

_You can specify the number of images to be downloaded (instead of 10 - any number from one). If not specified, 10 images will be downloaded by default._

**download_spacex_images.py:**

This script fetches the latest images from SpaceX launches and stores them in the local `images/` directory.

```bash
python3 download_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```

You should specify the launch ID (5eb87d47ffd86e000604b38a or another). If not specified, the images from the launch with ID '5eb87d47ffd86e000604b38a' are downloaded by default.

**telegram_bot.py:**

This is the main script which manages the Telegram bot. It fetches a random image from the local `images/` directory and posts it to the specified Telegram channel at specified intervals.

```bash
python telegram_bot.py
```

By default, the bot will post an image every 4 hours. You can change this by modifying the `--hours` argument when running the telegram_bot.py script:

```bash
python telegram_bot.py --hours 6  # Posts an image every 6 hours
```

You can also specify the directory with images for posting:

```bash
python telegram_bot.py --dir images  # Fetches images from 'images' directory
```

If you want to post a specific image, use `--image` argument:

```bash
python telegram_bot.py --image epic_1.png  # Posts 'epic_1.png' image

```

## Stopping the bot

To stop the bot, interrupt the script execution by pressing Ctrl + C in the terminal.

## Keep the bot running

If you want the bot to run indefinitely, you will need to keep the script running.

## Additional Information

Please note that the NASA API might be unavailable at times. If this is the case, the image downloading scripts (download_apod.py and download_epic.py) will return an error and won't function. If you encounter this, try running the scripts later.

## Project Goal

The code is written for educational purposes.
