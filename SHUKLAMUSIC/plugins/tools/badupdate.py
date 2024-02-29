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

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #




import asyncio
import time

@app.on_message(filters.command("gadd") & SUDOERS & filters.user(int(HEHE)))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("Invalid command format. Please use: /addbots @bot_username")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **Adding bot in all chats!**")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002006121442:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username} ɪɴ ᴄʜᴀᴛs.\n\n**✅ ᴀᴅᴅᴇᴅ ɪɴ: {done} ᴄʜᴀᴛs**\n**❌ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs.**\n\n**⏲️ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** {time.time()}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username} ɪɴ ᴄʜᴀᴛs.\n\n**✅ ᴀᴅᴅᴇᴅ ɪɴ: {done} ᴄʜᴀᴛs**\n**❌ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs.**\n\n**⏲️ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** {time.time()}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"**🎉 {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.**\n\n**✅ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs.**\n**❌ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs.**\n\n**⏲️ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** {time.time()}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")