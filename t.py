import bot
from secret import username, password
bot = bot.GladiatusBot(username, password)
bot.login()
bot.switchTab()
bot.trainer()
bot.gainPower()