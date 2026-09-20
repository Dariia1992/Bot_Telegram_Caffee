from aiogram import types

button_date = types.KeyboardButton(text="📅 Choosing date")
button_coffee = types.KeyboardButton(text="☕ Coffee")
button_tea = types.KeyboardButton(text="🍵 Tea")
button_bakery = types.KeyboardButton(text="🥐 Bakery")

main_keyboard = [
    [button_date],
    [button_coffee,button_tea,button_bakery],
]

kb_1 = types.ReplyKeyboardMarkup(
    keyboard=main_keyboard,
    resize_keyboard=True
)