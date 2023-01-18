from dotenv import load_dotenv
from shared.constants.settings import DEFAULT_SETTINGS as BASIC_SETTINGS
import os
import json
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
WEBHOOK_ENDPOINT = os.getenv("WEBHOOK_ENDPOINT", "")

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{WEBHOOK_ENDPOINT}'


DEFAULT_SETTINGS = {}
if os.path.exists("./settings.json"):
    with open("./settings.json") as file:
        DEFAULT_SETTINGS = json.load(file)
else:
    print("[ERROR] Can't load settings from file")
    with open("./settings.json", "w") as file:
        print("[INFO] Creating default settings file")
        json.dump(BASIC_SETTINGS, file, indent=4)

    DEFAULT_SETTINGS = BASIC_SETTINGS
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
        self.configs["GROUP"] = os.getenv("GROUP", "2")

    # Get config by key
    def get(self, key: str, default: any = "") -> str:
        return self.configs.get(key, default)


configService = ConfigService()
