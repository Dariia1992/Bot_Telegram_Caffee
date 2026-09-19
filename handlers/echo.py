from aiogram import Router, types

router = Router()

@router.message()
async def echo_message(message: types.Message):
    await message.answer(
        "🤔 I don't understand.\n"
        "Please choose an option from the menu."
    )