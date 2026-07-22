from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.types import Message

from services.ai import generate_text
from keyboards import main_keyboard, again_keyboard

from users import users

from database import check_limit

import random
from aiogram.types import FSInputFile

from promt import CATEGORY_PROMPTS

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):

    await message.answer(
        "✨ Добро пожаловать в Quoter\n\n"
        "Выбери категорию вдохновения:",
        reply_markup=ReplyKeyboardRemove()
    )

    await message.answer(
        "👇 Главное меню",
        reply_markup=main_keyboard
    )

@router.callback_query(F.data == "menu")
async def menu(callback: CallbackQuery):

    await callback.message.answer(
        "✨ Главное меню",
        reply_markup=main_keyboard
    )

    await callback.answer()

# цитата
@router.callback_query(F.data == "quote")
async def quote(callback: CallbackQuery):

    # if not check_limit(callback.from_user.id):
    #     await callback.message.answer(
    #         "⛔ Сегодня лимит исчерпан.\n\n"
    #         "Доступно 3 генерации в сутки."
    #     )
    #
    #     return
    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["quote"]
    )

    await loading.delete()

    images = [
        "images/1.jpg",
        "images/4.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"📜 Цитата\n\n{result}",
        reply_markup=again_keyboard("quote")
    )

    await callback.answer()

#мотивация
@router.callback_query(F.data == "motivation")
async def motivation(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

        return

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["motivation"]
    )

    await loading.delete()

    images = [
        "images/6.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"💪 Мотивация\n\n{result}",
        reply_markup=again_keyboard("motivation")
    )

    await callback.answer()

#для души
@router.callback_query(F.data == "soul")
async def soul(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["soul"]
    )

    await loading.delete()

    images = [
        "images/3.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"❤️ Для души\n\n{result}",
        reply_markup=again_keyboard("soul")
    )

    await callback.answer()

#подруга
@router.callback_query(F.data == "girl")
async def girl(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["girl"]
    )

    await loading.delete()

    images = [
        "images/9.jpeg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"👩 Совет подружки\n\n{result}",
        reply_markup=again_keyboard("girl")
    )

    await callback.answer()

#мужик
@router.callback_query(F.data == "man")
async def man(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["man"]
    )

    await loading.delete()

    images = [
        "images/8.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"👨 Мужские грёзы\n\n{result}",
        reply_markup=again_keyboard("man")
    )

    await callback.answer()

#для работы
@router.callback_query(F.data == "work")
async def work(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["work"]
    )

    await loading.delete()

    images = [
        "images/3.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"🎯 Для работы\n\n{result}",
        reply_markup=again_keyboard("work")
    )

    await callback.answer()

#утро
@router.callback_query(F.data == "morning")
async def morning(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["morning"]
    )

    await loading.delete()

    images = [
        "images/2.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"🌅 Утро\n\n{result}",
        reply_markup=again_keyboard("morning")
    )

    await callback.answer()

#вечер
@router.callback_query(F.data == "evening")
async def evening(callback: CallbackQuery):

    if not check_limit(callback.from_user.id):
        await callback.message.answer(
            "⛔ Сегодня лимит исчерпан.\n\n"
            "Доступно 3 генерации в сутки."
        )

    loading = await callback.message.answer(
        "⏳ Подбираю вдохновение..."
    )

    result = await generate_text(
        CATEGORY_PROMPTS["evening"]
    )

    await loading.delete()

    images = [
        "images/5.jpg",
    ]

    photo = FSInputFile(
        random.choice(images)
    )

    await callback.message.answer_photo(
        photo=photo,
        caption=f"🌙 Вечер\n\n{result}",
        reply_markup=again_keyboard("evening")
    )

    await callback.answer()



# @router.message(F.text == "💪 Мотивация")
# async def motivation(message: CallbackQuery):
#
#     result = await generate_text(
#         "Сгенерируй короткое мотивационное сообщение."
#     )
#     await message.answer(result)
#
#
# @router.message(F.text == "🌅 Утро")
# async def morning(message: CallbackQuery):
#     result = await generate_text(
#         "Напиши доброе вдохновляющее утреннее сообщение."
#     )
#     await message.answer(result)
#
#
# @router.message(F.text == "🌙 Вечер")
# async def evening(message: CallbackQuery):
#     result = await generate_text(
#         "Напиши спокойную вечернюю мудрую мысль."
#     )
#     await message.answer(result)
#
#
# @router.message(F.text == "🎯 Для работы")
# async def work(message: CallbackQuery):
#     result = await generate_text(
#         "Напиши мотивационную мысль для продуктивной работы."
#     )
#     await message.answer(result)
#
#
# @router.message(F.text == "❤️ Для души")
# async def soul(message: CallbackQuery):
#     result = await generate_text(
#         "Напиши тёплую жизненную цитату для души."
#     )
#     await message.answer(result)

@router.callback_query(F.data == "subscribe")
async def subscribe(message: CallbackQuery):
    from database import add_user

    add_user(message.from_user.id)

    await message.answer(
        "✅ Теперь я буду присылать тебе ежедневную цитату."
    )

@router.callback_query(F.data == "unsubscribe")
async def unsubscribe(message: CallbackQuery):
    from database import remove_user

    remove_user(message.from_user.id)

    await message.answer(
        "❌ Ежедневные цитаты отключены."
    )