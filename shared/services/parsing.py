import requests
from bs4 import BeautifulSoup
from ..types.exam import Exam
from ..types.lesson import Lesson
from ..decorators.invoke import InvokePerformance
from ..decorators.cache import Cache


class ParserService:

    @InvokePerformance
    @Cache(timeout=60000)
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

        return [self.mapTupleToLesson(i) for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday)]

    @staticmethod
    def convertLessonType(lessonType: str) -> str:
        if lessonType == "л":
            return "Лекция"
        elif lessonType == "п":
            return "Практика"
        else:
            return ""

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

    @staticmethod
    def mapTupleToLesson(lessonTuple: tuple) -> Lesson:
        time, remarks, subjectAndTeacher, lessonType, room, weekday = [
            ParserService.tagToText(item) for item in lessonTuple]

        # Using lower() method for getting day in lower case.
        # Used for getting day from dictionary.
        weekday = weekday.lower()

        lesson: Lesson = {
            "time": time,
            "meta": remarks,
            "subject": subjectAndTeacher,
            "type": ParserService.convertLessonType(lessonType),
            "room": room,
            "weekday": weekday
        }
        return lesson


parser: ParserService = ParserService()
