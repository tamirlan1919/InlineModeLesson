from aiogram import Router, F
from aiogram.types import Message
from database.crud import insert_to_movie
router = Router()

@router.message(F.text.startswith('/add_movie'))
async def add_movie_handler(message: Message):
    data = message.text.replace('/add_movie', '')
    parts = data.split('|', 3)

    if len(parts) != 3:
        await message.answer('Неправильно используйте шаблон /add_movie Название | Описание | Фото URL')

    title, description, photo_url = parts[0], parts[1], parts[2]
    insert_to_movie(title=title, description=description, photo_url=photo_url)
    await message.answer('Фильм успешно добавлен')


    