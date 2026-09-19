from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.keyboard_inline import (
    get_tea_keyboard,
    get_size_keyboard,
    get_quantity_keyboard,
    get_confirm_keyboard
)

from states.order import OrderStates


router = Router()


# TEA MENU
@router.message(F.text == "🍵 Tea")
async def tea_menu(message: types.Message, state: FSMContext):
    # Начинаем новый заказ
    await state.set_state(OrderStates.choosing_product)

    await message.answer(
        "🍵 Choose your tea:",
        reply_markup=get_tea_keyboard()
    )


# CHOOSE TEA
@router.callback_query(OrderStates.choosing_product)
async def choose_tea(
    callback: types.CallbackQuery,
    state: FSMContext
):
    # Сохраняем выбранный чай
    await state.update_data(product=callback.data)

    # Переходим к выбору размера
    await state.set_state(OrderStates.choosing_size)

    await callback.message.answer(
        "Choose size:",
        reply_markup=get_size_keyboard()
    )

    await callback.answer()


# CHOOSE SIZE
@router.callback_query(OrderStates.choosing_size)
async def choose_size(
    callback: types.CallbackQuery,
    state: FSMContext
):
    # Сохраняем размер
    await state.update_data(size=callback.data)

    # Переходим к количеству
    await state.set_state(OrderStates.choosing_quantity)

    await callback.message.answer(
        "Choose quantity:",
        reply_markup=get_quantity_keyboard()
    )

    await callback.answer()


# CHOOSE QUANTITY
@router.callback_query(OrderStates.choosing_quantity)
async def choose_quantity(
    callback: types.CallbackQuery,
    state: FSMContext
):
    # Сохраняем количество
    await state.update_data(quantity=callback.data)

    # Переходим к подтверждению
    await state.set_state(OrderStates.confirming_order)

    # Получаем данные заказа
    data = await state.get_data()

    product = data["product"]
    size = data["size"]
    quantity = data["quantity"]

    await callback.message.answer(
        f"🍵 Your order:\n"
        f"Tea: {product}\n"
        f"Size: {size}\n"
        f"Quantity: {quantity}",
        reply_markup=get_confirm_keyboard()
    )

    await callback.answer()


# CONFIRM ORDER
@router.callback_query(
    OrderStates.confirming_order,
    F.data == "confirm"
)
async def confirm_order(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await callback.message.answer(
        "✅ Order confirmed! Thank you! 🍵"
    )

    await state.clear()
    await callback.answer()


# CANCEL ORDER
@router.callback_query(
    OrderStates.confirming_order,
    F.data == "cancel"
)
async def cancel_order(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await callback.message.answer(
        "❌ Order cancelled."
    )

    await state.clear()
    await callback.answer()