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


examples = set(
    'добрый','доброе',"доброго","нихао","коничива","guten","гутен",
    "добрым","доброй","хорошего","добрейшее","добрейшего","добрейший",
    'спокойной',"добрых","сладких",
    "hello","hallo","hi","привет","хай"
)

exampleFile = open('examples.txt','r')
for line in exampleFile:
    line = line.lower()
    line1 = ""
    for x in line:
            if x.isalpha() or x.isnumeric() is True:
                line1 = line1 + str(x)
    line = line1
    examples.append(line)
exampleFile.close()
print(examples)

@bot.message_handler(commands=['addnewword'])
def new_word(message):
    print("Реакция на команду")
    if message.from_user.id == 376185154:
        exampleFile = open('examples.txt','a')
        print("Нужный пользователь")
        word = message.text[message.text.find(" ")+1:]
        print("захваченный текст "+word)
        examples.append(word.lower())
        exampleFile.write(word.lower()+"\n")
        exampleFile.close()
        bot.send_message(message.from_user.id,"Добавлено слово: \n"+
        word)

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
            "username" : message.from_user.username,
            "timeofstart" : time.ctime(message.date)
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
                    bot.send_message(message.chat.id,(example.capitalize()+"!"))
                    sended += 1
            #непозитивные ответы
            if word == "Недоброе":
                try:
                    bot.reply_to(message,"Ну что же, бывает и такое")
                    sended += 1
                except:
                    pass
            elif word == "токсик" or word == "таксик":
                try:
                    bot.reply_to(message,"Не надо так")
                    sended += 1
                except:
                    pass
            elif word == "душнила":
                try:
                    bot.reply_to(message,"Не стоит...")
                    sended += 1
                except:
                    pass
            elif word == "сосать":
                try:
                    bot.reply_to(message,"Осуждаю... 🤡")
                    sended += 1
                except:
                    pass
            elif word == "булить":
                try:
                    bot.reply_to(message,"Себя забуль.")
                    sended += 1
                except:
                    pass
            elif word == "бот":
                try:
                    bot.reply_to(message,"Я высшая форма жизни!")
                    sended += 1
                except:
                    pass


            #удачи
            if word == "удачи":
                try:
                    bot.reply_to(message,"Удачи! Да прибудет с тобой сила (в ньютонах)")
                    sended += 1
                except:
                    pass

            #приятного аппетита
            if word == "приятного":
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
        bot.register_next_step_handler(message,mainteance)
    elif message.text == "/mainteanceinfo":
        time = mt_owner.get("timeofstart").split()
        mt_time = time[3]
        bot.send_message(message.chat.id,("MAINTEANCE INFO:\nSTARTED BY: "+
        str(mt_owner.get("first_name"))+" "+str(mt_owner.get("last_name"))+
        "\nSTART TIME: "+str(mt_time)))
        bot.register_next_step_handler(message,mainteance)
    else: 
        mtcounter += 1
        if mtcounter == 10:
            bot.send_message(message.chat.id,"BOT IS IN MAINTEANCE MODE NOW.\nType /mainteanceinfo for more information")
            mtcounter = 0
        bot.register_next_step_handler(message,mainteance)


bot.polling()
