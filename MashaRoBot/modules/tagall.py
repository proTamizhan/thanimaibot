import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from MashaRoBot import telethn as bot
import telethon
from telethon import events


@bot.on(events.NewMessage(pattern="@all ?(.*)"))
async def _(event):
    if event.fwd_from:
        return # @ImJanindu
    mentions = event.pattern_match.group(1)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@bot.on(events.NewMessage(pattern="@admins ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Admins in this chat:** "
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.username}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__mod_name__ = "ᴛᴀɢᴀʟʟ💫"
__help__ = """
- /tagall : Tag everyone in a chat
"""
