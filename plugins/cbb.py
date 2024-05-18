# btn : about and close change here

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ OWNER : <a href='tg://user?id={OWNER_ID}'>MAHSOOM</a>\n○ UPDATES : <a href='https://t.me/Call_me_futurepilot'>Channel</a>\n○ MOVIE CHANNEL : <a href='https://t.me/Tamil_HDLatest_Movies'>TAMIL HD MOVIES</a>\n○ MOVIE REQUEST : <a href='https://t.me/+3DbjYjF9pvBkYzg1'>MOVIE REQUEST</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                        InlineKeyboardButton('JOIN', url='https://t.me/Call_me_futurepilot')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
