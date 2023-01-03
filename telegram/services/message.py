from shared.services.config import configService

messages: dict[dict[str]] = {
    "ru": {
        "show": "Просмотреть расписание",
        "closed": "Расписание закрыто",
        'mon': "Расписание группы на Понедельник: \n",
        'tue': "Расписание группы на Вторник: \n",
        'wed': "Расписание группы на Среду: \n",
        'thu': "Расписание группы на Четверг: \n",
        'fri': "Расписание группы на Пятницу: \n",
        'sat': "Расписание группы на Субботу: \n",
    }
}

# Service for basic message on languages.
# Currently only Russian is supported.


class MessageService:

    # Initialization of service with configs.
    def __init__(self) -> None:
        self.lang = configService.get("lang") or "ru"

    # Method for getting message by key or default value.
    def get(self, key: str, default: str = "") -> str:
        try:
            return messages[self.lang][key]
        except:
            return default


messageService = MessageService()
