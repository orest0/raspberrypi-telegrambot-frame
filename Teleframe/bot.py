import os
from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'
PHOTO_FOLDER = '/home/pi/raspberrypi-telegrambot-frame/Teleframe/photos'

def handle_images(update, context):
    message = update.message
    chat_id = message.chat_id

    # Check if the message contains a photo
    if message.photo:
        # Get the photo file ID
        file_id = message.photo[-1].file_id

        # Get information about the photo
        photo_info = context.bot.get_file(file_id)

        # Download the photo
        # photo_path = photo_info.download()
        photo_path = os.path.join(PHOTO_FOLDER,f"{file_id}.jpg")
        photo_info.download(photo_path)

        # Reply to the user
        context.bot.send_message(chat_id, f"Photo is sent to a PhotoFrame")
        context.bot.send_message(chat_id, f"Check it now")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Create a message handler for images
    image_handler = MessageHandler(Filters.photo, handle_images)
    dp.add_handler(image_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
