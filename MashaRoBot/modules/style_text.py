# made by @ctzfamily © @pegasusXteam - © @VegetaRobot

from MashaRoBot import dispatcher
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from MashaRoBot.modules.helper_funcs.alternate import typing_action
from telegram import ParseMode
from telegram.ext import run_async

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

text1font = [
    "ᵃ",
    "ᵇ",
    "ᶜ",
    "ᵈ",
    "ᵉ",
    "ᶠ",
    "ᵍ",
    "ʰ",
    "ⁱ",
    "ʲ",
    "ᵏ",
    "ˡ",
    "ᵐ",
    "ⁿ",
    "ᵒ",
    "ᵖ",
    "ᵠ",
    "ʳ",
    "ˢ",
    "ᵗ",
    "ᵘ",
    "ᵛ",
    "ʷ",
    "ˣ",
    "ʸ",
    "ᶻ",
]
text2font = [
    "ⓐ",
    "ⓑ",
    "ⓒ",
    "ⓓ",
    "ⓔ",
    "ⓕ",
    "ⓖ",
    "ⓗ",
    "ⓘ",
    "ⓙ",
    "ⓚ",
    "ⓛ",
    "ⓜ",
    "ⓝ",
    "ⓞ",
    "ⓟ",
    "ⓠ",
    "ⓡ",
    "ⓢ",
    "ⓣ",
    "ⓤ",
    "ⓥ",
    "ⓦ",
    "ⓧ",
    "ⓨ",
    "ⓩ",
]

text3font = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]
text4font = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]

text5font = [
    "ᴀ",
    "ʙ",
    "ᴄ",
    "ᴅ",
    "ᴇ",
    "ғ",
    "ɢ",
    "ʜ",
    "ɪ",
    "ᴊ",
    "ᴋ",
    "ʟ",
    "ᴍ",
    "ɴ",
    "ᴏ",
    "ᴘ",
    "ǫ",
    "ʀ",
    "s",
    "ᴛ",
    "ᴜ",
    "ᴠ",
    "ᴡ",
    "x",
    "ʏ",
    "ᴢ",
]


@run_async
@typing_action
def text1(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("plz reply to the text.", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            text1character = text1font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, text1character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def text2(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("plz reply to the text.", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            text2character = text2font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, text2character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def text3(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("plz reply to the text.", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            text3character = text3font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, text3character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def text4(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("plz reply to the text.", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            text4character = text4font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, text4character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@run_async
@typing_action
def text5(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("plz reply to the text.", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            text5character = text5font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, text5character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
            
__help__ = """

 ❍ `/text1`*:* reply to the text.
 ❍ `/text2`*:* reply to the text.
 ❍ `/text3`*:* reply to the text.
 ❍ `/text4`*:* reply to the text.
 ❍ `/text5`*:* reply to the text.
"""
__mod_name__ = "sᴛʏʟᴇ ᴛᴇxᴛ🦚"

TEXT1_HANDLER = DisableAbleCommandHandler("text1", text1)
TEXT2_HANDLER = DisableAbleCommandHandler("text2", text2)
TEXT3_HANDLER = DisableAbleCommandHandler("text3", text3)
TEXT4_HANDLER = DisableAbleCommandHandler("text4", text4)
TEXT5_HANDLER = DisableAbleCommandHandler("text5", text5)

dispatcher.add_handler(TEXT1_HANDLER)
dispatcher.add_handler(TEXT2_HANDLER)
dispatcher.add_handler(TEXT3_HANDLER)
dispatcher.add_handler(TEXT4_HANDLER)
dispatcher.add_handler(TEXT5_HANDLER)

__command_list__ = ["text1"]
__command_list__ = ["text2"]
__command_list__ = ["text3"]
__command_list__ = ["text4"]
__command_list__ = ["text5"]

__handlers__ = [TEXT1_HANDLER]
__handlers__ = [TEXT2_HANDLER]
__handlers__ = [TEXT3_HANDLER]
__handlers__ = [TEXT4_HANDLER]
__handlers__ = [TEXT5_HANDLER]



#this module only creat for @VegetaRobot don't copy it you copy this plz don't remove below text
# © @VegetaRobot - © @pegasusXteam
