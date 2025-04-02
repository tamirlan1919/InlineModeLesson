from aiogram import Router
from .add_movie import router as add_movie_router
from .inline_handler import router as inline_router 
router = Router()

router.include_routers(add_movie_router, inline_router)
