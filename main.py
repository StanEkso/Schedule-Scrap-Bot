import telebot
from telebot import types
import sys
import time
import random
import raspisanie

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat','sun']
call_days = {}
msgs = []
msgs.append(raspisanie.mon)
msgs.append(raspisanie.tue)
msgs.append(raspisanie.wed)
msgs.append(raspisanie.thu)
msgs.append(raspisanie.fri)
msgs.append(raspisanie.sat)
msgs.append(raspisanie.sun)

sended = 0

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
bot = telebot.TeleBot('1955658538:AAGDDsLSNqDuClkSvPtE3AiDEAm0jdxOxMo')

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


@bot.message_handler(commands=['расписание', 'schedule'])
def table(message):
    sended = 0
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



@bot.message_handler(commands=['mainteancemode'])
def mainteancemode(message):
    if message.chat.type == "private":
        global mt_owner
        bot.send_message(message.from_user.id, 'MAINTEANCE MODE ENABLED!')
        mt_owner = {
            "user_id": message.from_user.id,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "username": message.from_user.username,
            "timeofstart": time.ctime(message.date)
        }
        bot.register_next_step_handler(message, mainteance)


@bot.message_handler(content_types=['text'])
def start_command(message):
    print(message.chat.id)
    global mtcounter
    mtcounter = 0
    sended = 0
    try:
        input = message.text
    finally:
        pass
    print(message.from_user.first_name + " writes: " + input)
    inputS = input.split()
    if inputS[0] == "/asbot":
        bot.send_message(-1001519670451, message.text[message.text.find(" "):])
    for i in inputS:
        word = str(i)
        word1 = ""
        for x in word:
            if x.isalpha() or x.isnumeric() is True:
                word1 = word1 + str(x)
        word = word1.lower()
        if sended < 2:
            for example in examples:
                if word == example:
                    bot.send_message(message.chat.id, (example.capitalize() + "!"))
                    sended += 1
            # непозитивные ответы
            for example in badwords.keys():
                if word == example:
                    try:
                        bot.reply_to(message=message,text=badwords.get(word))
                        sended += 1
                    except:
                        pass


@bot.message_handler(content_types=['text'])
def mainteance(message):
    global mtcounter
    if message.text == '/mainteancemode':
        bot.register_next_step_handler(message, start_command)
        bot.send_message(message.from_user.id, "MAINTEANCE MODE DISABLED")
    elif message.from_user.id == mt_owner.get("user_id") and message.text == "/stats":
        bot.send_message(message.from_user.id, ("Счетчик сообщений до предупреждения: " + str(mtcounter)))
        bot.register_next_step_handler(message, mainteance)
    elif message.text == "/mainteanceinfo":
        time = mt_owner.get("timeofstart").split()
        mt_time = time[3]
        bot.send_message(message.chat.id, ("MAINTEANCE INFO:\nSTARTED BY: " +
                                           str(mt_owner.get("first_name")) + " " + str(mt_owner.get("last_name")) +
                                           "\nSTART TIME: " + str(mt_time)))
        bot.register_next_step_handler(message, mainteance)
    else:
        mtcounter += 1
        if mtcounter == 10:
            bot.send_message(message.chat.id,
                             "BOT IS IN MAINTEANCE MODE NOW.\nType /mainteanceinfo for more information")
            mtcounter = 0
        bot.register_next_step_handler(message, mainteance)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global sended
    global day
    day = call_days.get(call.message.id)
    schedule = types.InlineKeyboardMarkup()
    show = types.InlineKeyboardButton(text="Просмотреть", callback_data='show')
    schedule.add(show)
    if call.data == "show":
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
            if day == "mon":
                day = "sat"
            elif day == "tue":
                day = "mon"
            elif day == "wed":
                day = 'tue'
            elif day == "thu":
                day = 'wed'
            elif day == "fri":
                day = 'thu'
            elif day == "sat":
                day = 'fri'
            elif day == "sun":
                day = 'sat'
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
            if day == None:
                day = time.ctime(call.message.date)[:3].lower()
            if day == "mon":
                day = 'tue'
            elif day == "tue":
                day = 'wed'
            elif day == "wed":
                day = 'thu'
            elif day == "thu":
                day = 'fri'
            elif day == "fri":
                day = 'sat'
            elif day == "sat":
                day = 'mon'
            elif day == 'sun':
                day = 'mon'

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
