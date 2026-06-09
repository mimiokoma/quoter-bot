from users import users
from services.ai import generate_text

from database import get_users
for user_id in get_users():

    async def send_daily_quote(bot):

        quote = await generate_text(
            "Создай красивую вдохновляющую цитату дня."
        )

        for user_id in users:

            try:
                await bot.send_message(
                    user_id,
                    f"📜 Цитата дня\n\n{quote}"
                )

            except:
                pass