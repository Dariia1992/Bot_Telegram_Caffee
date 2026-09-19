from aiogram.fsm.state import State, StatesGroup
#sostoyanie zakaza Сейчас пользователь находится на этапе выбора конкретного продукта

"""choosing_product
      ↓
choosing_size
      ↓
choosing_quantity
      ↓
confirming_order"""

class OrderStates(StatesGroup):
    choosing_product = State()
    choosing_size = State()
    choosing_quantity = State()
    confirming_order = State()