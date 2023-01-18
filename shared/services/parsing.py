import requests
from bs4 import BeautifulSoup
import requests

from ..types.exam import Exam
from ..services.config import configService
from ..types.lesson import Lesson
from ..decorators.invoke import InvokeLog, InvokePerformance

# Parser service for parsing schedule from site and return it as array of lessons
# Lesson is a dict with keys: time, meta, subject, type, room, weekday
# Example:
# {
#  "time": "8:30-10:00",
#  "meta": "1-18",
#  "subject": "Математика",
#  "type": "Лекция",
#  "room": "Ауд. 1",
#  "weekday": "понедельник"
# }


class ParserService:
    url: str

    def __init__(self) -> None:
        self.url = configService.get("url")
        print(f"[INIT] Parser url: {self.url}")
        pass

    def getPageText(self) -> str:
        return requests.get(self.url).text

    @InvokePerformance
    def parseFromPage(self) -> list[Lesson]:
        soup = BeautifulSoup(self.getPageText(), features="html.parser")

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

            # Replacing short names of lesson types with full names.
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
                CURRENT_GROUP = CELLS[0].text.replace("\n", "")
                continue
            else:
                exams.append({
                    "group": CURRENT_GROUP,
                    "subject": CELLS[0].text.replace("\n", ""),
                    "teacher": CELLS[1].text.replace("\n", ""),
                    "examDate": CELLS[2].text.replace("\n", ""),
                    "examTime": CELLS[3].text.replace("\n", ""),
                    "examRoom": CELLS[4].text.replace("\n", ""),
                    "consultationDate": CELLS[5].text.replace("\n", ""),
                    "consultationTime": CELLS[6].text.replace("\n", ""),
                    "consultationRoom": CELLS[7].text.replace("\n", ""),
                })
        return exams


parser: ParserService = ParserService()
