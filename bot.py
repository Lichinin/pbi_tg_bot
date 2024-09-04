import os

import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.utils.keyboard import InlineKeyboardBuilder
load_dotenv()


class Aiobot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Aiobot, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher()
        self.dp.message.register(self.cmd_start, Command("start"))
        self.dp.message.register(self.cmd_random, Command("random"))
        self.session = aiohttp.ClientSession()

    async def cmd_start(self, message: types.Message):
        await message.answer("Hedddllo!")

    async def send_message(self, text):
        async with self.session:
            await self.bot.send_message(chat_id=self.chat_id, text=text)

    async def cmd_random(self, message: types.Message):
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text='Нажми кнопку эту',
            callback_data='random_value'
        ))
        await message.answer(
            'бла бла бла',
            reply_markup=builder.as_markup()
        )

    async def run_bot(self):
        await self.dp.start_polling(self.bot)
