from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def again_keyboard(category: str):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔄 Ещё",
                    callback_data=category
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏠 Главное меню",
                    callback_data="menu"
                )
            ]
        ]
    )

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📜 Цитата",
                callback_data="quote"
            )
        ],
        [
            InlineKeyboardButton(
                text="💪 Мотивация",
                callback_data="motivation"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌅 Утро",
                callback_data="morning"
            ),
            InlineKeyboardButton(
                text="🌙 Вечер",
                callback_data="evening"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎯 Работа",
                callback_data="work"
            ),
            InlineKeyboardButton(
                text="❤️ Душа",
                callback_data="soul"
            )
        ],
[
            InlineKeyboardButton(
                text="👨 Мужские грёзы",
                callback_data="man"
            ),
            InlineKeyboardButton(
                text="👩 Совет подружки",
                callback_data="girl"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔔 Подписаться",
                callback_data="subscribe"
            ),
            InlineKeyboardButton(
                text="🔕 Отписаться",
                callback_data="unsubscribe"
            )
        ]
    ]
)