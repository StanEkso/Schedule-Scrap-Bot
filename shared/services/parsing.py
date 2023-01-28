import requests
from bs4 import BeautifulSoup
from ..types.exam import Exam
from ..types.lesson import Lesson
from ..decorators.invoke import InvokePerformance


class ParserService:

    def __init__(self) -> None:
        pass

    @InvokePerformance
    def parseFromPage(self, url: str) -> list[Lesson]:
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")

        for a in soup.findAll('br'):
            a.replaceWith(" %s " % a.text)

        time = soup.find_all('td', {'class': 'time'})
        remarks = soup.find_all('td', {"class": "remarks"})
        subjectAndTeacher = soup.find_all('td', {"class": "subject-teachers"})
        lessonType = soup.find_all('td', {'class': 'lecture-practice'})
        room = soup.find_all('td', {'class': 'room'})
        weekday = soup.find_all('td', {'class': 'weekday'})

        lessons: list[Lesson] = []

        for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday):

            currentTime = i[0].text
            currentRemarks = i[1].text
            currentSubjectAndTeacher = i[2].text
            currentLessonType = i[3].text
            currentRoom = i[4].text

            # Using lower() method for getting day in lower case.
            # Used for getting day from dictionary.
            currentWeekDay = i[5].text.lower()

            lesson: Lesson = {
                "time": currentTime,
                "meta": currentRemarks,
                "subject": currentSubjectAndTeacher,
                "type": self.convertLessonType(currentLessonType),
                "room": currentRoom,
                "weekday": currentWeekDay
            }
            lessons.append(lesson)

        return lessons

    @staticmethod
    def convertLessonType(lessonType: str) -> str:
        if lessonType == "л":
            return "Лекция"
        elif lessonType == "п":
            return "Практика"
        else:
            return ""

    def __str__(self) -> str:
        return f"ParserService(url={self.url})"

    def __repr__(self) -> str:
        return self.__str__()

    @InvokePerformance
    def parseExams(self, url: str) -> list[Exam]:
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")

        TABLE = soup.find("table")
        ROWS = TABLE.find_all("tr")
        exams: list[Exam] = []
        CURRENT_GROUP = ""
        for ROW in ROWS:
            CELLS = ROW.find_all("td")
            if (len(CELLS) == 1):
                CURRENT_GROUP = self.tagToText(CELLS[0])
                continue
            else:
                TEXTS = [self.tagToText(CELL) for CELL in CELLS]
                exams.append({
                    "group": CURRENT_GROUP,
                    "subject": TEXTS[0],
                    "teacher": TEXTS[1],
                    "examDate": TEXTS[2],
                    "examTime": TEXTS[3],
                    "examRoom": TEXTS[4],
                    "consultationDate": TEXTS[5],
                    "consultationTime": TEXTS[6],
                    "consultationRoom": TEXTS[7],
                })
        return exams

    @staticmethod
    def tagToText(tag) -> str:
        return tag.text.replace("\n", "")


parser: ParserService = ParserService()
