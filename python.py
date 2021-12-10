import os
import telebot

bot = telebot.TeleBOT("API Key Here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message,"Hello! I'm YS Bro Chat Bot")
  
@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message, "  https://t.me/sinhalasubgroup")
  
  bot.polling()


