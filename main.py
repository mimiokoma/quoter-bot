import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.messages import router

from scheduler import scheduler
from daily_quote import send_daily_quote

async def main():

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(router)

    scheduler.add_job(
        send_daily_quote,
        "cron",
        hour=9,
        minute=0,
        kwargs={"bot": bot}
    )

    scheduler.start()


    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())