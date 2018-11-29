import time, datetime, os, requests
from os.path import join, dirname
from dotenv import load_dotenv
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.message.reply_text("I'm Article Collector Meeseeks! Share articles with me and I will collect and share them with the rest of the team!")

def help(bot, update):
    update.message.reply_text("Send me a link you consider interesting and I will take care of the rest.")

def collect(bot, update):
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    text = update.message.text

    if first_name is None:
        full_name = 'Unknown'
    elif last_name is None:
        full_name = first_name
    else:
        full_name = first_name + ' ' + last_name

    key = "https://"
    unwanted_extensions = ['jpg', 'jpeg', 'png']

    if key in text:
        pos = text.find(key)
        link = text[pos:].split(' ')[0]

        try:
            status = requests.get(link).status_code
        except requests.ConnectionError:
            status = 404

        if status == 200:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d %H:%M:%S')
            print('('+ st + ') ' + full_name + ' => ' + link)

            values = [
                [
                    st,
                    full_name,
                    "Chatbot can't read titles yet...",
                    link
                ],
            ]

            body = {
                'values': values
            }

            result = service.spreadsheets().values().append(
                spreadsheetId=os.getenv('SPREADSHEET_ID'), range=os.getenv('RANGE_NAME'),
                valueInputOption='USER_ENTERED', body=body).execute()

            print('{0} cells appended.'.format(result \
                                               .get('updates') \
                                               .get('updatedCells')))

            bot.send_message(chat_id=update.message.chat_id, text="Saving that for laterrr!")


def unknown(bot, update):
    update.message.reply_text("Existence is pain!")

def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', os.getenv('SHEETS_SCOPE'))
        creds = tools.run_flow(flow, store)

    global service
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    updater = Updater(token=os.getenv('BOT_TOKEN'))
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, collect))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
