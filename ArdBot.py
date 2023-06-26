#импорт библиотек
import telebot
import config
import requests
import Chart as conf
import Database as base
from loguru import logger
from telebot import types
from datetime import datetime
# Используемые переменные
on = "[активен]"
off = "[отключен]"
warn = "Вы используете админ комманды, будьте бдительны."
help = "/str - просмотр всех комманд \n /exit - Отключение бота \n /kick - выгнать участника \n /ban - выдать бан участнику \n /mute - выдать мут участнику \n /stat - статистика бота"
adpa = "123"
#переменная для библиотеки datetime
now = datetime.now()
gith = "https://github.com/rokSkr"
helpbot = "/request - Подает запрос на желаемый сайт \n /"
reqq = requests.get('https://skillbox.ru')

print("Статус: " + on)
print(now)
print("Лог-лист:\n $ [совершенное действие] [подробности] \n [время] \n [id пользователя]" )
bot = telebot.TeleBot(config.TOKEN)
logger.add("debug.log",format = "{time} {level} {message}", level = "DEBUG")
#функция для старта
@bot.message_handler(commands=["start"])
def welcome(message):

#КЛАВИАТУРА
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
#добавление кнопок
    
    item1 = types.KeyboardButton("Профиль")
    item2 = types.KeyboardButton("Донат")
    item3 = types.KeyboardButton("Комманды бота")
#добавление клавиатуры
    
    markup.add(item1,item2, item3)
    
    bot.send_message(message.chat.id, "Здраствуйте, я бот ArdBot , для управления используйте клавиатуру. ", reply_markup = markup)
    logger.info("Новый пользователь:")
    logger.info(message.chat.id)
@bot.message_handler(content_types=["text"])
def menu(message):
    if message.chat.type == "private":
#______________________________
#Админ панель бота
        #комманда /str
        if message.text == "/str":
            if message.chat.id == 934097460:
                bot.send_message(message.chat.id, "Вы успешно получили доступ к админ.коммандам.")
                logger.debug("Launched. /str")
                logger.debug(message.chat.id)
                bot.send_message(message.chat.id, help)
                
        # Комманда /ban
        if message.text == "/ban":
            bot.send_message(message.chat.id, "Бан")
            logger.debug("Launched. /ban")
            logger.debug(message.chat.id)
        # комманда /kick
        if message.text == "/kick":
            bot.send_message(message.chat.id, "kick")
            logger.debug("Launched. /kick")
            logger.debug(message.chat.id)
        #комманда /mute
        if message.text == "/mute":
            bot.send_message(message.chat.id, "mute")
            logger.debug("Launched. /mute")
            logger.debug(message.chat.id)
        # комманды /bd
        if message.text == "/bd":
            bot.send_message(message.chat.id, base.bd)
            logger.info("Launched. /bd")
            logger.info(message.chat.id)
        if message.text == "/clear":
            bot.send_message(message.chat.id, "Удалю")
        elif message.text == "Профиль":
            delb = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "📟Telegram:\n @Rok_Skr\n 📷Telegram group : \n @arDta3 \n 💻GitHub:\n rokskr", reply_markup = delb)
            
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton("GitHub")
            item5 = types.KeyboardButton("/start")
            markup1.add(item4, item5)
            bot.send_message(message.chat.id, "Воспользуйтесь клавиатурой: ", reply_markup = markup1)

        elif message.text == "Донат":
            bot.send_message(message.chat.id, "Донат")
#Отключение бота в меню
        elif message.text == "/exit":
            bot.send_message(message.chat.id, "Отключение бота...")
            bot.stop_polling()
            logger.error("Launched. /exit")
#_________________________
#Комманды бота
#_________________________
        if message.text == "Комманды бота":
            bot.send_message(message.chat.id, helpbot)
            bot.send_message(message.chat.id, now)
        if message.text == "/rq":
            bot.send_message(message.chat.id, conf.res)
            bot.send_message(message.chat.id, )
            
            print(conf.res)
            print(res1)
    if message.text == "GitHub":
            bot.send_message(message.chat.id, "Чтобы перейти к моему GitHub, нажмите на ссылку. " + gith)
#функция для отключения бота

@bot.message_handler(commands=["exit"])

def exit(message):
    bot.send_message(message.chat.id, "Статус: [отключен]. Для активизации используйте админ панель.")
    print("$  Статус. " + off)
    print(now)
    print(message.chat.id)
    bot.stop_polling()
bot.polling(none_stop=True)
#Админ комманда в боте
#функции Inline клавиатуры