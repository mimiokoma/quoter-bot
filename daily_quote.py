from database import get_users
from services.ai import generate_text


async def send_daily_quote(bot):

    quote = await generate_text(
        "Создай красивую вдохновляющую цитату дня."
    )

    for user_id in get_users():

        try:
            await bot.send_message(
                user_id,
                f"📜 Цитата дня\n\n{quote}"
            )

        except Exception as e:
            print(f"Ошибка отправки пользователю {user_id}: {e}")