from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

import config
from Spy import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS  # Green
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=ButtonStyle.PRIMARY  # Blue
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS  # Green
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=ButtonStyle.SECONDARY  # Grey
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                callback_data="dil_spy",
                style=ButtonStyle.PRIMARY  # Blue
            ),
            InlineKeyboardButton(
                text=_["S_B_7"],
                callback_data="gib_source",
                style=ButtonStyle.DANGER  # Red
            ),
        ],
        [
            InlineKeyboardButton(
                "• ʙᴏᴛ ɪɴғᴏ •",
                callback_data="bot_info_data",
                style=ButtonStyle.WARNING  # Yellow
            ),
        ],
    ]
    return buttons
