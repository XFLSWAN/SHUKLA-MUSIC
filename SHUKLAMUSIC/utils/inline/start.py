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
            InlineKeyboardButton(text="🕯ʜᴇʟᴘ🕯️", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="🍭 ᴧᴅᴍɪɴ 🍭", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🍥sᴜᴘᴘᴏʀᴛ🍥", url=config.SUPPORT_CHAT),
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
            InlineKeyboardButton(text="🍥sᴜᴘᴘᴏʀᴛ🍥", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="✨ᴜᴘᴅᴀᴛᴇs✨", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="🗼ʀᴇᴘᴏ🗼", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork"),
        ],
        [
            InlineKeyboardButton(text="⦿ 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ⦿", callback_data="settings_back_helper")
        ],
    ]
    return buttons
