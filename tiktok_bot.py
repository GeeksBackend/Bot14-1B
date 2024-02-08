from aiogram import Bot, Dispatcher, types, executor
from config import token 
import requests, os, logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply(f"Привет {message.from_user.full_name}, отправь ссылку на тикток")

@dp.message_handler()
async def get_url_tiktok(message:types.Message):
    if 'tiktok.com' in message.text:
        await message.reply('Начинаю скачивать видео...')
    else:
        await message.reply('Я вас не понял, отправьте ссылку на видео тикток')

executor.start_polling(dp)