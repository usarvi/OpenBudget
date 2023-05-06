import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import API_TOKEN

bot_token = API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    chat_id = message.chat.id

    url1 = "https://t.me/ochiqbudjetbot?start=00266224004"
    url = "https://openbudget.uz/boards-list/2/4bd4bb63-94de-4b8d-b983-8e1464ac104c"    
    html = '''\t1️⃣ Автомобиль йулининг тўлиқ манзили-\tЁмчи  қишлоғи йўллари\t🛣
    \t2️⃣ Йўлниниг умумий узунлиги (м) -\t <code>9300</code>🎢 
    \t3️⃣ Йўл пойининг умумий кенглиги (м)-\t <code>6</code>🎢
    \t4️⃣ Қатнов қисмининг умумий эни (м)-\t <code>6</code>🎢
    \t5️⃣ Таъмир-талаб қисми (м²) -\t <code>35520</code>🎢
    \t6️⃣ Таъмирланган йили - <code>None</code>
    \t7️⃣ Таъмирлаш учун талаб этилади-\t <code>1 500 000 000</code> so'm\t💸'''
    
    message = f"<b>Assalomu alaykum\nUshbu linkka kirib ovoz bering👇👇👇:</b>\n {url} {chat_id}\n<b>{html}</b>"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Ovoz berish", url=url1))

    await bot.send_message(chat_id, text=message, reply_markup=keyboard, parse_mode='HTML')

@dispatcher.message_handler()
async def echo(message: types.Message):
    url = "https://openbudget.uz/boards-list/2/4bd4bb63-94de-4b8d-b983-8e1464ac104c"  
    natija=f"Assalomu alaykum hurmatli hamshaharlik\nSiz {url} manzilga kirib ovoz bering"
    await message.answer(natija)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)