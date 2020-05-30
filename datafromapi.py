import requests
import json
import pypyodbc
import re
from DB import connection, cursor, SQL_DELETE_DATA_Clans, SQL_SELECT_TOP_50


#   Подключаем БД
connection
cursor
ttt=str("ttt")





#   Инструкция для получения инфо по API и запись в БД
def data_clans():
#   API Запросы
    #   Запрос на первую тысячу кланов
    try:
        Clear_API_Request = requests.get('https://api.worldoftanks.ru/wot/clanratings/top/?application_id=AAAAAA&limit=1000&page_no=1&rank_field=efficiency&fields=clan_id%2C+clan_tag%2C+clan_name%2C+efficiency.rank%2C+v10l_avg%2C+wins_ratio_avg%2C+fb_elo_rating_10%2Cfb_elo_rating_8%2Cfb_elo_rating_6%2C+efficiency.rank_delta%2Cgm_elo_rating_10')
        Clear_API_Request = Clear_API_Request.json()
    except:
        print("1 Не доступен worldoftanks.ru")
    #   Запрос на вторую тысячу кланов
    try:
        Clear_API_Request_2 = requests.get('https://api.worldoftanks.ru/wot/clanratings/top/?application_id=AAAAAAA&limit=1000&page_no=2&rank_field=efficiency&fields=clan_id%2C+clan_tag%2C+clan_name%2C+efficiency.rank%2C+v10l_avg%2C+wins_ratio_avg%2C+fb_elo_rating_10%2Cfb_elo_rating_8%2Cfb_elo_rating_6%2C+efficiency.rank_delta%2Cgm_elo_rating_10')
        Clear_API_Request_2 = Clear_API_Request_2.json()
    except:
        print("2 Не доступен worldoftanks.ru")
        print("Проверьте сетевое подключение и перезапустите программу! Для выходна нажмите любую клавишу.")
        input()
    #   Перебираем полученую инфу и записываем в БД первую тысячу кланов
    n=000
    m=000
    while n<=999:
    
        API_clan_id = str(Clear_API_Request['data'][n]['clan_id'])
        API_clan_tag = str(Clear_API_Request['data'][n]['clan_tag'])
        API_clan_name_re = str(Clear_API_Request['data'][n]['clan_name'])
        API_clan_name = re.sub(r"\'", "''", API_clan_name_re)
        emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)

        API_clan_name = emoji_pattern.sub(r'', API_clan_name)
        API_efficiency_rank = str(Clear_API_Request['data'][n]['efficiency']['rank'])
        API_efficiency_rank_delta=Clear_API_Request['data'][n]['efficiency']['rank_delta']
        API_fb_elo_rating_10 = str(Clear_API_Request['data'][n]['fb_elo_rating_10']['value'])
        API_fb_elo_rating_8 = str(Clear_API_Request['data'][n]['fb_elo_rating_8']['value'])
        API_fb_elo_rating_6 = str(Clear_API_Request['data'][n]['fb_elo_rating_6']['value'])
        API_gm_elo_rating_10 = str(Clear_API_Request['data'][n]['gm_elo_rating_10']['value'])
        API_v10l_avg = str(Clear_API_Request['data'][n]['v10l_avg']['value'])
        API_wins_ratio_avg = str(Clear_API_Request['data'][n]['wins_ratio_avg']['value'])
        Clan_link=str("https://ru.wargaming.net/clans/wot/"+API_clan_id+"/")
        def ifelse1_1():                                    #   К значениям дельты >0 добавляем "+"
            API_efficiency_rank_delta_="+"+str(API_efficiency_rank_delta)
            OneH_SQL_Insert1="""
                    INSERT INTO b_telegram.dbo.Clans
                    VALUES (""""'"+API_clan_id+"',"+"'"+API_clan_tag+"',"+"'"+API_clan_name+"',"+"'"+API_efficiency_rank+"',"+"'"+API_efficiency_rank_delta_+"',"+"'"+API_fb_elo_rating_10+"',"+"'"+API_fb_elo_rating_8+"',"+"'"+API_fb_elo_rating_6+"',"+"'"+API_gm_elo_rating_10+"',"+"'"+API_v10l_avg+"',"+"'"+API_wins_ratio_avg+"',"+"'"+Clan_link+"')"
            cursor.execute(OneH_SQL_Insert1)          
       
        def ifelse1_2():                                    #   К значениям ==0 либо <0 ничего не добавляем
            API_efficiency_rank_delta_=str(API_efficiency_rank_delta)
            OneH_SQL_Insert11="""
                    INSERT INTO b_telegram.dbo.Clans
                    VALUES (""""'"+API_clan_id+"',"+"'"+API_clan_tag+"',"+"'"+API_clan_name+"',"+"'"+API_efficiency_rank+"',"+"'"+API_efficiency_rank_delta_+"',"+"'"+API_fb_elo_rating_10+"',"+"'"+API_fb_elo_rating_8+"',"+"'"+API_fb_elo_rating_6+"',"+"'"+API_gm_elo_rating_10+"',"+"'"+API_v10l_avg+"',"+"'"+API_wins_ratio_avg+"',"+"'"+Clan_link+"')"
            cursor.execute(OneH_SQL_Insert11)
                                                            #   Запись данных в БД
        if API_efficiency_rank_delta==None:                 #   Если значение у WG API == None, значит писать 0
            API_efficiency_rank_delta=0                     #
            if API_efficiency_rank_delta>0:                 #   
                ifelse1_1()                                 #
            else:                                           #
                ifelse1_2()                                 #
        else:                                               #
            if API_efficiency_rank_delta>0:                 #
                ifelse1_1()                                 #
            else:                                           #
                ifelse1_2()                                 #
        n=n+1                                               #
#   Перебираем полученую инфу и записываем в БД вторую тысячу кланов        
    while m<=999: 
        API_clan_id_2 = str(Clear_API_Request_2['data'][m]['clan_id'])
        API_clan_tag_2 = str(Clear_API_Request_2['data'][m]['clan_tag'])
        API_clan_name_re_2 = str(Clear_API_Request_2['data'][m]['clan_name'])
        API_clan_name_2 = re.sub(r"\'", "''", API_clan_name_re_2)
        emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)

        API_clan_name_2 = emoji_pattern.sub(r'', API_clan_name_2)
        API_efficiency_rank_2 = str(Clear_API_Request_2['data'][m]['efficiency']['rank'])
        API_efficiency_rank_delta_2 =Clear_API_Request_2['data'][m]['efficiency']['rank_delta']
        API_fb_elo_rating_10_2 = str(Clear_API_Request_2['data'][m]['fb_elo_rating_10']['value'])
        API_fb_elo_rating_8_2 = str(Clear_API_Request_2['data'][m]['fb_elo_rating_8']['value'])
        API_fb_elo_rating_6_2 = str(Clear_API_Request_2['data'][m]['fb_elo_rating_6']['value'])
        API_gm_elo_rating_10_2 = str(Clear_API_Request_2['data'][m]['gm_elo_rating_10']['value'])
        API_v10l_avg_2 = str(Clear_API_Request_2['data'][m]['v10l_avg']['value'])
        API_wins_ratio_avg_2 = str(Clear_API_Request_2['data'][m]['wins_ratio_avg']['value'])
        Clan_link2=str("https://ru.wargaming.net/clans/wot/"+API_clan_id_2+"/")
        def ifelse2_1():
            API_efficiency_rank_delta_2_="+"+str(API_efficiency_rank_delta_2)
            OneH_SQL_Insert2="""
                    INSERT INTO b_telegram.dbo.Clans
                    VALUES (""""'"+API_clan_id_2+"',"+"'"+API_clan_tag_2+"',"+"'"+API_clan_name_2+"',"+"'"+API_efficiency_rank_2+"',"+"'"+API_efficiency_rank_delta_2_+"',"+"'"+API_fb_elo_rating_10_2+"',"+"'"+API_fb_elo_rating_8_2+"',"+"'"+API_fb_elo_rating_6_2+"',"+"'"+API_gm_elo_rating_10_2+"',"+"'"+API_v10l_avg_2+"',"+"'"+API_wins_ratio_avg_2+"',"+"'"+Clan_link2+"')"
            cursor.execute(OneH_SQL_Insert2)
            

        def ifelse2_2():
            API_efficiency_rank_delta_2_=str(API_efficiency_rank_delta_2)
            OneH_SQL_Insert22="""
                    INSERT INTO b_telegram.dbo.Clans
                    VALUES (""""'"+API_clan_id_2+"',"+"'"+API_clan_tag_2+"',"+"'"+API_clan_name_2+"',"+"'"+API_efficiency_rank_2+"',"+"'"+API_efficiency_rank_delta_2_+"',"+"'"+API_fb_elo_rating_10_2+"',"+"'"+API_fb_elo_rating_8_2+"',"+"'"+API_fb_elo_rating_6_2+"',"+"'"+API_gm_elo_rating_10_2+"',"+"'"+API_v10l_avg_2+"',"+"'"+API_wins_ratio_avg_2+"',"+"'"+Clan_link2+"')"
            cursor.execute(OneH_SQL_Insert22)
        
        if API_efficiency_rank_delta_2==None:
            API_efficiency_rank_delta_2=0
            if API_efficiency_rank_delta_2>0:
                ifelse2_1()
            else:
                ifelse2_2()
        else:
            if API_efficiency_rank_delta_2>0:
                ifelse2_1()
            else:
                ifelse2_2()
            
        m=m+1
    connection.commit()             #   Заканчиваем запись в БД
    
    print("DB Update")              #   Выводим надпись об обновлении

#   Инструкция по обновлению инфы в БД
def try_ ():
    try:
        data_clans()
        print("Data add without delete")
    except:
        cursor.execute(SQL_DELETE_DATA_Clans)
        print("Data Delete")
        data_clans()
        print("Data ADD")
    else:
        print("DB is not updated - API trouble")
        pass
try_()

#   Инструкция на выборку из БД по топ 50 кланам и форматируем инфу
def top_50():
    cursor.execute(SQL_SELECT_TOP_50)
    top50_data=cursor.fetchall()

    top50_data1= "№ "+str(top50_data[0][0])+" || Клан-тег: "+str(top50_data[0][1])+" || Изменение позиции: "+str(top50_data[0][2])+"\n"
    top50_data2= "№ "+str(top50_data[1][0])+" || Клан-тег: "+str(top50_data[1][1])+" || Изменение позиции: "+str(top50_data[1][2])+"\n"
    top50_data3= "№ "+str(top50_data[2][0])+" || Клан-тег: "+str(top50_data[2][1])+" || Изменение позиции: "+str(top50_data[2][2])+"\n"
    top50_data4= "№ "+str(top50_data[3][0])+" || Клан-тег: "+str(top50_data[3][1])+" || Изменение позиции: "+str(top50_data[3][2])+"\n"
    top50_data5= "№ "+str(top50_data[4][0])+" || Клан-тег: "+str(top50_data[4][1])+" || Изменение позиции: "+str(top50_data[4][2])+"\n"
    top50_data6= "№ "+str(top50_data[5][0])+" || Клан-тег: "+str(top50_data[5][1])+" || Изменение позиции: "+str(top50_data[5][2])+"\n"
    top50_data7= "№ "+str(top50_data[6][0])+" || Клан-тег: "+str(top50_data[6][1])+" || Изменение позиции: "+str(top50_data[6][2])+"\n"
    top50_data8= "№ "+str(top50_data[7][0])+" || Клан-тег: "+str(top50_data[7][1])+" || Изменение позиции: "+str(top50_data[7][2])+"\n"
    top50_data9= "№ "+str(top50_data[8][0])+" || Клан-тег: "+str(top50_data[8][1])+" || Изменение позиции: "+str(top50_data[8][2])+"\n"
    top50_data10= "№ "+str(top50_data[9][0])+" || Клан-тег: "+str(top50_data[9][1])+" || Изменение позиции: "+str(top50_data[9][2])+"\n"
    top50_data11="№ "+str(top50_data[10][0])+" || Клан-тег: "+str(top50_data[10][1])+" || Изменение позиции: "+str(top50_data[10][2])+"\n"
    top50_data12="№ "+str(top50_data[11][0])+" || Клан-тег: "+str(top50_data[11][1])+" || Изменение позиции: "+str(top50_data[11][2])+"\n"
    top50_data13="№ "+str(top50_data[12][0])+" || Клан-тег: "+str(top50_data[12][1])+" || Изменение позиции: "+str(top50_data[12][2])+"\n"
    top50_data14="№ "+str(top50_data[13][0])+" || Клан-тег: "+str(top50_data[13][1])+" || Изменение позиции: "+str(top50_data[13][2])+"\n"
    top50_data15="№ "+str(top50_data[14][0])+" || Клан-тег: "+str(top50_data[14][1])+" || Изменение позиции: "+str(top50_data[14][2])+"\n"
    top50_data16="№ "+str(top50_data[15][0])+" || Клан-тег: "+str(top50_data[15][1])+" || Изменение позиции: "+str(top50_data[15][2])+"\n"
    top50_data17="№ "+str(top50_data[16][0])+" || Клан-тег: "+str(top50_data[16][1])+" || Изменение позиции: "+str(top50_data[16][2])+"\n"
    top50_data18="№ "+str(top50_data[17][0])+" || Клан-тег: "+str(top50_data[17][1])+" || Изменение позиции: "+str(top50_data[17][2])+"\n"
    top50_data19="№ "+str(top50_data[18][0])+" || Клан-тег: "+str(top50_data[18][1])+" || Изменение позиции: "+str(top50_data[18][2])+"\n"
    top50_data20="№ "+str(top50_data[19][0])+" || Клан-тег: "+str(top50_data[19][1])+" || Изменение позиции: "+str(top50_data[19][2])+"\n"
    top50_data21="№ "+str(top50_data[20][0])+" || Клан-тег: "+str(top50_data[20][1])+" || Изменение позиции: "+str(top50_data[20][2])+"\n"
    top50_data22="№ "+str(top50_data[21][0])+" || Клан-тег: "+str(top50_data[21][1])+" || Изменение позиции: "+str(top50_data[21][2])+"\n"
    top50_data23="№ "+str(top50_data[22][0])+" || Клан-тег: "+str(top50_data[22][1])+" || Изменение позиции: "+str(top50_data[22][2])+"\n"
    top50_data24="№ "+str(top50_data[23][0])+" || Клан-тег: "+str(top50_data[23][1])+" || Изменение позиции: "+str(top50_data[23][2])+"\n"
    top50_data25="№ "+str(top50_data[24][0])+" || Клан-тег: "+str(top50_data[24][1])+" || Изменение позиции: "+str(top50_data[24][2])+"\n"
    top50_data26="№ "+str(top50_data[25][0])+" || Клан-тег: "+str(top50_data[25][1])+" || Изменение позиции: "+str(top50_data[25][2])+"\n"
    top50_data27="№ "+str(top50_data[26][0])+" || Клан-тег: "+str(top50_data[26][1])+" || Изменение позиции: "+str(top50_data[26][2])+"\n"
    top50_data28="№ "+str(top50_data[27][0])+" || Клан-тег: "+str(top50_data[27][1])+" || Изменение позиции: "+str(top50_data[27][2])+"\n"
    top50_data29="№ "+str(top50_data[28][0])+" || Клан-тег: "+str(top50_data[28][1])+" || Изменение позиции: "+str(top50_data[28][2])+"\n"
    top50_data30="№ "+str(top50_data[29][0])+" || Клан-тег: "+str(top50_data[29][1])+" || Изменение позиции: "+str(top50_data[29][2])+"\n"
    top50_data31="№ "+str(top50_data[30][0])+" || Клан-тег: "+str(top50_data[30][1])+" || Изменение позиции: "+str(top50_data[30][2])+"\n"
    top50_data32="№ "+str(top50_data[31][0])+" || Клан-тег: "+str(top50_data[31][1])+" || Изменение позиции: "+str(top50_data[31][2])+"\n"
    top50_data33="№ "+str(top50_data[32][0])+" || Клан-тег: "+str(top50_data[32][1])+" || Изменение позиции: "+str(top50_data[32][2])+"\n"
    top50_data34="№ "+str(top50_data[33][0])+" || Клан-тег: "+str(top50_data[33][1])+" || Изменение позиции: "+str(top50_data[33][2])+"\n"
    top50_data35="№ "+str(top50_data[34][0])+" || Клан-тег: "+str(top50_data[34][1])+" || Изменение позиции: "+str(top50_data[34][2])+"\n"
    top50_data36="№ "+str(top50_data[35][0])+" || Клан-тег: "+str(top50_data[35][1])+" || Изменение позиции: "+str(top50_data[35][2])+"\n"
    top50_data37="№ "+str(top50_data[36][0])+" || Клан-тег: "+str(top50_data[36][1])+" || Изменение позиции: "+str(top50_data[36][2])+"\n"
    top50_data38="№ "+str(top50_data[37][0])+" || Клан-тег: "+str(top50_data[37][1])+" || Изменение позиции: "+str(top50_data[37][2])+"\n"
    top50_data39="№ "+str(top50_data[38][0])+" || Клан-тег: "+str(top50_data[38][1])+" || Изменение позиции: "+str(top50_data[38][2])+"\n"
    top50_data40="№ "+str(top50_data[39][0])+" || Клан-тег: "+str(top50_data[39][1])+" || Изменение позиции: "+str(top50_data[39][2])+"\n"
    top50_data41="№ "+str(top50_data[40][0])+" || Клан-тег: "+str(top50_data[40][1])+" || Изменение позиции: "+str(top50_data[40][2])+"\n"
    top50_data42="№ "+str(top50_data[41][0])+" || Клан-тег: "+str(top50_data[41][1])+" || Изменение позиции: "+str(top50_data[41][2])+"\n"
    top50_data43="№ "+str(top50_data[42][0])+" || Клан-тег: "+str(top50_data[42][1])+" || Изменение позиции: "+str(top50_data[42][2])+"\n"
    top50_data44="№ "+str(top50_data[43][0])+" || Клан-тег: "+str(top50_data[43][1])+" || Изменение позиции: "+str(top50_data[43][2])+"\n"
    top50_data45="№ "+str(top50_data[44][0])+" || Клан-тег: "+str(top50_data[44][1])+" || Изменение позиции: "+str(top50_data[44][2])+"\n"
    top50_data46="№ "+str(top50_data[45][0])+" || Клан-тег: "+str(top50_data[45][1])+" || Изменение позиции: "+str(top50_data[45][2])+"\n"
    top50_data47="№ "+str(top50_data[46][0])+" || Клан-тег: "+str(top50_data[46][1])+" || Изменение позиции: "+str(top50_data[46][2])+"\n"
    top50_data48="№ "+str(top50_data[47][0])+" || Клан-тег: "+str(top50_data[47][1])+" || Изменение позиции: "+str(top50_data[47][2])+"\n"
    top50_data49="№ "+str(top50_data[48][0])+" || Клан-тег: "+str(top50_data[48][1])+" || Изменение позиции: "+str(top50_data[48][2])+"\n"
    top50_data50="№ "+str(top50_data[49][0])+" || Клан-тег: "+str(top50_data[49][1])+" || Изменение позиции: "+str(top50_data[49][2])+"\n"

    TOP_50=top50_data1+top50_data2+top50_data3+top50_data4+top50_data5+top50_data6+top50_data7+top50_data8+top50_data9+top50_data10+top50_data11+top50_data12+top50_data13+top50_data14+top50_data15+top50_data16+top50_data17+top50_data18+top50_data19+top50_data20+top50_data21+top50_data22+top50_data23+top50_data24+top50_data25+top50_data26+top50_data27+top50_data28+top50_data29+top50_data30+top50_data31+top50_data32+top50_data33+top50_data34+top50_data35+top50_data36+top50_data37+top50_data38+top50_data39+top50_data40+top50_data41+top50_data42+top50_data43+top50_data44+top50_data45+top50_data46+top50_data47+top50_data48+top50_data49+top50_data50
    return TOP_50

def Server_info():
    try:
        Clear_API_Request_3 = requests.get('https://api.worldoftanks.ru/wgn/servers/info/?application_id=AAAAAAA&language=ru&game=wot&fields=server%2C+players_online')
        Clear_API_Request_3 = Clear_API_Request_3.json()
        server_ru1=str("Server: "+Clear_API_Request_3['data']['wot'][3]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][3]['players_online'])+"\n\n"
        server_ru2=str("Server: "+Clear_API_Request_3['data']['wot'][2]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][2]['players_online'])+"\n\n"
        server_ru3=str("Server: "+Clear_API_Request_3['data']['wot'][4]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][4]['players_online'])+"\n\n"
        server_ru4=str("Server: "+Clear_API_Request_3['data']['wot'][7]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][7]['players_online'])+"\n\n"
        server_ru5=str("Server: "+Clear_API_Request_3['data']['wot'][6]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][6]['players_online'])+"\n\n"
        server_ru6=str("Server: "+Clear_API_Request_3['data']['wot'][5]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][5]['players_online'])+"\n\n"
        server_ru7=str("Server: "+Clear_API_Request_3['data']['wot'][1]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][1]['players_online'])+"\n\n"
        server_ru8=str("Server: "+Clear_API_Request_3['data']['wot'][0]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][0]['players_online'])+"\n\n"
        server_ru9=str("Server: "+Clear_API_Request_3['data']['wot'][8]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][8]['players_online'])+"\n\n"
        server_ru10=str("Server: "+Clear_API_Request_3['data']['wot'][9]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][9]['players_online'])+"\n\n"
        server_ru11=str("Server: "+Clear_API_Request_3['data']['wot'][10]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][10]['players_online'])+"\n\n"
        server_ru12=str("Server: "+Clear_API_Request_3['data']['wot'][11]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][11]['players_online'])+"\n\n"
        server_ru13=str("Server: "+Clear_API_Request_3['data']['wot'][12]['server']+"\nOnline: ")+str(Clear_API_Request_3['data']['wot'][12]['players_online'])+"\n\n"
        server_all="WoT RU Online: "+str(Clear_API_Request_3['data']['wot'][0]['players_online']+Clear_API_Request_3['data']['wot'][1]['players_online']+Clear_API_Request_3['data']['wot'][2]['players_online']+Clear_API_Request_3['data']['wot'][3]['players_online']+Clear_API_Request_3['data']['wot'][4]['players_online']+Clear_API_Request_3['data']['wot'][5]['players_online']+Clear_API_Request_3['data']['wot'][6]['players_online']+Clear_API_Request_3['data']['wot'][7]['players_online']+Clear_API_Request_3['data']['wot'][8]['players_online']+Clear_API_Request_3['data']['wot'][9]['players_online']+Clear_API_Request_3['data']['wot'][10]['players_online']+Clear_API_Request_3['data']['wot'][11]['players_online']+Clear_API_Request_3['data']['wot'][12]['players_online'])
        server_info=server_ru1+server_ru2+server_ru3+server_ru4+server_ru5+server_ru6+server_ru7+server_ru8+server_ru9+server_ru10+server_ru11+server_ru12+server_ru13+server_all
        return server_info
    except:
        print("В данный момент, информация о серверах недоступна!")
Server_info()



