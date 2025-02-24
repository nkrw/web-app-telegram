from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram import Dispatcher

async def shop_button_handler(message: types.Message):
    # Créer un bouton "Ouvrir la boutique" pour ouvrir la Mini App
    web_app_button = InlineKeyboardButton(
    text="Ouvrir la boutique",
    web_app=WebAppInfo(url="https://nkrw.github.io/web-app-telegram/")  # Remplace par une URL valide
)


    # Ajouter le bouton au clavier (assurer qu'il est dans une liste)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])

    # Envoie un message avec le bouton
    await message.answer("Cliquez sur le bouton pour ouvrir la boutique :", reply_markup=keyboard)

def register_handlers(dp: Dispatcher):
    dp.message.register(shop_button_handler, Command("start"))
