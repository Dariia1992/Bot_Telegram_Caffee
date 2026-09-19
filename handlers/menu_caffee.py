from aiogram import Router, types, F
from keyboards.keyboard_inline import get_coffee_keyboard, get_size_keyboard, get_quantity_keyboard,get_confirm_keyboard
router = Router()
from aiogram.fsm.context import FSMContext #Это «память текущего заказа конкретного пользователя».
from states.order import OrderStates


#coffee
@router.message(F.text == "☕ Coffee")
async def coffee_menu(message: types.Message, state: FSMContext):
    await state.set_state(OrderStates.choosing_product)
    
    await message.answer(
        "☕ Choose your coffee:",
        reply_markup=get_coffee_keyboard()
    )
    
    
@router.callback_query(OrderStates.choosing_product) # ловит нажатие на inline-кнопку.
async def choose_coffee(callback: types.CallbackQuery,state: FSMContext): # объект с информацией о том, какую кнопку нажали.
    await state.update_data(product=callback.data)
    await state.set_state(OrderStates.choosing_size)
    await callback.message.answer("Choose size:",reply_markup=get_size_keyboard())


    
    data = await state.get_data()
    print(data)
    
    
@router.callback_query(OrderStates.choosing_size)
async def choose_size(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(size=callback.data)
    await state.set_state(OrderStates.choosing_quantity)
    await callback.message.answer(
    "Choose quantity:",
    reply_markup=get_quantity_keyboard()
)
    
@router.callback_query(OrderStates.choosing_quantity)
async def choose_quantity(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(quantity=callback.data)
    await state.set_state(OrderStates.confirming_order)
    
    data = await state.get_data()
    product = data["product"]
    size = data["size"]
    quantity = data["quantity"]
    
    await callback.message.answer(
    f"☕ Your order:\n"
    f"Coffee: {product}\n"
    f"Size: {size}\n"
    f"Quantity: {quantity}", reply_markup=get_confirm_keyboard()
)


# CONFIRM ORDER
@router.callback_query(
    OrderStates.confirming_order,
    F.data == "confirm"
)
async def confirm_order(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("✅ Order confirmed! Thank you! ☕")
    await state.clear()
    await callback.answer()


# CANCEL ORDER
@router.callback_query(
    OrderStates.confirming_order,
    F.data == "cancel"
)
async def cancel_order(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("❌ Order cancelled.")
    await state.clear()
    await callback.answer()
    
    
    



