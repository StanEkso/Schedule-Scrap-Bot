import os

USE_MODE = os.getenv("USE", 'POLLING').upper()
FIRST_DAY = os.getenv("FIRST_DAY", "29.08.2022")

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
WEBHOOK_ENDPOINT = os.getenv("WEBHOOK_ENDPOINT", "")

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{WEBHOOK_ENDPOINT}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv("PORT", 8000)
