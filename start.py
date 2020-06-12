from vkbottle import Bot, Message
import config
import base64
import codecs

bot = Bot(config.TOKEN)


@bot.on.message_handler(text =  ["/en64 <text>", "!en64 <text>"])
async def encode(mes: Message, text):
    try:
        text = text.encode("UTF_8")
        text = base64.b64encode(text)
        text = text.decode("UTF-8")
        await mes('Ваш результат: ')
        await mes(text)
    except:
        await mes("Произошла неизвестная ошибка")

@bot.on.message_handler(text =  ["/de64 <text>", "!de64 <text>"])
async def decode(mes: Message, text):
    try:
        text = text.encode("UTF_8")
        text = base64.b64decode(text)
        text = text.decode("UTF-8")
        await mes('Ваш результат: ')
        await mes(text)
    except:
        await mes("Произошла неизвестная ошибка! (часто расшифровывают не зашифрованный текст)")

@bot.on.message_handler(text = ["/rot13 <text>", "!rot13 <text>"])
async def rot13(mes: Message, text):
    text = codecs.decode(text, 'rot_13')
    await mes('Ваш результат: ')
    await mes(text)

bot.run_polling(skip_updates=False)