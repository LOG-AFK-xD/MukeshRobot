from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://te.legra.ph/file/a05d9e016942a9dfa1775.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**Hᴇʏ​ {message.from_user.mention()},\n\nI Aᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ​ :** [Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={OWNER_ID})
**» Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{y()}`
**» Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{o}` 
**» Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{s}` 
**» Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{z}`

**Gʀᴏᴜᴘ ✘ Cᴏɴᴛʀᴏʟʟᴇʀ Sᴏᴜʀᴄᴇ Is Nᴏᴡ Pᴜʙʟɪᴄ Aɴᴅ Nᴏᴡ Yᴏᴜ Cᴀɴ Mᴀᴋᴇ Yᴏᴜʀ Oᴡɴ Bᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Creator",user_id=OWNER_ID
                    ),
                    InlineKeyboardButton(
                        "Support •",
                        url="t.me/LovePoisonxD",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
_help__ = """
 /repo  Tᴏ Gᴇᴛ Rᴇᴘᴏ 
 /source Tᴏ Gᴇᴛ Rᴇᴘᴏ
"""
