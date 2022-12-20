from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("School 152 ✈"), KeyboardButton("Test || Тест")],
            [KeyboardButton("Bog'lanish 📲"), KeyboardButton("𝐔𝐧𝐢𝐒𝐭𝐮𝐝𝐲")],
        ]
    elif tip == "ha":
        bts = [
            [KeyboardButton("HA || ДА")],
            [KeyboardButton("Orqaga🔙")],
        ]
    elif tip == "baho":
        bts = [
            [KeyboardButton("Juda zo‘r 🌟")],
            [KeyboardButton("Yaxshi 👍")],
            [KeyboardButton("Kamchiliklar bor 📚")],
            [KeyboardButton("Menga yoqmadi 👎")],
            [KeyboardButton("Orqaga🔙")],
        ]
    elif tip == "fan":
        bts = [
            [KeyboardButton("📚 Biologiya Uzb 📚"), KeyboardButton("📚 Fizika Uzb 📚")],
            [KeyboardButton("📚 Biologiya Rus 📚"), KeyboardButton("📚 Ona tili 📚")],
            [KeyboardButton("📚 English  📚"), KeyboardButton("📚 Matematika Uzb 📚")],
            [KeyboardButton("👍 Botni baholang 👍"), KeyboardButton("Orqaga🔙")],
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "call":
        btn = [
            [InlineKeyboardButton("Bog'lanish Uchun ", url="https://link-to-tel.herokuapp.com/tel/"
                                                           "+998(99)855-74-03")],
        ]
    # elif btn_type == "fikir":
    #     btn = [
    #         [InlineKeyboardButton("Chatga o'tish", url="https://t.me/chat_school255")]
    #     ]
    elif btn_type == "unistudy":
        btn = [
            [InlineKeyboardButton("Welkin Group", url="https://t.me/Welkin_GR")],
        ]
    elif btn_type == "humo":
        btn = [
            [InlineKeyboardButton("Bog'lanish Uchun", url="https://t.me/Welkin_Manager")],
        ]
    else:
        btn = [
            [InlineKeyboardButton("Saytga tashrif ✈", callback_data="sayt", url="https://maktab-152.uz/"),
             InlineKeyboardButton("Kanal📱", callback_data="kan", url="https://t.me/yashnobod152maktab")],
        ]

    return InlineKeyboardMarkup(btn)


try:
    create_table()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        a = update.message.from_user.first_name
        print(a)
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text("<b>Assalomu Alekum || Привет</b> {}  😁 \n\n<b>School 152 </b> botiga tashrif "
                              "uchun rahmat 🤝 \nSiz botni kezish davomida ko'proq malumot olasiz.\n\n"
                              "O'zingizga kerakli bo'lga bo'limni tanlang👇🏻 \n\n__________________\n\nБлагодарим "
                              "вас за "
                              "посещение бота <b>School 152 </b> 🤝 \n\nВы получите дополнительную "
                              "информацию по"
                              "мере просмотра бота.\n\nВыберите нужный раздел👇🏻 "
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


def message_handler(update, context):
    user = update.message.from_user
    msg = update.message.text
    if msg == "School 152 ✈":
        update.message.reply_text("Saytga tashrif buyursangiz ko'proq malumotlarga ega bo'lasiz va bizning. \n \n "
                                  "𝐊𝐚𝐧𝐚𝐥𝐠𝐚 ham ❗️𝐎𝐛𝐮𝐧𝐚 bo'lib qo'ysangiz Hursand bo'lamiz.",
                                  reply_markup=inline_btn("btn"), parse_mode="HTML")

    # bog'lanish
    elif msg == "Bog'lanish 📲":
        update.message.reply_text("Maktab <b>administratsiasi</b> bilan bog'lanish uchun shu \n<b>(Bog'lanish "
                                  "Uchun)</b> \n\n "
                                  "❗️Malum Sabablarga ko'ra aloqa yozib olinishi mumkin...",
                                  reply_markup=inline_btn("call"), parse_mode="HTML")

    # HUMO bilan ishlanga qisim
    elif msg == "𝐔𝐧𝐢𝐒𝐭𝐮𝐝𝐲":
        update.message.bot.send_video(chat_id=update.message.chat_id, video=open('video.mp4', 'rb'),
                                      supports_streaming=True, caption="🇺🇿UniStudy nima va qanday vazifasi bor tez "
                                                                       "kunda buni sizga taqdim etamzi va ancha katta "
                                                                       "foydasi bor bo'lishi mumkin... \n\n🇷🇺Что такое "
                                                                       "UniStudy и какова его функция... \n\n Cледуй "
                                                                       "сюда👇🏻", reply_markup=inline_btn("unistudy"),
                                      parse_mode="HTML")

    elif msg == "Test || Тест":
        update.message.reply_text("Testda o'z bilimingizni tekshirishingiz mumkin agar tayyor bo'lsangiz <b>(HA)</b> "
                                  "tugmasini bosing😃 \n\nВы можете проверить свои знания в тесте, если готовы, "
                                  "нажмите кнопку <b>(ДА)</b>😃",
                                  reply_markup=btns("ha"), parse_mode="HTML")

    # orqaga Back bilan ishlanga qisim
    elif msg == "Orqaga🔙":
        update.message.reply_text("Tashrif uchun rahmat 😃", reply_markup=btns("menu"))

    elif msg == "HA || ДА":
        update.message.reply_photo(photo=open("Test.png", "rb"),
                                   caption="👋🏻 Salom do'stim ! Siz o'zingizga kerakli fandan test yechishga "
                                           "tayyormisiz🤔\n\n Unda test yechishni boshlang ... \n\n O'zingizga kerakli "
                                           "bo'limni tanlang...👇🏻",
                                   reply_markup=btns("fan"))

    # botni baholash qismi
    elif msg == "Juda zo‘r 🌟":
        update.message.reply_text("Rahmat ☺️")

    elif msg == "Yaxshi 👍":
        update.message.reply_text("Rahmat 👍")

    elif msg == "Kamchiliklar bor 📚":
        update.message.reply_text("Kamchiliklarni ko'rib chiqamiz 😊")

    elif msg == "Menga yoqmadi 👎":
        update.message.reply_text("Baho uchun tashakkur🙂")

    elif msg == "👍 Botni baholang 👍":
        update.message.reply_text("Marhamat botimizni baholang !!!\n\n Rahmat !!!", reply_markup=btns("baho"))

    # Test ishlash qismi

    # elif msg == "📚 DTM majburiy fanlardan testlar 📚":
    #     update.message.reply_photo(document=open("dtmtest.pdf", "rb"),
    #                                caption="TEST. Asosiy va Majburiy fanlar \n Ona tili va Adabiyot \nTarix\nIngliz "
    #                                        "tili\nRus tili\nMatematika\nFizika\nBiologiya\nKimyo\nGeografiya\n"
    #                                        "\nUzizga kerakli fanlardan testlarni yeching",
    #                                reply_markup=btns("fan"))

    elif msg == "📚 Biologiya Uzb 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('Biologiya.uz.pdf', 'rb'), filename='Biologiya.pdf',
                                  caption="DTM dan olingan 😊")

    elif msg == "📚 Biologiya Rus 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('Biologiya_ru.uz.pdf', 'rb'), filename='Biologiya.pdf',
                                  caption="DTM dan olingan 😊")

    elif msg == "📚 Fizika Uzb 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('Fizika_ru.uz.pdf', 'rb'), filename='Fizika_ru.uz.pdf',
                                  caption="DTM dan olingan 😊")

    elif msg == "📚 Ona tili 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('Ona tili.uz.pdf', 'rb'), filename='Ona tili.uz.pdf',
                                  caption="DTM dan olingan 😊")

    elif msg == "📚 Matematika Uzb 📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('Matematika.uz.pdf', 'rb'), filename='Matematika.uz'
                                                                                                      '.pdf',
                                  caption="DTM dan olingan 😊")

    elif msg == "📚 English  📚":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open('Ingliz tili.uz.pdf', 'rb'), filename='Ingliz'
                                                                                                       'tili.uz.pdf',
                                  caption="DTM dan olingan 😊")


def main():
    Token = "5640282842:AAE0tXXLMvNVPGLeCado39k9a3c89avv6Qs"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    # updater.dispatcher.add_handler(CallbackQueryHandler(send_document))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
