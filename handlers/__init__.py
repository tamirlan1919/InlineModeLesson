from aiogram import Router
from .add_movie import router as add_movie_router
router = Router()

router.include_routers(add_movie_router)
