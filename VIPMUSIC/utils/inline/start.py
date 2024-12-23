from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️ ᴧᴅᴅ мᴇ ʙᴧʙʏ ⛩️",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️ ᴧᴅᴅ мᴇ ʙᴧʙʏ ⛩️",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🍬 sᴜᴘᴘᴏꝛᴛ 🍬", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="🍹 ᴜᴘᴅᴀᴛᴇ 🍹", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="🏩 ʜᴇʟᴘ ᴧиᴅ ᴄᴏᴍᴍᴧɴᴅs 🏩", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️ ᴧᴅᴅ мᴇ ʙᴧʙʏ ⛩️", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons


def music_start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️ ᴧᴅᴅ мᴇ ʙᴧʙʏ ⛩️",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🦋 ᴀʙᴏᴜᴛ 🦋", callback_data="about"),
            InlineKeyboardButton(text="🍬 sᴜᴘᴘᴏꝛᴛ 🍬", callback_data="support"),
        ],
        [InlineKeyboardButton(text="🏩 ʜᴇʟᴘ ᴧиᴅ ᴄᴏᴍᴍᴧɴᴅs 🏩", callback_data="feature")],
    ]
    return buttons
