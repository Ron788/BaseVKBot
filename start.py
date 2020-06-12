from vkbottle import Bot, Message
import config
import base64

bot = Bot(config.TOKEN)


@bot.on.message_handler(text =  ["/en64 <text>", "!en64 <text>"])
async def encode(mes: Message, text):
    try:
        text = text.encode("UTF_8")
        text = base64.b64encode(text)
        text = text.decode("UTF-8")
        await mes('Ваш результат: ' + text)
    except:
        await mes("Произошла неизвестная ошибка")

@bot.on.message_handler(text =  ["/de64 <text1>", "!de64 <text1>"])
async def decode(mes: Message, text1):
    try:
        text1 = text1.encode("UTF_8")
        text1 = base64.b64decode(text1)
        text1 = text1.decode("UTF-8")
        await mes('Ваш результат: ' + text1)
    except:
        await mes("Произошла неизвестная ошибка! (часто расшифровывают не зашифрованный текст)")

bot.run_polling(skip_updates=False)