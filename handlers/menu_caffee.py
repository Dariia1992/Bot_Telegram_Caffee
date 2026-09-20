from aiogram import Router, types, F
from keyboards.keyboard_inline import get_coffee_keyboard, get_size_keyboard, get_quantity_keyboard,get_confirm_keyboard
router = Router()
from aiogram.fsm.context import FSMContext #Это «память текущего заказа конкретного пользователя».
from states.order import OrderStates




"""router.message     → ловим сообщение
F.text             → смотрим его текст
== "☕ Coffee"      → текст должен быть таким
message            → получаем само сообщение"""


#coffee
@router.message(F.text == "☕ Coffee")# «Если пользователь прислал текст ☕ Coffee — запускай функцию ниже».
async def coffee_menu(message: types.Message, state: FSMContext):#Создаём функцию. message — сообщение пользователя, state — память его заказа.
    await state.set_state(OrderStates.choosing_product)#Теперь пользователь находится на этапе выбора продукта»
    
    await message.answer(#Бот отправляет сообщение пользователю.
        "☕ Choose your coffee:",#Текст сообщения.
        reply_markup=get_coffee_keyboard()#К сообщению прикрепляется клавиатура.
    )
    
"""callback_query          → ловим inline-кнопку
choosing_size           → только на этом этапе
callback                → информация о нажатой кнопке
state                   → доступ к памяти FSM"""
@router.callback_query(OrderStates.choosing_product) # «Если пользователь сейчас находится на этапе choosing_product и нажал inline-кнопку — запускай функцию ниже».
async def choose_coffee(callback: types.CallbackQuery,state: FSMContext): # объект с информацией о том, какую кнопку нажали.
    await state.update_data(product=callback.data)#«Запомни выбранный продукт»
    await state.set_state(OrderStates.choosing_size)#Переключаем этап:
    await callback.message.answer("Choose size:",reply_markup=get_size_keyboard())#бот отвечает сообщением после нажатия на inline-"Choose size:" → пишет:Choose size:


    
    data = await state.get_data()#Возьми всё, что сейчас сохранено в FSM, и положи в переменную data».
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
    
    
    



"""# записать
await state.update_data(size=callback.data)

# поменять этап
await state.set_state(OrderStates.choosing_quantity)

# достать
data = await state.get_data()

update_data → записать
set_state   → перейти
get_data    → достать
"""