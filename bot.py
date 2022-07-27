import requests
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters


def get_Download_URL_From_API(url):
    API_URL = "https://youtube-video-info.p.rapidapi.com/video_formats"
    querystring = {"video":"edPREMPZ5RA"}

    headers = {
	"X-RapidAPI-Host": "youtube-video-info.p.rapidapi.com",
	"X-RapidAPI-Key": "747d1ec801msh1b8fd112fe516d8p1b3059jsnc4b6ad53bb89" # This is your API Token, keep it secret
}

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    return data['streams'][0]['url']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Welcome to URL downloader!\nPlease provide a valid url')


def textHandler(update: Update, context: CallbackContext) -> None:
    user_message = str(update.message.text)

    if update.message.parse_entities(types=MessageEntity.URL):
        download_url = get_Download_URL_From_API(user_message)
        update.message.reply_text(text=f'Your download url is: {download_url}')



def main():
    TOKEN = "YOUR BOT TOKEN"
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, textHandler, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()