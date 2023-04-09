import os
import telebot

# 从环境变量中获取 Telegram Bot 的 token
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# 创建一个 TeleBot 对象
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, '发送 /id 获取id')


@bot.message_handler(commands=['id'])
def id(message):
  chat_id = message.chat.id
  bot.send_message(message.chat.id, f'{chat_id}')

# 启动机器人
bot.polling()
