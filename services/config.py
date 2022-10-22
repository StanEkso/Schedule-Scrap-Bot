from dotenv import load_dotenv
import os
import json

DEFAULT_SETTINGS = {}
try:
    with open("./settings.json") as file:
        DEFAULT_SETTINGS = json.load(file)
except:
    pass


class ConfigService:
    configs = DEFAULT_SETTINGS

    def __init__(self) -> None:
        if (os.getenv("dev", "false") == "true"):
            load_dotenv(".dev.env")
        self.configs['token'] = os.getenv("TOKEN", "")
        self.configs['url'] = os.getenv("PARSE_URL", "")

    def get(self, key: str) -> str:
        return self.configs.get(key, "")


configService = ConfigService()
