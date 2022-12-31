import requests
from bs4 import BeautifulSoup
import requests
from shared.services.config import configService
from telegram.services.message import messageService


def formStringFromArray(arr: list) -> str:
    return " ".join(arr)


class ParserService:
    url: str

    def __init__(self) -> None:
        self.url = configService.get("url")
        pass

    def getPageText(self) -> str:
        return requests.get(self.url).text

    def parseFromPage(self):
        soup = BeautifulSoup(self.getPageText(), features="html.parser")
        for a in soup.findAll('br'):
            a.replaceWith(" %s " % a.text)
        time = soup.find_all('td', {'class': 'time'})
        remarks = soup.find_all('td', {"class": "remarks"})
        subjectAndTeacher = soup.find_all('td', {"class": "subject-teachers"})
        lessonType = soup.find_all('td', {'class': 'lecture-practice'})
        room = soup.find_all('td', {'class': 'room'})
        weekday = soup.find_all('td', {'class': 'weekday'})

        lessons = []
        for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday):

            type = i[3].text
            currentWeekDay = i[5].text.lower()
            if type == "л":
                type = "Лекция"
            elif type == "п":
                type = "Практика"
            else:
                type = ""

            lesson = {
                "time": i[0].text,
                "meta": i[1].text,
                "subject": i[2].text,
                "type": type,
                "room": i[4].text,
                "weekday": currentWeekDay
            }
            lessons.append(lesson)

        return lessons


parser: ParserService = ParserService()
