# coding: utf-8

# uvicorn main:app --reload --host 0.0.0.0 --port 8000
# uvicorn nain:app --reload --host 0.0.0.0

import asyncio
from fastapi import FastAPI

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from handlers import get_start, get_message
from apis.default_api import router as DefaultApiRouter
import uvicorn
import logging

from dotenv import load_dotenv
import os
load_dotenv()
# Load the .env file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
database_url = os.getenv('DATABASE_URL')

# aiogram 3.5.0
# from aiogram.types import DefaultBotProperties
# default_properties = DefaultBotProperties(parse_mode='HTML')
# bot = Bot(BOT_TOKEN, default=default_properties)

bot = Bot(BOT_TOKEN, parse_mode='HTML')
bot_task = None

async def lifespan(app: FastAPI):
    global bot_task
    try:
        logger.info("Starting bot task")
        loop = asyncio.get_running_loop()
        bot_task = loop.create_task(start_bot())
        yield
    finally:
        if bot_task:
            logger.info("Canceling bot task")
            bot_task.cancel()
            try:
                await bot_task
            except asyncio.CancelledError:
                logger.info("Bot task canceled")
        logger.info("Shutting down application")


app = FastAPI(lifespan=lifespan)
dispatcher = Dispatcher()

app.include_router(DefaultApiRouter)

async def start_bot():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Registration of event handlers
    dispatcher.message.register(get_start, Command(commands=['start']))
    dispatcher.message.register(get_message, F.text)

    # This will start the bot
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

