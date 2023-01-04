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
        'day_is_chosen': 'Этот день уже выбран',
    },
    "en": {
        "show": "Show schedule",
        "closed": "Schedule is closed",
        'mon': "Group schedule on Monday: \n",
        'tue': "Group schedule on Tuesday: \n",
        'wed': "Group schedule on Wednesday: \n",
        'thu': "Group schedule on Thursday: \n",
        'fri': "Group schedule on Friday: \n",
        'sat': "Group schedule on Saturday: \n",
        'day_is_chosen': 'This day is already chosen',
    }
}

# Service for basic message on languages.


class MessageService:

    # Initialization of service with configs.
    def __init__(self) -> None:
        self.lang = configService.get("CURRENT_LANGUAGE") or "ru"

    # Method for getting message by key or default value.
    def get(self, key: str, default: str = "") -> str:
        try:
            return messages[self.lang][key]
        except:
            return default


messageService = MessageService()
