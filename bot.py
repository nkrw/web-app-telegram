import logging
from aiogram.client.default import DefaultBotProperties
import config
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from aiogram.filters import Command

from config import TOKEN, WEBHOOK_URL, ADMIN_ID_LIST
from db import create_db_and_tables
from handlers.user.shop_button import register_handlers  # Import du handler

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# Initialisation du bot et des webhooks
async def on_startup(bot: Bot):
    await create_db_and_tables()
    await bot.set_webhook(WEBHOOK_URL)
    for admin in ADMIN_ID_LIST:
        try:
            await bot.send_message(admin, 'Bot on ✅"')
        except Exception as e:
            logging.warning(e)


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')

def main() -> None:
    register_handlers(dp)  # Enregistre le handler pour le bouton Shop
    dp.startup.register(on_startup)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_requests_handler.register(app, path=config.WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.WEBAPP_HOST, port=config.WEBAPP_PORT)
