import telebot
import sys
import time
import random
streams = ['https://youtu.be/czjXw_GmZMU','https://youtu.be/5ypwKTMpp8c',
'https://youtu.be/eG-vjxeg2Og',
'https://youtu.be/dzI95u7kgrQ',
'https://youtu.be/Zk3N8ePW8f4',
'https://youtu.be/AGLeP30qOu8',
'https://youtu.be/t0AVXlHzkoQ',
'https://youtu.be/_671f3kAMYY',
'https://youtu.be/dT_XT9lld04',
'https://youtu.be/ZLrx_-AkEDw',
'https://youtu.be/1BzQrDGrces',
'https://youtu.be/zzLeJ3V-aqA',
'https://youtu.be/8zErbnThKVQ',
'https://youtu.be/_fwPrnJtafA',
'https://youtu.be/aYR3Gl_nmH0']
bot = telebot.TeleBot('1955658538:AAGDDsLSNqDuClkSvPtE3AiDEAm0jdxOxMo')
@bot.message_handler(content_types=['text'])
def start_command(message):
    try:
        input = message.text
    finally:
        pass
    print(message.from_user.first_name + " writes: " + input)
    inputS = input.split()
    if inputS[0] == "/asbot":
        bot.send_message(-1001519670451, message.text[message.text.find(" "):])
    if not(len(input) >= 30):
        for i in inputS:
            word = str(i)
            word1 = ""
            for x in word:
                if x.isalpha() or x.isnumeric() is True:
                    word1 = word1 + str(x)
            word = word1.capitalize()

            ## Утро
            if word == "Добрый" or word == "Дабрый":
                bot.send_message(message.chat.id, "Добрый!")
            elif word == "Доброе":
                bot.send_message(message.chat.id, "Доброе!")
            elif word == "Нихао":
                bot.send_message(message.chat.id, "Нихао!")
            elif word == "Коничива":
                bot.send_message(message.chat.id, "Коничива!")
            elif word == "Guten":
                bot.send_message(message.chat.id, "Guten morgen!")
            elif word == "Гутен":
                bot.send_message(message.chat.id, "Guten morgen!")
            elif word == "Доброго":
                bot.send_message(message.chat.id, "Доброго!")
            elif word == "Добрым":
                bot.send_message(message.chat.id, "С добрым!")
            elif word == "Доброй":
                bot.send_message(message.chat.id, "Доброй!")
            elif word == "Хорошего":
                bot.send_message(message.chat.id, "Хорошего!")
            elif word == "Добрейшего":
                bot.send_message(message.chat.id, "Добрейшего!")
            elif word == "Добрейший":
                bot.send_message(message.chat.id, "Добрейший")


            #Ночь
            if word == "Спокойной" or word == "Споке" or word == "Спок":
                bot.send_message(message.chat.id, "Спокойной!")
            elif word == "Добрых":
                bot.send_message(message.chat.id, "Добрых!")



            #Ответы на приветствия
            if word == "Hello":
                bot.reply_to(message, "Hello!")
            elif word == "Привет":
                bot.reply_to(message,"Привет!")
            elif word == "Хай":
                bot.reply_to(message, "Хай!")

            #непозитивные ответы
            if word == "Недоброе":
                bot.reply_to(message,"Ну что же, бывает и такое")
            elif word == "Токсик" or word == "Таксик":
                bot.reply_to(message,"Не надо так")
            elif word == "Душнила":
                bot.reply_to(message,"Не стоит...")
            elif word == "Сосать":
                bot.reply_to(message,"Осуждаю... 🤡")
            elif word == "Булить":
                bot.reply_to(message,"Себя забуль.")
            elif word == "Бот":
                bot.reply_to(message,"Я высшая форма жизни!")


            #удачи
            if word == "Удачи":
                bot.reply_to(message,"Удачи! Да прибудет с тобой сила (в ньютонах)")

            #приятного аппетита
            if word == "Приятного":
                bot.send_message(message.chat.id,"Приятного!")

            #стримы Перца
            if word == 'Cтрим':
                random_stream = random.choice(streams)
                bot.send_message(message.chat.id,"Посморите как этот стрим:")
                bot.send_message(message.chat.id,random_stream)

bot.polling()
