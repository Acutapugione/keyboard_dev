from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Button first",
                callback_data="second",
            ),
        ]
    ]
)
