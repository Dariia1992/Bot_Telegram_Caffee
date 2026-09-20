from data import work_time
from datetime import date, timedelta,datetime
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
    

def get_time_keyboard():
    buttons = []

    start_time = datetime.strptime(
        work_time.work_start_time,
        "%H:%M"
    )

    end_time = datetime.strptime(
        work_time.work_end_time,
        "%H:%M"
    )

    current_time = start_time

    while current_time < end_time:
        time_text = current_time.strftime("%H:%M")

        button = types.InlineKeyboardButton(
            text=time_text,
            callback_data=f"time:{time_text}"
        )

        buttons.append([button])

        current_time += timedelta(minutes=30)

    return types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )