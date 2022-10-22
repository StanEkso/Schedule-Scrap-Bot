from dotenv import load_dotenv
import os


class ConfigService:
    configs = {}

    def __init__(self) -> None:
        if (os.getenv("dev", "false") == "true"):
            load_dotenv(".dev.env")
        self.token = os.getenv("token", "")
        self.configs['token'] = os.getenv("token", "")
        self.configs['url'] = os.getenv("PARSE_URL", "")
        print(self.configs)

    def get(self, key: str) -> str:
        return self.configs.get(key, "")


config = ConfigService()
