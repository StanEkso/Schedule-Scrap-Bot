import requests
import string
from bs4 import BeautifulSoup


def parsing():
    msgs = []
    mon = "Расписание 02 группы на Понедельник: \n"
    tue = "Расписание 02 группы на Вторник\n"
    wed = "Расписание 02 группы на Среду\n"
    thu = "Расписание 02 группы на Четверг\n"
    fri = "Расписание 02 группы на Пятницу\n"
    sat = "Расписание 02 группы на Субботу\n"
    sun = 'Какие пары в Воскресенье? Поспи хоть, дружище...'


    url = "https://mmf.bsu.by/ru/raspisanie-zanyatij/dnevnoe-otdelenie/1-kurs/2-gruppa/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    for a in soup.findAll('br'):
        a.replaceWith(" %s " %a.text)

    time = soup.find_all('td', {'class': 'time'})
    remarks = soup.find_all('td', {"class": "remarks"})
    subjectteachers = soup.find_all('td', {"class": "subject-teachers"})
    lecturepractice = soup.find_all('td', {'class': 'lecture-practice'})
    room = soup.find_all('td', {'class':'room'})
    weekday = soup.find_all('td', {'class':'weekday'})
    for i in zip(time,remarks,subjectteachers,lecturepractice,room, weekday):
        type = i[3].text
        if type == "л": type = "Лекция"
        elif type == "п":   type = "Практика"
        else:   type =""
        if i[5].text.lower() == "понедельник":
            mon += i[0].text + " " + i[1].text + " " +i[2].text + " " + type + " " + i[4].text + '\n'
        elif i[5].text.lower() == "вторник":
            tue += i[0].text + " " + i[1].text + " " +i[2].text + " " + type + " " + i[4].text + '\n'
        elif i[5].text.lower() == "среда":
            wed += i[0].text + " " + i[1].text + " " + i[2].text + " " + type + " " + i[4].text + '\n'
        elif i[5].text.lower() == "четверг":
            thu += i[0].text + " " + i[1].text + " " +i[2].text + " " + type + " " + i[4].text + '\n'
        elif i[5].text.lower() == "пятница":
            fri += i[0].text + " " + i[1].text + " " + i[2].text + " " + type + " " + i[4].text + '\n'
        elif i[5].text.lower() == "суббота":
            sat += i[0].text + " " + i[1].text + " " + i[2].text + " " + type + " " + i[4].text + '\n'

    mon = mon.replace("  ", " ")
    tue = tue.replace("  ", " ")
    wed = wed.replace("  ", " ")
    thu = thu.replace("  ", " ")
    fri = fri.replace("  ", " ")
    sat = sat.replace("  ", " ")
    msgs = [mon, tue, wed,thu,fri,sat,sun]
    return msgs