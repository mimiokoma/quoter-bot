from aiogram import Router, F
from aiogram.types import Message

from services.ai import generate_text
from keyboards import main_keyboard

from users import users

router = Router()


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "✨ Добро пожаловать в Quoter\n\n"
        "Я создаю уникальные цитаты и мотивационные сообщения с помощью ИИ.",
        reply_markup=main_keyboard
    )


@router.message(F.text == "📜 Цитата")
async def quote(message: Message):
    result = await generate_text(
        "Сгенерируй красивую философскую цитату. До 2 предложений."
    )
    await message.answer(result)


@router.message(F.text == "💪 Мотивация")
async def motivation(message: Message):
    result = await generate_text(
        "Сгенерируй короткое мотивационное сообщение."
    )
    await message.answer(result)


@router.message(F.text == "🌅 Утро")
async def morning(message: Message):
    result = await generate_text(
        "Напиши доброе вдохновляющее утреннее сообщение."
    )
    await message.answer(result)


@router.message(F.text == "🌙 Вечер")
async def evening(message: Message):
    result = await generate_text(
        "Напиши спокойную вечернюю мудрую мысль."
    )
    await message.answer(result)


@router.message(F.text == "🎯 Для работы")
async def work(message: Message):
    result = await generate_text(
        "Напиши мотивационную мысль для продуктивной работы."
    )
    await message.answer(result)


@router.message(F.text == "❤️ Для души")
async def soul(message: Message):
    result = await generate_text(
        "Напиши тёплую жизненную цитату для души."
    )
    await message.answer(result)

@router.message(F.text == "🔔 Подписаться")
async def subscribe(message: Message):
    from database import add_user

    add_user(message.from_user.id)

    await message.answer(
        "✅ Теперь я буду присылать тебе ежедневную цитату."
    )

@router.message(F.text == "🔕 Отписаться")
async def unsubscribe(message: Message):
    from database import remove_user

    remove_user(message.from_user.id)

    await message.answer(
        "❌ Ежедневные цитаты отключены."
    )