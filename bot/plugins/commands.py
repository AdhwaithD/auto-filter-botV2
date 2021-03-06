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
                caption =f"<b>FILM NAME๐ฝ๏ธ</b>: <code><b> {file_name}</b> </code>\n<b>โค๏ธJoin [โ๐ฌ ๐ฅCINEMA LOKAM๐ฅ ๐ฌโ] For New Movies.</b>\nโค๏ธ<u> ๐๐๐๐๐๐ข๐๐ ๐ต๐๐ ๐๐๐๐๐ ๐พ๐๐ ๐๐๐๐๐๐๐ ๐ฟ๐๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐ฑ๐ข ๐๐๐๐๐๐๐ ๐พ๐๐ ๐ฒ๐๐๐๐๐๐/๐ถ๐๐๐๐ ๐ป๐๐๐ ๐๐ ๐๐๐๐ ๐ต๐๐๐๐๐๐</u> \n\nโ๐๐ ๐๐ ๐๐ฆ๐ฃ โ๐๐๐๐๐๐๐คโ  \nโฑโฑโฑโฑโฑโฑโฑโฑโฑโฑโฑโฑ  \n๐๐ฎ๐๐๐๐๐๐: @ADMOVEIโป \n๐๐ฎ๐๐๐๐๐๐ : @ADMOVEIS_OTTโป \n๐ฅ๐ฒ๐๐๐๐ : @ADMOVEIAD โป \n๐ฅ๐ฒ๐๐๐๐ : @ADMOVEIAD",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('โ๏ธ ๐๐๐ผ๐๐', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/ADMOVEIAD")
                ],
                [
                    InlineKeyboardButton('๐ฌ ๐๐๐๐๐', url="https://t.me/ADMOVEIAD"),
                    InlineKeyboardButton('๐ ๐๐๐ ๐๐๐๐๐ผ๐๐', url="https://t.me/ADMOVEIS_OTT")
                ],
                [
                    InlineKeyboardButton('๐ ๐๐๐๐๐๐๐', url="https://t.me/ADMOVEIAD"),
                    InlineKeyboardButton('๐ฅ ๐พ๐๐ผ๐๐๐๐', url="https://t.me/ADMOVEI")
                ]
            ]
        )
    )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
            InlineKeyboardButton('โป๏ธ ๐ถ๐๐๐๐', url='https://t.me/ADMOVEIAD'),
            InlineKeyboardButton('โญ๏ธ ๐ฒ๐๐๐๐๐๐', url='https://t.me/ADMOVEI')
            ],[
            InlineKeyboardButton('๐ตโโ๏ธ ๐ฐ๐๐ข ๐ณ๐๐๐๐๐ ๐ตโโ๏ธ', url='https://t.me/Lucifer_Devil_AD')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/064e37be329e704c11638.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
            InlineKeyboardButton('โป๏ธ ๐ถ๐๐๐๐', url='https://t.me/ADMOVEIAD'),
            InlineKeyboardButton('โญ๏ธ ๐ฒ๐๐๐๐๐๐', url='https://t.me/ADMOVEI')
            ],[
            InlineKeyboardButton('๐ตโโ๏ธ ๐ฐ๐๐ข ๐ณ๐๐๐๐๐ ๐ตโโ๏ธ', url='http://t.me/Lucifer_Devil_AD')
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
            InlineKeyboardButton('โป๏ธ ๐ถ๐๐๐๐', url='https://t.me/ADMOVEIAD'),
            InlineKeyboardButton('โญ๏ธ ๐ฒ๐๐๐๐๐๐', url='https://t.me/ADMOVEI')
            ],[
            InlineKeyboardButton('๐ตโโ๏ธ ๐ฐ๐๐ข ๐ณ๐๐๐๐๐ ๐ตโโ๏ธ', url='http://t.me/Lucifer_Devil_AD')
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
