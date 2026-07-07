from database import get_users
from services.ai import generate_text
from keyboards import main_keyboard
from promt import CATEGORY_PROMPTS

CHANNEL_ID = "@channel7mimi"


async def send_daily_quote(bot):
    quote = await generate_text(
        CATEGORY_PROMPTS["motivation"] | CATEGORY_PROMPTS["soul"] | CATEGORY_PROMPTS["morning"]
    )

    # канал
    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"Вам послание 💫\n\n{quote}"
        )
    except Exception as e:
        print(f"Ошибка канала: {e}")

    # пользователи
    for user_id in get_users():
        print(get_users())
        try:
            await bot.send_message(
                user_id,
                "✨ Твоё ежедневное вдохновение ждёт.\n\nВыбери настроение:",
                reply_markup=main_keyboard
            )

        except Exception as e:
            print(
                f"Ошибка отправки пользователю {user_id}: {e}"
            )