import logging
from telegram import Update,InlineQueryResultArticle,InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,InlineQueryHandler,MessageHandler,filters

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text="therr is not any help way")
async def aine(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
	text_caps = ' '.join(context.args).upper()
	await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def inline_caps(update:Update,context:ContextTypes.DEFAULT_TYPE):
	query=update.inline_query.query
	if not query:
		return
	results=[]
	results.append(
		InlineQueryResultArticle(
			id=query.upper(),
			title='Caps',
			input_message_content=InputTextMessageContent(query.upper())
		)
	)
	await context.bot.answer_inline_query(update.inline_query.id,results)

if __name__ == '__main__':
	application = ApplicationBuilder().token('6275465742:AAEYMZz-2Sl7RUueqxyLc47olJJnI9A5FxU').build()

	start_handler = CommandHandler('start', start)
	help_handler=CommandHandler('help',help)
	message_handler=MessageHandler(filters.TEXT,aine)
	caps_handler = CommandHandler('caps', caps)
	inline_caps_handler=InlineQueryHandler(inline_caps)

	application.add_handler(start_handler)
	application.add_handler(help_handler)
	application.add_handler(message_handler)
	application.add_handler(caps_handler)
	application.add_handler(inline_caps_handler)

	application.run_polling()


    #'6275465742:AAEYMZz-2Sl7RUueqxyLc47olJJnI9A5FxU'