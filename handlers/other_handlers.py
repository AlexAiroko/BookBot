from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message()
async def answer_other_message(message: Message):
	await message.answer("Я вас не понимаю.")