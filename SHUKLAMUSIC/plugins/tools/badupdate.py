from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from SHUKLAMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/itzshukla/STRANGER-CHATBOT/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐔sᴇʀʙᴏᴛ 𝐑ᴇᴘᴏ 🗡️", url=f"https://t.me/Shukla_op_clone1bot")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-SPAM-X/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/itzshukla/STRANGER-CHATBOT/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐔sᴇʀʙᴏᴛ 𝐑ᴇᴘᴏ 🗡️", url=f"https://t.me/Shukla_op_clone1bot")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-SPAM-X/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/itzshukla/STRANGER-CHATBOT/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐔sᴇʀʙᴏᴛ 𝐑ᴇᴘᴏ 🗡️", url=f"https://t.me/Shukla_op_clone1bot")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-SPAM-X/fork")
                 ]
            ]
        ),
    )