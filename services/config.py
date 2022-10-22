from dotenv import load_dotenv
import os


class ConfigService:
    configs = {}

    def __init__(self) -> None:
        if (os.getenv("dev", "false") == "true"):
            load_dotenv(".dev.env")
        print(os.environ)
        self.configs['token'] = os.getenv("TOKEN", "")
        self.configs['url'] = os.getenv("PARSE_URL", "")
        print(self.configs)

    def get(self, key: str) -> str:
        return self.configs.get(key, "")


configService = ConfigService()
