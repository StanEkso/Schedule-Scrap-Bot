from config import config as configService

messages: dict[dict[str]] = {
    "ru": {
        "showSchedule": "Просмотреть расписание",
        'mon': "Расписание группы на Понедельник: \n",
        'tue': "Расписание группы на Вторник: \n",
        'wed': "Расписание группы на Среду: \n",
        'thu': "Расписание группы на Четверг: \n",
        'fri': "Расписание группы на Пятницу: \n",
        'sat': "Расписание группы на Субботу: \n",
    }
}


class MessageService:
    def __init__(self) -> None:
        self.lang = configService.get("lang") or "ru"

    def get(self, key: str, default: str = "") -> str:
        return messages.get(self.lang).get(key, default)


messageService = MessageService()
print(messageService.get("mon"))
