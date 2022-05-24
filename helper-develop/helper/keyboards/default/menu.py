from utils.db_api.mydb import connect
from aiogram import types


def reply_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    conn, cursor = connect()

    cursor.execute("SELECT * FROM helper_language")
    myresult = cursor.fetchall()
    cursor.close()

    btn_arr = []

    for row in myresult:
        btn_arr.append(row[1])
        
    markup.add(*btn_arr)
    
    return markup
