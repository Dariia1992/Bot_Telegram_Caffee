from aiogram import Router, types
from aiogram.filters.command import Command

from keyboards.keyboard_main1 import kb_1
from aiogram.types import FSInputFile #img

router = Router()

# @router.message(Command("start"))
# async def command_start(message:types.Message):
#     await message.answer("☕ Welcome to Coffee Bot!\n"
#     "What would you like today? 😊",reply_markup=kb_1)

@router.message(Command("start"))
async def command_start(message: types.Message):

    photo = FSInputFile("caffee.png")
    music = FSInputFile("Cafe Del Mar - By The Sea.mp3")

    await message.answer_photo(
        photo=photo,
        caption=(
            "☕ Welcome to Coffee Bot!\n"
            "What would you like today? 😊"
        ),
        reply_markup=kb_1
    )

    await message.answer_audio(
        audio=music
    )