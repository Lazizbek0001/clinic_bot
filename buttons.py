from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Uzbek"),
            KeyboardButton(text="Rus")
        ],
        
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Telfon raqam yuboring", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

kasal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qandli diabet"),
            KeyboardButton(text="Semizlik")
        ]
    ],
    resize_keyboard=True
)



diabet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "1 tip"),
            KeyboardButton(text = "2 tip")
            
        ],
        [
            KeyboardButton(text = "Bilmayman")
        ]
    ],
    resize_keyboard=True
)




tip3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "1 - 25 yoshgacha"),
            KeyboardButton(text= "25 va yuqori")
        ]
    ],
    resize_keyboard=True
)

insulin_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "XA"),
            KeyboardButton(text="YOQ")
        ]
    ],
    resize_keyboard=True
)

insulin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Ha"),
            KeyboardButton(text = "Yoq")
        ]
    ],
    resize_keyboard=True
)


