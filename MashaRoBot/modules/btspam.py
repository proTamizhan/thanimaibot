import asyncio
import os
from asyncio import sleep
from telethon import events
from .. import bot, OWNER_ID

#############-CONSTANTS-##############
LOGGER = True

@telethn.on(events.NewMessage(pattern=r"/tspam (.*)"))
async def tmeme(e):
  if OWNER_ID==True:
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()


@telethn.on(events.NewMessage(pattern=r"/spam (.*)"))
async def spammer(e):
  if OWNER_ID == True:
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()


@telethn.on(events.NewMessage(pattern=r"/bigspam (.*)"))
async def bigspam(e):
  if OWNER_ID==True:
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()