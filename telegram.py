import telebot
from DB import connection, cursor
import time
import os 
import threading
from datafromapi import top_50, Server_info
from Log import log_sys
import re

def DB_UPDATER():                                                                                               #  
    xxx=0                                                                                                       #   xxx - переменная бесконечного цикла
    while xxx<1:                                                                                                #
        time.sleep(14400)                                                                                          #
        try:                                                                                                    #   Инструкция отвечающая за обновление содержимого 
            os.system('datafromapi.py')                                                                         #
            log_sys("Попытка обновления БД [DB_UPDATER]", None, None, None, None, None, None, "Yes")            #
            print("Попытка обновления БД [DB_UPDATER]")                                                         #
        except:                                                                                                 #
            log_sys("Ошибка обновления БД [DB_UPDATER]", None, None, None, None, None, None, "Yes")             #
            print("Ошибка обновления БД [DB_UPDATER]r")                                                         #

t = threading.Thread(target=DB_UPDATER, name='DB_UPDATER')                                                      #   Заводим во второй поток функцию DB_UPDATER


#API Telegram BOT                                                                #
bot = telebot.TeleBot(" ")          #   Подключаемся к боту
print("Бот-токен получен")                                                       #
log_sys("Бот-токен получен", None, None, None, None, None, None, "Yes")          #

#БОТ-Клавиатура
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/help','/top50','/status')

#БОТ-Старт                                                                                                                                                                                   #
@bot.message_handler(commands=['start'])                                                                                                                                                        #
def send_welcome(message):                                                                                                                                                                      #   Инструкция стартовой команды бота
    log_sys("Пользователь запустил бота [/start]", message.message_id, message.text, message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name, "No")             # (event, message_id, text, user_id, username, user_fname, user_lname, sys_global)     
    bot.send_message(message.chat.id, "Привет, я клановый инфо-бот! Для получения списка команд используй /help \nДля получения информации о клане введи клан-тег", reply_markup=keyboard1)                             #

#БОТ-помощь
@bot.message_handler(commands=['help'])                                                                                                                                                        #
def send_message(message_help):                                                                                                                                                                      #   Инструкция стартовой команды бота
    log_sys("Пользователь нажал [/help]", message_help.message_id, message_help.text, message_help.chat.id, message_help.chat.username, message_help.chat.first_name, message_help.chat.last_name, "No")             # (event, message_id, text, user_id, username, user_fname, user_lname, sys_global)     
    bot.send_message(message_help.chat.id, 'Для вывода информации о нужном тебе клане, просто напиши его клан-тег в боте, если добавляешь бота в групповой чат, то клан тег пиши через "/"\nПример "/E-BAN"\nОстальные опции можно запросить нажав кнопки!')                             #

#Бот-Статус серверов
@bot.message_handler(commands=['status'])                                                                                                                                                        #
def send_message_server(message_server):
    log_sys("Пользователь запросил вывод статуса серверов [/status]", message_server.message_id, message_server.text, message_server.chat.id, message_server.chat.username, message_server.chat.first_name, message_server.chat.last_name, "No")       #
    bot.send_message(message_server.chat.id,Server_info())


#TOP50                                                                                                                                                                                                                                       #
@bot.message_handler(commands=['top50'])                                                                                                                                                                                                     #   Инcтрукция выдачи рейтинга топ-50 кланов
def send_message_top50(message_top50):                                                                                                                                                                                                             #
    log_sys("Пользователь запросил вывод топ-50 кланов [/top50]", message_top50.message_id, message_top50.text, message_top50.chat.id, message_top50.chat.username, message_top50.chat.first_name, message_top50.chat.last_name, "No")       #
    bot.send_message(message_top50.chat.id,top_50())                                                                                                                                                                                         #   top_50() - данные из БД

#Clan_Tag                                                                                                                                                                                                                   #
@bot.message_handler(content_types= 'text' )                                                                                                                                                                                #
def handle_text(message_tag):                                                                                                                                                                                               #   Инструкция выдачи рейтинга клана по клан-тегу
    log_sys("Пользователь запросил вывод данных о клане", message_tag.message_id, message_tag.text, message_tag.chat.id, message_tag.chat.username, message_tag.chat.first_name, message_tag.chat.last_name, "No")          #                                                                                                                                  #
    message_tag_x=str(message_tag.text)
    message_tag_x=re.sub(r"/", "", message_tag_x)
    bot.send_message(message_tag.chat.id, "Вы выбрали клан тег: "+message_tag_x)                                                                                                                                                                                                                #   Ниже SQL запрос на выборку инфы из БД
    OneH_SQL_SELECT="""                                                                                                         
                            SELECT *
                            FROM [b_telegram].[dbo].[Clans] WHERE clan_tag ='"""+message_tag_x+"""'
                    """
    cursor.execute(OneH_SQL_SELECT)                                                                                                                 #
    results=cursor.fetchall()                                                                                                                       #   Получаем массив инфы
    try:                                                                                                                                            #   Сортировка
        y=results[0][1]                                                                                                                             #
        print(y)                                                                                                                                    #
        try:                                                                                                                                        #
            tel_id=str(results[0][0])                                                                                                               #
            tel_tag=str(results[0][1])                                                                                                              #
            tel_name=str(results[0][2])                                                                                                             #
            tel_efficiency_rank=str(results[0][3])                                                                                                  #
            tel_efficiency_rank_delta=str(results[0][4])                                                                                            #
            tel_fb_elo_rating_10=str(results[0][5])                                                                                                 #
            tel_fb_elo_rating_8=str(results[0][6])                                                                                                  #
            tel_fb_elo_rating_6=str(results[0][7])                                                                                                  #
            tel_gm_elo_rating_10=str(results[0][8])                                                                                                 #
            tel_v10l_avg=str(results[0][9])                                                                                                         #
            tel_wins_ratio_avg=str(results[0][10])                                                                                                  #
            tel_clan_link=str(results[0][11])                                                                                                       #
                                                                                                                                                        #   
            ALL_DATA=("Клан-тег: "+tel_tag+"\n"                                                                                                         #   После сортировки готовим данные
        "Название клана: "+tel_name+"\n"                                                                                                                #
        "ID Клана: "+tel_id+"\n"                                                                                                                        #
        "Позиция клана: "+tel_efficiency_rank+"\n"                                                                                                      #
        "Изменение позиции клана: "+tel_efficiency_rank_delta+"\n"                                                                                      #
        "ЭЛО Укрепрайона (10 уровень): "+tel_fb_elo_rating_10+"\n"                                                                                      #
        "ЭЛО Укрепрайона (8 уровень): "+tel_fb_elo_rating_8+"\n"                                                                                        #
        "ЭЛО Укрепрайона (6 уровень): "+tel_fb_elo_rating_6+"\n"                                                                                        #
        "ЭЛО Глобальная карта (10 уровень): "+tel_gm_elo_rating_10+"\n"                                                                                 #
        "Среднее количество техники 10 уровня на игрока клана: "+tel_v10l_avg+"\n"                                                                      #
        "Средний процент побед игроков клана: "+tel_wins_ratio_avg+"\n"                                                                                 #
        "Ссылка: "+tel_clan_link)                                                                                                                       #
                                                                                                                                                        #
            bot.send_message(message_tag.chat.id, ALL_DATA)                                                                                             #   Вывод данных в телегу
                                                                                                                                                        #
        except:                                                                                                                                     #
            print("Error in clan_tag")                                                                                                              #
    except:                                                                                                                                         #
        bot.send_message(message_tag.chat.id, "Клан-тег не найден")                                                                                 #   Вывод если клан тега в БД нет
                                                                                                                                                    #

try:                                                                                                                            #
    t.start()                                                                                                                   #   Запуск второго потока с функцией DB_UPDATER
    log_sys("Запуск второго потока с функцией DB_UPDATER", None, None, None, None, None, None, "Yes")                           #   
except:                                                                                                                         #
    log_sys("Ошибка запуска второго потока с функцией DB_UPDATER", None, None, None, None, None, None, "Yes")                   #   

bot.polling(none_stop=True, timeout=123)                                                                                        #   Опрос бота
log_sys("Бот завершил свою работу", None, None, None, None, None, None, "Yes")                                                  #















