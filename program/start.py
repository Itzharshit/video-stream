from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **🤖 𝙄 𝘼𝙈 𝘼𝙉 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝙁𝙊𝙍 𝙋𝙇𝘼𝙔𝙄𝙉𝙂 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙏𝙃𝙀 𝙑𝙊𝙄𝘾𝙀 𝘾𝙃𝘼𝙏𝙎 𝙊𝙁 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 𝙂𝙍𝙊𝙐𝙋 & 𝘾𝙃𝘼𝙉𝙉𝙀𝙇.

✅  𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 :- @ARMY0071**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰➕ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ➕❱",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❰𝗕𝗮𝘀𝗶𝗰 𝗚𝘂𝗶𝗱𝗲❱", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("❰𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀❱", callback_data="cbcmds"),
                    InlineKeyboardButton("❰𝗗𝗼𝗻𝗮𝘁𝗲❱", url=f"https://t.me/ARMY0071"),
                ],
                [
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url=f"https://t.me/Worldwide_friends_chatting_zonee"
                    ),
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url=f"https://t.me/ARMY0071"
                    ),
                ],
                
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❰𝗚𝗿𝗼𝘂𝗽❱", url=f"https://t.me/Worldwide_friends_chatting_zonee"),
                InlineKeyboardButton(
                    "❰𝗢𝘄𝗻𝗲𝗿❱", url=f"https://t.me/ARMY0071"
                ),
            ]
        ]
    )

    alive = f"**🤖 𝙄 𝘼𝙈 𝘼𝙉 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝙁𝙊𝙍 𝙋𝙇𝘼𝙔𝙄𝙉𝙂 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙏𝙃𝙀 𝙑𝙊𝙄𝘾𝙀 𝘾𝙃𝘼𝙏𝙎 𝙊𝙁 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 𝙂𝙍𝙊𝙐𝙋 & 𝘾𝙃𝘼𝙉𝙉𝙀𝙇. ✅  𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 :- @ARMY0071**"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `𝙋𝙤𝙣𝙜!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 𝗕𝗼𝘁 𝘀𝘁𝗮𝘁𝘂𝘀:\n"
        f"• **𝙐𝙥𝙩𝙞𝙢𝙚:** `{uptime}`\n"
        f"• **𝙨𝙩𝙖𝙧𝙩 𝙩𝙞𝙢𝙚:** `{START_TIME_ISO}`"
    )
