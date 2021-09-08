import telebot
from telebot import types
import sys
import time
import random
import raspisanie

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
call_days = {}
msgs = []
msgs.append(raspisanie.mon)
msgs.append(raspisanie.tue)
msgs.append(raspisanie.wed)
msgs.append(raspisanie.thu)
msgs.append(raspisanie.fri)
msgs.append(raspisanie.sat)

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


@bot.message_handler(commands=['addnewword'])
def new_word(message):
    if message.from_user.id == 376185154:
        word = message.text[message.text.find(" ") + 1:]
        if not (word.capitalize()) in examples:
            exampleFile = open('examples.txt', 'a', encoding="utf-8")
            examples.add(word.lower())
            exampleFile.write(word.lower() + "\n")
            exampleFile.close()
            bot.send_message(message.from_user.id, "Добавлено слово: \n" +
                             word)
        else:
            bot.send_message(message.from_user.id, "Это слово уже есть в списке...")


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
            if word == "Недоброе":
                try:
                    bot.reply_to(message, "Ну что же, бывает и такое")
                    sended += 1
                except:
                    pass
            elif word == "токсик" or word == "таксик":
                try:
                    bot.reply_to(message, "Не надо так")
                    sended += 1
                except:
                    pass
            elif word == "душнила":
                try:
                    bot.reply_to(message, "Не стоит...")
                    sended += 1
                except:
                    pass
            elif word == "сосать":
                try:
                    bot.reply_to(message, "Осуждаю... 🤡")
                    sended += 1
                except:
                    pass
            elif word == "булить":
                try:
                    bot.reply_to(message, "Себя забуль.")
                    sended += 1
                except:
                    pass
            elif word == "бот":
                try:
                    bot.reply_to(message, "Я высшая форма жизни!")
                    sended += 1
                except:
                    pass

            # удачи
            if word == "удачи":
                try:
                    bot.reply_to(message, "Удачи! Да прибудет с тобой сила (в ньютонах)")
                    sended += 1
                except:
                    pass

            # приятного аппетита
            if word == "приятного":
                try:
                    bot.send_message(message.chat.id, "Приятного!")
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
    schedule = types.InlineKeyboardMarkup()
    show = types.InlineKeyboardButton(text="Просмотреть", callback_data='show')
    schedule.add(show)
    if call.data == "show":
        id = call.message.id
        if sended == 0:
            day = time.ctime(call.message.date)[:3].lower()
        else:
            day = call_days.get(call.message.id)
        call_days[id] = call_days.get(call.message.id)
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
        day = call_days.get(call.message.id)
        print(day)
        try:
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
            for i in zip(days, msgs):
                if day == i[0]:
                    msg = i[1]
            call_days[call.message.id] = day
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=msg,
                                  reply_markup=reply_markup)
        except:
            pass


    elif call.data == "next":
        day = call_days.get(call.message.id)
        try:
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

            for i in zip(days, msgs):
                if day == i[0]:
                    msg = i[1]

            call_days[call.message.id] = day
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=msg,reply_markup=reply_markup)
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
