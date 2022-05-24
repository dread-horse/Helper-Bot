from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_api.mydb import connect


def inline_language_menu():
    keyboards = InlineKeyboardMarkup(row_width=4, time=False)

    conn, cursor = connect()

    cursor.execute("SELECT name FROM helper_language")
    myresult = cursor.fetchall()
    cursor.close()

    btn_arr = []

    for row in myresult:
        btn_arr.append(
            InlineKeyboardButton(text=row[0], callback_data=f"language {row[0]}")
        )

    keyboards.add(*btn_arr)

    return keyboards


