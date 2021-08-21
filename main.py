import telebot
import sys
import time
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
                bot.reply_to(message,"Я высшая форма жизни, а ты просто мешок с костями")


            #удачи
            if word == "Удачи":
                bot.reply_to(message,"Удачи! Да прибудет с тобой сила (в ньютонах)")

bot.polling()
