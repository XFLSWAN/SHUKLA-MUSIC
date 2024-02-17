from pyrogram.types import InlineKeyboardButton

import config
from SHUKLAMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="⦿ 𝙷𝙴𝙻𝙿 ⦿", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="⦿ 𝚂𝙴𝚃 ⦿", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="⦿ 𝙶𝚁𝙾𝚄𝙿 ⦿", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="⦿ 𝙶𝚁𝙾𝚄𝙿 ⦿", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="⦿ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⦿", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="⦿ 𝚁𝙴𝙿𝙾 ⦿", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork"),
        ],
        [
            InlineKeyboardButton(text="⦿ 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ⦿", callback_data="settings_back_helper")
        ],
    ]
    return buttons
