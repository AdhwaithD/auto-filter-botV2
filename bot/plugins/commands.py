#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption =f"<b>FILM NAME📽️</b>: <code><b> {file_name}</b> </code>\n<b>❤️Join [★Ⓜ️🌀𝚅𝙸𝙴𝚂_𝙲𝙻𝚄𝙱_𝟸⭕️𝟷𝟿™★] For New Movies.</b>\n❤️<u> 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</u> \n\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱  \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @MCmoviesall➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @Movies_Club_2019 ➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @Movies_Club_2019",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/Movies_Club_2019"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/mcnewmovies")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/joinchat/Qdw9ffZKXMxmMTg1"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/mcallmovies")
                ]
            ]
        )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            ],[
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/Sanoob_Achu_18')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            ],[
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/Sanoob_Achu_18')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            ],[
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/Sanoob_Achu_18')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
