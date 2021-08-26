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

@bot.message_handler(commands=['mainteancemode'])
def mainteancemode(message):
    if message.chat.type == "private":
        global mt_owner
        bot.send_message(message.from_user.id,'MAINTEANCE MODE ENABLED!')
        mt_owner = {
            "user_id" : message.from_user.id,
            "first_name" : message.from_user.first_name,
            "last_name" : message.from_user.last_name,
            "username" : message.from_user.username
        }
        bot.register_next_step_handler(message,mainteance)
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
    if sended == 0:
        for i in inputS:
            word = str(i)
            word1 = ""
            for x in word:
                if x.isalpha() or x.isnumeric() is True:
                    word1 = word1 + str(x)
            word = word1.capitalize()
            if sended < 2:
                ## Утро
                if word == "Добрый" or word == "Дабрый":
                    try:
                        bot.send_message(message.chat.id, "Добрый!")
                        sended += 1
                    except:
                        pass
                elif word == "Доброе":
                    try:
                        bot.send_message(message.chat.id, "Доброе!")
                        sended += 1
                    except:
                        pass
                elif word == "Нихао":
                    try:
                        bot.send_message(message.chat.id, "Нихао!")
                        sended += 1
                    except:
                        pass
                elif word == "Коничива":
                    try:
                        bot.send_message(message.chat.id, "Коничива!")
                        sended += 1
                    except:
                        pass
                elif word == "Guten":
                    try:
                        bot.send_message(message.chat.id, "Guten morgen!")
                        sended += 1
                    except:
                        pass
                elif word == "Гутен":
                    try:
                        bot.send_message(message.chat.id, "Guten morgen!")
                        sended += 1
                    except:
                        pass
                elif word == "Доброго":
                    try:
                        bot.send_message(message.chat.id, "Доброго!")
                        sended += 1
                    except:
                        pass
                      
                elif word == "Добрым":
                    try:
                        bot.send_message(message.chat.id, "С добрым!")
                        sended += 1
                    except:
                        pass
                elif word == "Доброй":
                    try:
                        bot.send_message(message.chat.id, "Доброй!")
                        sended += 1
                    except:
                        pass
                elif word == "Хорошего":
                    try:
                        bot.send_message(message.chat.id, "Хорошего!")
                        sended += 1
                    except:
                        pass
                elif word == "Добрейшего":
                    try:
                        bot.send_message(message.chat.id, "Добрейшего!")
                        sended += 1
                    except:
                        pass
                elif word == "Добрейший":
                    try:
                        bot.send_message(message.chat.id, "Добрейший")
                        sended += 1
                    except:
                        pass


                #Ночь
                if word == "Спокойной" or word == "Споке" or word == "Спок":
                    try:
                        bot.send_message(message.chat.id, "Спокойной!")
                        sended += 1
                    except:
                        pass
                elif word == "Добрых":
                    try:
                        bot.send_message(message.chat.id, "Добрых!")
                        sended += 1
                    except:
                        pass



                #Ответы на приветствия
                if word == "Hello":
                    try:
                        bot.reply_to(message, "Hello!")
                        sended += 1
                    except:
                        pass
                elif word == "Привет":
                    try:
                        bot.reply_to(message,"Привет!")
                        sended += 1
                    except:
                        pass
                elif word == "Хай":
                    try:
                        bot.reply_to(message, "Хай!")
                        sended += 1
                    except:
                        pass
                #непозитивные ответы
                if word == "Недоброе":
                    try:
                        bot.reply_to(message,"Ну что же, бывает и такое")
                        sended += 1
                    except:
                        pass
                elif word == "Токсик" or word == "Таксик":
                    try:
                        bot.reply_to(message,"Не надо так")
                        sended += 1
                    except:
                        pass
                elif word == "Душнила":
                    try:
                        bot.reply_to(message,"Не стоит...")
                        sended += 1
                    except:
                        pass
                elif word == "Сосать":
                    try:
                        bot.reply_to(message,"Осуждаю... 🤡")
                        sended += 1
                    except:
                        pass
                elif word == "Булить":
                    try:
                        bot.reply_to(message,"Себя забуль.")
                        sended += 1
                    except:
                        pass
                elif word == "Бот":
                    try:
                        bot.reply_to(message,"Я высшая форма жизни!")
                        sended += 1
                    except:
                        pass


                #удачи
                if word == "Удачи":
                    try:
                        bot.reply_to(message,"Удачи! Да прибудет с тобой сила (в ньютонах)")
                        sended += 1
                    except:
                        pass

                #приятного аппетита
                if word == "Приятного":
                    try:
                        bot.send_message(message.chat.id,"Приятного!")
                        sended += 1
                    except:
                        pass

@bot.message_handler(content_types=['text'])
def mainteance(message):
    global mtcounter
    if message.text == '/mainteancemode':
        bot.register_next_step_handler(message,start_command)
        bot.send_message(message.from_user.id,"MAINTEANCE MODE DISABLED")
    elif message.from_user.id == mt_owner.get("user_id") and message.text == "/stats":
        bot.send_message(message.from_user.id,("Счетчик сообщений до предупреждения: "+str(mtcounter)))
    else: 
        mtcounter += 1
        if mtcounter == 10:
            bot.send_message(message.chat.id,"BOT IS IN MAINTEANCE MODE NOW. CONTACT @Ekso4")
            mtcounter = 0
        bot.register_next_step_handler(message,mainteance)


bot.polling()
