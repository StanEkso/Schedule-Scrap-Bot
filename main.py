import telebot
import sys
import time
import random
streams = ['https://youtu.be/czjXw_GmZMU','https://youtu.be/5ypwKTMpp8c','https://youtu.be/eG-vjxeg2Og','https://youtu.be/dzI95u7kgrQ','https://youtu.be/Zk3N8ePW8f4','https://youtu.be/AGLeP30qOu8',
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

@bot.message_handler(commands=['stream'])
def stream(message):
    random_stream = random.choice(streams)
    bot.send_message(message.chat.id,"Посморите как этот стрим:")
    bot.send_message(message.chat.id,random_stream)
@bot.message_handler(content_types=['text'])
def start_command(message):
    sended = 0
    try:
        input = message.text
    finally:
        pass
    print(message.from_user.first_name + " writes: " + input)
    inputS = input.split()
    if inputS[0] == "/asbot":
        bot.send_message(-1001519670451, message.text[message.text.find(" "):])
    if sended == 0:
        for i in inputS:
            word = str(i)
            word1 = ""
            for x in word:
                if x.isalpha() or x.isnumeric() is True:
                    word1 = word1 + str(x)
            word = word1.capitalize()
            if sended <= 2:
                ## Утро
                if word == "Добрый" or word == "Дабрый":
                    bot.send_message(message.chat.id, "Добрый!")
                    sended += 1
                elif word == "Доброе":
                    bot.send_message(message.chat.id, "Доброе!")
                    sended += 1
                elif word == "Нихао":
                    bot.send_message(message.chat.id, "Нихао!")
                    sended += 1
                elif word == "Коничива":
                    bot.send_message(message.chat.id, "Коничива!")
                    sended += 1
                elif word == "Guten":
                    bot.send_message(message.chat.id, "Guten morgen!")
                    sended += 1
                elif word == "Гутен":
                    bot.send_message(message.chat.id, "Guten morgen!")
                    sended += 1
                elif word == "Доброго":
                    bot.send_message(message.chat.id, "Доброго!")
                    sended += 1
                elif word == "Добрым":
                    bot.send_message(message.chat.id, "С добрым!")
                    sended += 1
                elif word == "Доброй":
                    bot.send_message(message.chat.id, "Доброй!")
                    sended += 1
                elif word == "Хорошего":
                    bot.send_message(message.chat.id, "Хорошего!")
                    sended += 1
                elif word == "Добрейшего":
                    bot.send_message(message.chat.id, "Добрейшего!")
                    sended += 1
                elif word == "Добрейший":
                    bot.send_message(message.chat.id, "Добрейший")
                    sended += 1


                #Ночь
                if word == "Спокойной" or word == "Споке" or word == "Спок":
                    bot.send_message(message.chat.id, "Спокойной!")
                    sended += 1
                elif word == "Добрых":
                    bot.send_message(message.chat.id, "Добрых!")
                    sended += 1



                #Ответы на приветствия
                if word == "Hello":
                    bot.reply_to(message, "Hello!")
                    sended += 1
                elif word == "Привет":
                    bot.reply_to(message,"Привет!")
                    sended += 1
                elif word == "Хай":
                    bot.reply_to(message, "Хай!")
                    sended += 1

                #непозитивные ответы
                if word == "Недоброе":
                    bot.reply_to(message,"Ну что же, бывает и такое")
                    sended += 1
                elif word == "Токсик" or word == "Таксик":
                    bot.reply_to(message,"Не надо так")
                    sended += 1
                elif word == "Душнила":
                    bot.reply_to(message,"Не стоит...")
                    sended += 1
                elif word == "Сосать":
                    bot.reply_to(message,"Осуждаю... 🤡")
                    sended += 1
                elif word == "Булить":
                    bot.reply_to(message,"Себя забуль.")
                    sended += 1
                elif word == "Бот":
                    bot.reply_to(message,"Я высшая форма жизни!")
                    sended += 1


                #удачи
                if word == "Удачи":
                    bot.reply_to(message,"Удачи! Да прибудет с тобой сила (в ньютонах)")
                    sended += 1

                #приятного аппетита
                if word == "Приятного":
                    bot.send_message(message.chat.id,"Приятного!")
                    sended += 1


            

bot.polling()
