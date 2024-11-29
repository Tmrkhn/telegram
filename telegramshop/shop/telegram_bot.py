from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.conf import settings
from shop.models import Product 

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def list_products(update: Update, context: CallbackContext) -> None:
    products = Product.objects.all()
    product_list = "\n".join([f"{product.name} - {product.price}" for product in products])
    update.message.reply_text(product_list)

def main():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("list_products", list_products))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
