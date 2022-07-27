#by @NobleWolf for @FridayUB

from pyrogram import *
from pyrogram.types import *
from helpers.basic import edit_or_reply
import random 
from handlers.help import *


NOBLE = [ ____$$$$$$$$$____ 
____$$$$$$$$$____ 
______$$$$$______ 
______$$$$$______ 
______$$$$$______ 
______$$$$$______ 
____$$$$$$$$$____ 
____$$$$$$$$$____ 
_________________ 
_$$$$$$___$$$$$$_ 
$$$$$$$$_$$$$$$$$ 
$$$$$$$$$$$$$$$$$ 
_$$$$$$$$$$$$$$$_ 
___$$$$$$$$$$$___ 
_____$$$$$$$_____ 
_______$$$_______ 
________$________ 
_________________ 
__$$$$$___$$$$$__ 
__$$$$$$_$$$$$$__ 
___$$$$$$$$$$$___ 
_____$$$$$$$_____ 
______$$$$$______ 
______$$$$$______ 
______$$$$$______ 
_________________ 
_____$$$$$$$_____ 
___$$$$$$$$$$$___ 
__$$$$$___$$$$$__ 
__$$$$$___$$$$$__ 
__$$$$$___$$$$$__ 
___$$$$$$$$$$$___ 
_____$$$$$$$_____ 
_________________ 
__$$$$$___$$$$$__ 
__$$$$$___$$$$$__ 
__$$$$$___$$$$$__ 
__$$$$$___$$$$$__ 
__$$$$$$_$$$$$$__ 
___$$$$$$$$$$$___ 
____$$$$$$$$$____
]


@Client.on_message(filters.me & (filters.command(["loveyou"], ["."]) | filters.regex("^loveyou ")))
async def _(client: Client, message: Message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble] 
    await edit_or_reply(message, reply_text)

add_command_help(
    "loveyou",
    [
        [".loveyou", "It Will Send Random Emojis."],
    ],
)
