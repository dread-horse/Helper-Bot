from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.engine.mydb_help import get_name_theme


def inline_theme_menu(lang: str):
    result = get_name_theme(language=lang)

    keyboards = InlineKeyboardMarkup(row_width=3)
    btn_arr = []
    for row in result:
        btn_arr.append(
            InlineKeyboardButton(text=row[0], callback_data=f"theme {row[0]} {row[1]}")
        )

    keyboards.add(*btn_arr)
    return keyboards

