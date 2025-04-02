from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultPhoto
from uuid import uuid4
import requests

from database.crud import get_movie_by_title

router = Router()

def is_valid_image_url(url: str) -> bool:
    try:
        response = requests.head(url, timeout=3)
        return response.status_code == 200 and 'image' in response.headers.get('Content-Type', '')
    except:
        return False

@router.inline_query()
async def inline_query_handler(inline_query: InlineQuery):
    query_text = inline_query.query.strip()
    rows = get_movie_by_title(query_text)
    results = []

    for row in rows:
        title = row[0]
        description = row[1]
        photo_url = row[2]

        if not photo_url or not is_valid_image_url(photo_url):
            continue

        result = InlineQueryResultPhoto(
            id=str(uuid4()),
            photo_url=photo_url,
            thumbnail_url=photo_url,
            caption=f"<b>{title}</b>\n\n{description}",
            parse_mode="HTML"
        )
        results.append(result)

    await inline_query.answer(results, cache_time=1)
