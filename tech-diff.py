import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# CONFIGURATION

TOKEN = sys.argv[1]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# HANDLERS

async def warning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_thread_id = update.message.message_thread_id if update.message.message_thread_id else None
    response = "Estamos com problemas técnicos no momento. Tente novamente mais tarde."
    await context.bot.send_message(chat_id=update.message.chat_id, text=response, parse_mode='html', disable_web_page_preview=True, message_thread_id=message_thread_id)

# MAIN
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    warning_handler = CommandHandler(['start', 'help', 'roll', 'r', 'rf'], warning)
    application.add_handler(warning_handler)
    
    application.run_polling()
