from typing import TypedDict


class Lesson(TypedDict):
    """
    The object representing a lesson.
    """

    time: str
    meta: str
    subject: str
    type: str
    room: str
    weekday: str


def lessonToString(lesson: Lesson) -> str:
    return f"{lesson['time']} <strong>{lesson['meta']}</strong> {lesson['subject']} {lesson['type']} {lesson['room']}"
