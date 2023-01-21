from dotenv import load_dotenv
from shared.constants.settings import DEFAULT_SETTINGS as BASIC_SETTINGS
from shared.logger.logger import logger
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
    logger.error("Can't load settings from file")
    with open("./settings.json", "w") as file:
        logger.info("Creating default settings file")
        json.dump(BASIC_SETTINGS, file, indent=4)

    DEFAULT_SETTINGS = BASIC_SETTINGS
    pass


class ConfigService:
    configs = DEFAULT_SETTINGS

    def __init__(self) -> None:
        if (os.getenv("MODE", "development") != "production"):
            try:
                load_dotenv(".dev.env")
            except:
                pass

        self.configs['token'] = os.getenv("TOKEN", "")
        self.configs["GROUP"] = os.getenv("GROUP", "2")
        self.configs["COURSE"] = os.getenv("COURSE", "2")
        self.configs["scheduleUrl"] = self.constructScheduleUrl(
            self.configs["COURSE"], self.configs["GROUP"])
        self.configs["examsUrl"] = self.constructUrl(self.configs["COURSE"])

    # Get config by key
    def get(self, key: str, default: any = "") -> str:
        return self.configs.get(key, default)

    @staticmethod
    def constructScheduleUrl(course: int | str, group: int | str) -> str:
        return f"https://mmf.bsu.by/ru/raspisanie-zanyatij/dnevnoe-otdelenie/{course}-kurs/{group}-gruppa/"

    @staticmethod
    def constructUrl(course: int | str) -> str:
        return f"https://mmf.bsu.by/ru/raspisanie-ekzamenov/dnevnoe-otdelenie/{course}-kurs/"


configService = ConfigService()
