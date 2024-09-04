from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
from dotenv import load_dotenv
import os
load_dotenv()


class MyBot:
    def __init__(self):
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.updater = Updater(self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

    def start(self, update, context):
        user = update.effective_user
        update.message.reply_text("!!!!!и!")

    def pbi_error(self, message, update: Update, context=CallbackContext):
        update.message.reply_text(f"{message}!!!!!и!")

    def echo(update, context):
        update.message.reply_text(update.message.text)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
