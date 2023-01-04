import requests
from bs4 import BeautifulSoup
import requests
from shared.services.config import configService
from shared.types.lesson import Lesson

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
        pass

    def getPageText(self) -> str:
        return requests.get(self.url).text

    def parseFromPage(self) -> list[Lesson]:
        # Parsing content via BeautifulSoup.
        soup = BeautifulSoup(self.getPageText(), features="html.parser")

        # Replacing <br> tags with spaces.
        for a in soup.findAll('br'):
            a.replaceWith(" %s " % a.text)

        # Getting all needed tags.
        time = soup.find_all('td', {'class': 'time'})
        remarks = soup.find_all('td', {"class": "remarks"})
        subjectAndTeacher = soup.find_all('td', {"class": "subject-teachers"})
        lessonType = soup.find_all('td', {'class': 'lecture-practice'})
        room = soup.find_all('td', {'class': 'room'})
        weekday = soup.find_all('td', {'class': 'weekday'})

        lessons: list[Lesson] = []

        # Zip all lists and iterate over them.
        for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday):

            # Getting data from table
            currentTime = i[0].text
            currentRemarks = i[1].text
            currentSubjectAndTeacher = i[2].text
            currentLessonType = i[3].text
            currentRoom = i[4].text

            # Using lower() method for getting day in lower case.
            # Used for getting day from dictionary.
            currentWeekDay = i[5].text.lower()

            # Replacing short names of lesson types with full names.
            if currentLessonType == "л":
                currentLessonType = "Лекция"
            elif currentLessonType == "п":
                currentLessonType = "Практика"
            else:
                currentLessonType = ""
            lesson: Lesson = {
                "time": currentTime,
                "meta": currentRemarks,
                "subject": currentSubjectAndTeacher,
                "type": currentLessonType,
                "room": currentRoom,
                "weekday": currentWeekDay
            }
            lessons.append(lesson)

        return lessons


# Create a parser service instance.
parser: ParserService = ParserService()
