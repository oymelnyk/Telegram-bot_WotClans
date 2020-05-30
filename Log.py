import time
from DB import cursor, connection

def log_sys(event, message_id, text, user_id, username, user_fname, user_lname, sys_global):
    
    
    log_sys_date=str(time.strftime("%Y"+"-"+"%m"+"-"+"%d"))
    log_sys_time=str(time.strftime(" %H"+":"+"%M"+":"+"%S "))
    log_sys_event=str(event)
    log_sys_message_id=str(message_id)
    log_sys_text=str(text)
    log_sys_user_id=str(user_id)
    log_sys_username=str(username)
    log_sys_user_fname=str(user_fname)
    log_sys_user_lname=str(user_lname)
    log_sys_global=str(sys_global)
    
    connection
    cursor
    SQL_LOGS="""
                    INSERT INTO b_telegram.dbo.Logs
                    VALUES (""""'"+log_sys_date+"',"+"'"+ log_sys_time+"',"+"'"+log_sys_event+"',"+"'"+log_sys_message_id+"',"+"'"+log_sys_text+"',"+"'"+log_sys_user_id+"',"+"'"+log_sys_username+"',"+"'"+log_sys_user_fname+"',"+"'"+log_sys_user_lname+"',"+"'"+log_sys_global+"')"
    
    #SQL_LOGS="""
    #                INSERT INTO b_telegram.dbo.Logs
    #                VALUES ('a','b','c','d','e','f','g','h','k','l')"""
    cursor.execute(SQL_LOGS)
    connection.commit()
    





    print(log_sys_date+log_sys_time+" "+log_sys_event+" "+log_sys_message_id+" "+log_sys_event+" "+log_sys_text+" "+log_sys_user_id+" "+log_sys_username+" "+log_sys_user_fname+" "+log_sys_user_lname+" "+log_sys_global)




