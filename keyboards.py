from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Цитата"),
            KeyboardButton(text="💪 Мотивация")
        ],
        [
            KeyboardButton(text="🌅 Утро"),
            KeyboardButton(text="🌙 Вечер")
        ],
        [
            KeyboardButton(text="🎯 Для работы"),
            KeyboardButton(text="❤️ Для души")
        ]
    ],
    resize_keyboard=True
)