from aiogram import types
from data.menu_coffee import coffee
from data.menu_tea import tea
from data.menu_bakery import bakery


def get_coffee_keyboard():
    buttons = []
    for name, price in coffee.items():
        button = types.InlineKeyboardButton(text=f"{name} - {price} ₪",callback_data=name)
        buttons.append([button])
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
    
    
def get_size_keyboard():
    sizes = ["Small", "Medium", "Large"]
    buttons = []
    for size in sizes:
        button = types.InlineKeyboardButton(text=f"{size}",callback_data=size)
        buttons.append([button])
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def get_quantity_keyboard():
    buttons = []
    for i in range(1,6):
        button = types.InlineKeyboardButton(text=f"{i}",callback_data=str(i))
        buttons.append([button])
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def get_confirm_keyboard():
    buttons = []
    button_confirm = types.InlineKeyboardButton(text="✅ Confirm",callback_data="confirm")
    button_cancel = types.InlineKeyboardButton(text="❌ Cancel",callback_data="cancel")
    buttons.append([button_confirm,button_cancel])
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

#tea
def get_tea_keyboard():
    buttons = []
    for name, price in tea.items():
        button = types.InlineKeyboardButton(text=f"{name} - {price} ₪",callback_data=name)
        buttons.append([button])
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

#bakery
def get_bakery_keyboard():
    buttons = []
    for name, price in bakery.items():
        button = types.InlineKeyboardButton(text=f"{name} - {price} ₪",callback_data=name)
        buttons.append([button])
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

