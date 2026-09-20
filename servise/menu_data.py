from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.keybords_time import get_data_dates,get_time_keyboard
from states.order import OrderStates



router = Router()


# КНОПКА DATE В ГЛАВНОМ МЕНЮ
@router.message(F.text == "📅 Choosing date")
async def date_menu(
    message: types.Message,
    state: FSMContext
):
    await state.set_state(OrderStates.choosing_date)

    await message.answer(
        "📅 Choose date:",
        reply_markup=get_data_dates()
    )


# ВЫБРАЛИ ДАТУ
@router.callback_query(OrderStates.choosing_date)
async def choose_date(
    callback: types.CallbackQuery,
    state: FSMContext
):
    date = callback.data.split(":",1)[1]

    # Сохраняем дату
    await state.update_data(date=date)

    # Переходим к выбору времени
    await state.set_state(OrderStates.choosing_time)

    await callback.message.answer(
        f"📅 You chose: {date}\n"
        f"🕐 Choose time:",
        reply_markup=get_time_keyboard()
    )

    await callback.answer()


# ВЫБРАЛИ ВРЕМЯ
@router.callback_query(OrderStates.choosing_time)
async def choose_time(
    callback: types.CallbackQuery,
    state: FSMContext
):
    time = callback.data.split(":",1)[1]

    # Сохраняем время
    await state.update_data(time=time)

    data = await state.get_data()

    await callback.message.answer(
        f"✅ Date and time selected:\n"
        f"📅 {data['date']}\n"
        f"🕐 {data['time']}"
    )

    await callback.answer()