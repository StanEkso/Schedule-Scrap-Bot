# Write a lesson class inheriting from TypedDict and use it in the ParserService class:

from typing import TypedDict


class Lesson(TypedDict):
    time: str
    meta: str
    subject: str
    type: str
    room: str
    weekday: str

# Create a function taking a Lesson and returning a string
# Example:
# 8:15 1-18 Математика Лекция Ауд. 1


def lessonToString(lesson: Lesson) -> str:
    return f"{lesson['time']} <strong>{lesson['meta']}</strong> {lesson['subject']} {lesson['type']} {lesson['room']}"
