import os
from pyrogram import Client, filters
from pyrogram.types import *

from MashaRoBot.conf import get_str_key
from MashaRoBot import pbot
 
 # pls don't delete
REPO_TEXT = "**Thanimai [BOT](https://telegra.ph/file/526ed899597d7827474a1.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [Telegram pro](t.me/TheTelegrampro) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @THANIMAIBOTS «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://github.com/proTamizhan/thanimaibot"),
        InlineKeyboardButton("Gɪᴛʜᴜʙ", url=f"https://github.com/proTamizhan"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ❣️", url="https://t.me/TheTelegrampro"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/thanimaisupport"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Kittu_the_criminall"),
      ],[
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/THANIMAIBOTS"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/ctzfamily"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Sarbudeen786"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
