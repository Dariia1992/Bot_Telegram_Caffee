from aiogram.fsm.state import State, StatesGroup


class OrderStates(StatesGroup):

    # DATE / TIME
    choosing_date = State()
    choosing_time = State()

    # COFFEE
    choosing_coffee = State()
    choosing_coffee_size = State()
    choosing_coffee_quantity = State()

    # TEA
    choosing_tea = State()
    choosing_tea_size = State()
    choosing_tea_quantity = State()

    # BAKERY
    choosing_bakery = State()
    choosing_bakery_size = State()
    choosing_bakery_quantity = State()

    # FINAL
    confirming_order = State()