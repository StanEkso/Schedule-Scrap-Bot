from datetime import datetime
import requests
import telebot
from telebot import types
import sys
import time
import string
from parsing import parsing
from stack import Stack
from config import API_TOKEN, LOG_CHANNEL_ID, LOGGING_CHAT_ID, MAIN_CHANNEL
message_stack = Stack(10)
BASE_URL = ''
global msgs
sended = 0
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat','sun']
call_days = {}
msgs = parsing()
reply_markup = types.InlineKeyboardMarkup()
buttonPrev = types.InlineKeyboardButton(text="◀", callback_data='prev')
buttonOK = types.InlineKeyboardButton(text="OK", callback_data="ok")
buttonNext = types.InlineKeyboardButton(text="▶", callback_data='next')
buttonMon = types.InlineKeyboardButton(text="ПН", callback_data="mon")
buttonTue = types.InlineKeyboardButton(text="ВТ", callback_data="tue")
buttonWed = types.InlineKeyboardButton(text="СР", callback_data="wed")
buttonThu = types.InlineKeyboardButton(text="ЧТ", callback_data="thu")
buttonFri = types.InlineKeyboardButton(text="ПТ", callback_data="fri")
buttonSat = types.InlineKeyboardButton(text="СБ", callback_data="sat")
reply_markup.add(buttonPrev, buttonOK, buttonNext)
reply_markup.row().add(buttonMon, buttonTue, buttonWed) \
    .row().add(buttonThu, buttonFri, buttonSat)
bot = telebot.TeleBot(API_TOKEN)

badwords = {
    "недоброе": "Ну, что же, бывает всякое. Даже такое.",
    "булить": "Кого булить? Себя забуль",
    "токсик": "Не надо так",
    "душнила": "Не стоит",
    "сосать": "Осуждаю...",
    "бот":"Я высшая форма жизни",
    "удачи":"Удачи! Да прибудет с тобой сила всемирного тяготения"
}

examples = set()

exampleFile = open('examples.txt', 'r', encoding="utf-8")
for line in exampleFile:
    line = line.lower()
    line1 = ""
    for x in line:
        if x.isalpha() or x.isnumeric() is True:
            line1 = line1 + str(x)
    line = line1
    examples.add(line)
exampleFile.close()


def sendLogs(data):
    bot.send_message(LOG_CHANNEL_ID, data)
    pass

def checkAdminInChannel(adminID):
    admins = bot.get_chat_administrators(MAIN_CHANNEL)
    for admin in admins:
        if admin.user.id == adminID:
            return True

    return False

@bot.channel_post_handler(func = lambda message: True)
def post_handler(post):
    print(post)

@bot.message_handler(commands=['post'])
def postInChannel(message):


    if not checkAdminInChannel(message.from_user.id):
        return bot.send_message(message.from_user.id, "Вы не являетесь администратором канала " + bot.get_chat(MAIN_CHANNEL).title)
    
    # return bot.send_message(message.from_user.id,"Функция не реализована :(")
    arguments = message.text.split(' ')
    arguments.pop(0)
    isReadable = arguments.pop(0)
    kboard = types.InlineKeyboardMarkup()
    templateAction = 'action_view_'+isReadable
    if isReadable != 'none':
        buttonView = types.InlineKeyboardButton(text="Прочитал", callback_data=templateAction)
        kboard.add(buttonView)
    else:
        kboard = None

    bot.send_message(chat_id=MAIN_CHANNEL,text=' '.join(arguments), reply_markup=kboard)


@bot.edited_message_handler(func=lambda message: message.chat.id == LOGGING_CHAT_ID)
def editHandler(message):
    date = message.date
    date+=10800
    date = datetime.utcfromtimestamp(date)
    date = date.strftime('%H:%M:%S')
    log = message.from_user.first_name + " (@" + message.from_user.username +") изменил сообщение\n"
    log+= "Оригинал был в " + date + ", изменено в " + datetime.utcfromtimestamp(message.edit_date+10800).strftime('%H:%M:%S') + "\n"
    message_stack.add(datetime.utcfromtimestamp(message.edit_date+10800).strftime('%H:%M:%S') + " " +message.from_user.first_name + " (@" + message.from_user.username +") (изм.): " + message.text)
    bot.send_message(LOG_CHANNEL_ID, log)

@bot.message_handler(commands=['расписание', 'schedule'])
def table(message):
    global msgs
    msgs = parsing()
    schedule = types.InlineKeyboardMarkup()
    show = types.InlineKeyboardButton(text="Просмотреть", callback_data='show')
    schedule.add(show)
    if message.chat.id == -1001580924097 or message.chat.type == 'private':
        bot.send_message(message.chat.id, "Просмотреть расписание?", reply_markup=schedule)
    try:
        bot.delete_message(message.chat.id, message_id=message.id)
    except:
        pass


@bot.message_handler(commands=['delit'])
def delete_msg(message):
    if message.from_user.id == 376185154:
        if message.reply_to_message != None:
            try:
                bot.delete_message(message.chat.id, message.reply_to_message.message_id)
                bot.delete_message(message.chat.id, message.id)
            except:
                pass



@bot.message_handler(content_types=['text'])
def start_command(message):
    try:
        input = message.text
    finally:
        pass
    
    date = message.date
    date+=10800
    date = datetime.utcfromtimestamp(date)
    date = date.strftime('%H:%M:%S')
    log = date + " " + message.from_user.first_name + " (@" + message.from_user.username +"): " + input
    print(log)
    if message.chat.id == LOGGING_CHAT_ID:
        result = message_stack.add(log)
        if (result["state"]):
            sendLogs(result["data"])

    words = list(set(input.translate(str.maketrans('','', string.punctuation)).lower().split()))
    for i in words:
        for example in examples:
            if str(i) == example:
                bot.send_message(message.chat.id, (example.capitalize() + "!"))
            # непозитивные ответы
        for example in badwords.keys():
            if str(i) == example:
                try:
                    bot.reply_to(message=message,text=badwords.get(str(i)))
                except:
                    pass

@bot.callback_query_handler(func=lambda call: 'action_view_' in call.data)
def callVote(call):
    # print(call)
    user_id = call.from_user.id
    user_first_name = call.from_user.first_name
    user_name = call.from_user.username
    user_info = {
        "id": user_id,
        "name": user_first_name,
        "username": user_name,
        "action": call.data.split('action_view_')[1]
    }
    print(user_info)
    response = requests.post('http://localhost:8080/views/append', json=user_info)
    print(response.json())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global msgs
    global sended
    global day
    day = call_days.get(call.message.id)
    schedule = types.InlineKeyboardMarkup()
    show = types.InlineKeyboardButton(text="Просмотреть", callback_data='show')
    schedule.add(show)
    if call.data == "show":
        # msgs = parsing()
        id = call.message.id
        if sended == 0:
            day = time.ctime(call.message.date)[:3].lower()
        else:
            day = call_days.get(call.message.id)
        call_days[id] = day
        for i in zip(days, msgs):
            if day == i[0]:
                msg = i[1]
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=msg,
                                  reply_markup=reply_markup)
            sended = 1
        except:
            day = time.ctime(call.message.date)[:3].lower()
            for i in zip(days, msgs):
                if day == i[0]:
                    msg = i[1]
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=msg,
                                  reply_markup=reply_markup)
            sended = 1

    elif call.data == "ok":
        try:
            sended = 0
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Расписание закрыто",
                                  reply_markup=schedule)
        except:
            pass
    elif call.data == "prev":
        try:
            if day == None:
                day = time.ctime(call.message.date)[:3].lower()
            else:
                day = days[days.index(day)-1]

            for i in zip(days, msgs):
                 if day == i[0]:
                     msg = i[1]
            call_days[call.message.id] = day
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=msg,
                                  reply_markup=reply_markup)
        except:
            pass


    elif call.data == "next":
        try:
            if days.index(day) != len(days) - 1:
                day = days[days.index(day) + 1]
            else:
                day = days[0]

            for i in zip(days, msgs):
                if day == i[0]:
                    msg = i[1]

            call_days[call.message.id] = day
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=msg, reply_markup=reply_markup)
        except:
            pass
    else:
        day = call_days.get(call.message.id)
        if day == call.data:
            pass
        else:
            day = call.data
            for i in zip(days, msgs):
                if day == i[0]:
                    msg = i[1]
            call_days[call.message.id] = day
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=msg,
                                  reply_markup=reply_markup)


bot.polling()
