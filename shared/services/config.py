from dotenv import load_dotenv
import os
import json
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
WEBHOOK_ENDPOINT = os.getenv("WEBHOOK_ENDPOINT", "")


DEFAULT_SETTINGS = {
    "WEBAPP_HOST": '0.0.0.0',
    "WEBAPP_PORT": os.getenv("PORT", 8000)
}
try:
    with open("./settings.json") as file:
        DEFAULT_SETTINGS = json.load(file)
except:
    pass


class ConfigService:
    configs = DEFAULT_SETTINGS

    def __init__(self) -> None:
        if (os.getenv("MODE", "development") != "production"):
            load_dotenv(".dev.env")
        self.configs['token'] = os.getenv("TOKEN", "")
        self.configs['url'] = os.getenv("PARSE_URL", "")

    def get(self, key: str) -> str:
        return self.configs.get(key, "")


configService = ConfigService()
