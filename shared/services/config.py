from dotenv import load_dotenv
import os
import json
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
WEBHOOK_ENDPOINT = os.getenv("WEBHOOK_ENDPOINT", "")

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{WEBHOOK_ENDPOINT}'


DEFAULT_SETTINGS = {}
try:
    # Try to load settings from file
    with open("./settings.json") as file:
        DEFAULT_SETTINGS = json.load(file)
except:
    pass


class ConfigService:
    configs = DEFAULT_SETTINGS

    def __init__(self) -> None:
        if (os.getenv("MODE", "development") != "production"):
            try:
                # Try to load settings from file in non-production mode
                load_dotenv(".dev.env")
            except:
                pass

        self.configs['token'] = os.getenv("TOKEN", "")
        self.configs['url'] = os.getenv("PARSE_URL", "")

    # Get config by key
    def get(self, key: str) -> str:
        return self.configs.get(key, "")


configService = ConfigService()
