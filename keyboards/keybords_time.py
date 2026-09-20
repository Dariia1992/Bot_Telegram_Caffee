from data import work_time
from datetime import date, timedelta
from aiogram import types


def get_data_dates():
    buttons = []
    today = date.today()#segodnya
    for dayset in range(7):
        current_day = today + timedelta(days=dayset)
        weekday = current_day.weekday()
        if weekday not in work_time.work_days:
            continue
        buttons_text = current_day.strftime("%d.%m.%Y")
        #buttons_text = current_day.strftime("%d.%m.%Y")
        button = types.InlineKeyboardButton(text=buttons_text,callback_data=f"date:{buttons_text}")
        buttons.append([button])
        
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
    