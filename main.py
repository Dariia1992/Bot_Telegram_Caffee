from aiogram import Bot, Dispatcher
import asyncio
import logging

import config
from handlers import commands, echo, menu_caffee, menu_bakery,menu_tea



TOKEN_API = config.TOKEN_TG

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_API)
dp = Dispatcher()


dp.include_router(commands.router)
dp.include_router(menu_caffee.router)
dp.include_router(menu_tea.router)
dp.include_router(menu_bakery.router)

# echo всегда последним
dp.include_router(echo.router)




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())