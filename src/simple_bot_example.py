from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = ""
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when the command /start is issued."""
    await update.message.reply_text('Hi! Your API Key generation script will go here.')

def main() -> None:

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.run_polling()

if __name__ == '__main__':
    main()
