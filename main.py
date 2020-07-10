import telepot

TOKEN = "xxxx"
up_id = "649179764+1" #update id

telegram_bot = telepot.Bot(TOKEN)
print(telegram_bot.getMe())
telegram_bot.getUpdates(up_id)