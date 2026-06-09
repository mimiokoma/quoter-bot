from database import get_users
from services.ai import generate_text

CHANNEL_ID = "@channel7mimi"


async def send_daily_quote(bot):

    quote = await generate_text(
        "Создай красивую вдохновляющую цитату дня."
    )

    # канал
    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"📜 Цитата дня\n\n{quote}"
        )
        print("Цитата отправлена в канал")
    except Exception as e:
        print(f"Ошибка канала: {e}")

    # пользователи
    for user_id in get_users():

        try:
            await bot.send_message(
                user_id,
                f"📜 Цитата дня\n\n{quote}"
            )

        except Exception as e:
            print(
                f"Ошибка отправки пользователю {user_id}: {e}"
            )