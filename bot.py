from telegram.ext import *
from dotenv import load_dotenv
import handler
import os

load_dotenv()
bot_token = str(os.environ.get("BOT_TOKEN"))
handler_list = ['help','add','delete','info','send','list','test']

updater = Updater(bot_token,use_context=True)
dp = updater.dispatcher

for i in handler_list:
    method = getattr(handler, i+'_command')
    dp.add_handler(CommandHandler(i,method))

updater.start_polling()
updater.idle()


