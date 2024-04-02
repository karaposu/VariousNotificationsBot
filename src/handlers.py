from aiogram.types import Message
import secrets
import logging
import backoff
import aiogram
from aiogram import Bot

from dotenv import load_dotenv
import os
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
# Configure logging at the beginning of your script
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


first_time= """This is variousnotificationsbot. My purpose is to be the generic notification interface for all telegram users. 
you have an app or you created an app and you want people to receive notifications through telegram. This is where I come in. 
1. Find and /start variousnotificationsbot in Telegram
2. Take the generated_token
3. Make Post request using the token and following format
curl -X POST http://104.197.79.151:8000/sendNotification -H "Content-Type: application/json" -d '{"message": "YourMessageHere", "apiKey": "generated_token_here"}'
For details and documentation please visit www.variousnotificationsbot.com
"""

async def send_ID(message: Message, ID):

    await message.answer(ID)

async def get_start(message: Message):
    logger.info(f"Received /start command from user {message.from_user.id}")
    try:
        user_id = message.from_user.id
        api_key, is_new_user = save_new_user_or_get_existing_key(user_id)

        if is_new_user:
            answer= first_time
            answer = "I created a unique token for you. This ID is all you need to streamline your notifications to me. Great notifications!\n"
        else:
            answer = "Welcome back! Here is your existing token for notifications.\n"

        await message.answer(answer)
        await send_ID(message, str(api_key))
        logger.info(f"Successfully handled /start command for user {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error handling /start command for user {message.from_user.id}: {e}", exc_info=True)

async def get_message(message: Message):
    await message.answer('You wrote me a text message')



from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
import secrets
from database_setup import User, APIKey, engine
def save_new_user_or_get_existing_key(telegram_id):
    session = Session(bind=engine)
    try:
        # Try to find the user by telegram_id
        user = session.query(User).filter(User.telegram_id == str(telegram_id)).one_or_none()

        if user:
            # If user exists, get their API key
            api_key = user.api_keys[0].api_key  # Assuming one API key per user for simplicity
            return api_key, False  # Return existing API key and False indicating user already existed
        else:
            # If user does not exist, create new user and API key
            generated_api_key = secrets.token_urlsafe(32)
            new_user = User(telegram_id=str(telegram_id))
            new_api_key = APIKey(api_key=generated_api_key, user=new_user)
            session.add(new_user)
            session.add(new_api_key)
            session.commit()
            return generated_api_key, True  # Return new API key and True indicating new user was created
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


from aiogram.types import Message
async def send_notification(message: Message, user_id, notification):

    await message.answer(notification)


@backoff.on_exception(backoff.expo,
                      aiogram.exceptions.TelegramNetworkError,
                      max_tries=5)
async def send_notification(user_id: int, notification: str):
    try:
        await bot.send_message(chat_id=user_id, text=notification)
    except Exception as e:
        print(f"Failed to send message to {user_id}: {e}")
        raise  # Reraising the exception is important for the retry mechanism to work


if __name__ == "__main__":
   import asyncio
   asyncio.run(send_notification(12345, "Your message here"))
