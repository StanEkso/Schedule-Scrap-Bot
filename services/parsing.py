import requests
import string
from bs4 import BeautifulSoup
import requests
from config import config as configService
from message import messageService


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
        sun = 'Какие пары в Воскресенье? Поспи хоть, дружище...'
        time = soup.find_all('td', {'class': 'time'})
        remarks = soup.find_all('td', {"class": "remarks"})
        subjectAndTeacher = soup.find_all('td', {"class": "subject-teachers"})
        lessonType = soup.find_all('td', {'class': 'lecture-practice'})
        room = soup.find_all('td', {'class': 'room'})
        weekday = soup.find_all('td', {'class': 'weekday'})
        days = {
            "понедельник": messageService.get("mon"),
            "вторник": messageService.get("tue"),
            "среда": messageService.get("wed"),
            "четверг": messageService.get("thu"),
            "пятница": messageService.get("fri"),
            "суббота": messageService.get("sat"),
        }
        for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday):
            type = i[3].text
            currentWeekDay = i[5].text.lower()
            if type == "л":
                type = "Лекция"
            elif type == "п":
                type = "Практика"
            else:
                type = ""
            if not days.get(currentWeekDay):
                days[currentWeekDay] = ""
            days[currentWeekDay] += i[0].text + " " + i[1].text + " " + \
                i[2].text + " " + type + " " + i[4].text + '\n'

        return list(days.values())


parser: ParserService = ParserService()
