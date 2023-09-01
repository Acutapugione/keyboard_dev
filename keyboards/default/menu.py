from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

phone = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(
            text="Share your contact",
            request_contact=True
        )
    ]],
    resize_keyboard=True
)

geolocation = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(
            text="Share your geolocation",
            request_location=True
        )
    ]],
    resize_keyboard=True
)