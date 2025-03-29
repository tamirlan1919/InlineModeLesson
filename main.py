from config import TOKEN
from aiogram import Bot, Dispatcher
import asyncio
import logging
from handlers import router
from database.models import make_table_movie

async def main():
    logging.basicConfig(level=logging.INFO)
    make_table_movie()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())