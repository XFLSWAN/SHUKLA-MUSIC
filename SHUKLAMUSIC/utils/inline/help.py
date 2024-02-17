from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from SHUKLAMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="⦿ 𝙼𝙾𝚁𝙴 ⦿", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="⦿ 𝙰𝙳𝙼𝙸𝙽 ⦿",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="⦿ 𝙰𝚄𝚃𝙷 ⦿",
                    callback_data="help_callback hb2",
                ),
            
            ],
            [
                InlineKeyboardButton(
                    text="⦿ 𝙱𝙻𝙾𝙲𝙺 ⦿",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="⦿ 𝙶𝙲𝙰𝚂𝚃 ⦿",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⦿ 𝙶𝙱𝙰𝙽 ⦿",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="⦿ 𝙻𝚈𝚁𝙸𝙲𝚂 ⦿",
                    callback_data="help_callback hb5",
                ),
            ],
                        
            [
                InlineKeyboardButton(
                    text="⦿ 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃 ⦿",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="⦿ 𝚅𝙾𝙸𝙲𝙴-𝙲𝙷𝙰𝚃 ⦿",
                    callback_data="help_callback hb10",
                ),
            ],
            [
                            InlineKeyboardButton(text="⦿ 𝚂𝙷𝙸𝚅𝙰𝙽𝚂𝙷-𝚇𝙳 ⦿", url=f"https://t.me/SHIVANSH39"),
                            InlineKeyboardButton(text="⦿ 𝚂𝙷𝚄𝙺𝙻𝙰 ⦿", url=f"https://t.me/ITSZ_SHIVANSH"),
            ],
            [
           
                InlineKeyboardButton(
                    text="⦿ 𝙿𝙻𝙰𝚈 ⦿",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="⦿ 𝚂𝚄𝙳𝙾 ⦿",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⦿ 𝚂𝚃𝙰𝚁𝚃 ⦿",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="⦿ 𝙼𝙾𝚁𝙴 ⦿", callback_data="help_callback hb14"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⦿ 𝙷𝙴𝙻𝙿 ⦿",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
    
    
    
