from typing import TypedDict

MessageLocalization = TypedDict('MessageLocalization', {
    'show': str,
    'schedule_closed': str,
    'mon': str,
    'tue': str,
    'wed': str,
    'thu': str,
    'fri': str,
    'sat': str,
    'day_is_chosen': str,
    "current_week_num": str
})

messages: dict[str, MessageLocalization] = {
    "ru": {
        "show": "Просмотреть расписание",
        "schedule_closed": "Расписание закрыто",
        'mon': "Расписание группы на Понедельник: \n",
        'tue': "Расписание группы на Вторник: \n",
        'wed': "Расписание группы на Среду: \n",
        'thu': "Расписание группы на Четверг: \n",
        'fri': "Расписание группы на Пятницу: \n",
        'sat': "Расписание группы на Субботу: \n",
        "current_week_num": "Текущий номер недели: ",
        'day_is_chosen': 'Этот день уже выбран',
    },
    "en": {
        "show": "Show schedule",
        "schedule_closed": "Schedule is closed",
        'mon': "Group schedule on Monday: \n",
        'tue': "Group schedule on Tuesday: \n",
        'wed': "Group schedule on Wednesday: \n",
        'thu': "Group schedule on Thursday: \n",
        'fri': "Group schedule on Friday: \n",
        'sat': "Group schedule on Saturday: \n",
        "current_week_num": "Current week number: ",
        'day_is_chosen': 'This day is already chosen',
    }
}
