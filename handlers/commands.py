from aiogram import Router, types
from aiogram.filters.command import Command

from keyboards.keyboard_main1 import kb_1


router = Router()

@router.message(Command("start"))
async def command_start(message:types.Message):
    await message.answer("☕ Welcome to Coffee Bot!\n"
    "What would you like today? 😊",reply_markup=kb_1)