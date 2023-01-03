import requests
import string
from bs4 import BeautifulSoup
import requests
from shared.services.config import configService
from telegram.services.message import messageService

# Service for parsing schedule from site.


class ParserService:
    url: str

    # Initialization of service with configs.
    def __init__(self) -> None:
        self.url = configService.get("url")
        pass

    # Method for get page text.
    def getPageText(self) -> str:
        try:
            return requests.get(self.url).text
        except:
            return ""

    def parseFromPage(self):
        # Parsing content via BeautifulSoup.
        soup = BeautifulSoup(self.getPageText(), features="html.parser")

        # Replacing <br> tags with spaces.
        for a in soup.findAll('br'):
            a.replaceWith(" %s " % a.text)
        sun = 'Какие пары в Воскресенье? Поспи хоть, дружище...'

        # Getting all needed tags.
        time = soup.find_all('td', {'class': 'time'})
        remarks = soup.find_all('td', {"class": "remarks"})
        subjectAndTeacher = soup.find_all('td', {"class": "subject-teachers"})
        lessonType = soup.find_all('td', {'class': 'lecture-practice'})
        room = soup.find_all('td', {'class': 'room'})
        weekday = soup.find_all('td', {'class': 'weekday'})

        # Creating dictionary for days with default messages.
        days = {
            "понедельник": messageService.get("mon"),
            "вторник": messageService.get("tue"),
            "среда": messageService.get("wed"),
            "четверг": messageService.get("thu"),
            "пятница": messageService.get("fri"),
            "суббота": messageService.get("sat"),
        }

        # Zip all lists and iterate over them.
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
            if currentLessonType == "л":
                currentLessonType = "Лекция"
            elif currentLessonType == "п":
                currentLessonType = "Практика"
            else:
                currentLessonType = ""

            if not days.get(currentWeekDay):
                days[currentWeekDay] = ""

            resultString = " ".join([currentTime, currentRemarks,
                                     currentSubjectAndTeacher, currentLessonType, currentRoom])
            # Replace "  " with " " in result string.
            resultString = resultString.replace("  ", " ")
            days[currentWeekDay] += resultString + "\n"

        return list(days.values())


# Singleton instance of ParserService.
parser: ParserService = ParserService()
