import random

from aiogram import types

from locales_dict import LocalesDict
from models import PostMode

class QueryResults:
    def __init__(self, locales: LocalesDict):
        self.locales = locales

    def message_too_long(self, lang: str):
        message_content = types.InputTextMessageContent(self.locales[lang].too_long_message)
        return types.InlineQueryResultArticle(
            id = '1', title = self.locales[lang].too_long_title,
            input_message_content = message_content,
            description = self.locales[lang].too_long_description,
            thumb_url = 'https://telegra.ph/file/8563f0df6e8581900de8d.jpg')

    def mode_for(self, lang: str, post_id, body, scope_string):
        keyboard = types.InlineKeyboardMarkup(inline_keyboard =
            [[types.InlineKeyboardButton(self.locales[lang].view, callback_data = str(post_id) +
            ' ' + PostMode.parse_key(PostMode.FOR))]])
        message_content = types.InputTextMessageContent(self.locales[lang].for_message % scope_string)
        return types.InlineQueryResultArticle(
            id = str(PostMode.FOR), title = self.locales[lang].for_title % scope_string,
            input_message_content = message_content,
            reply_markup = keyboard,
            description = body,
            thumb_url = 'https://telegra.ph/file/8563f0df6e8581900de8d.jpg')

    def mode_except(self, lang: str, post_id, body, scope_string):
        keyboard = types.InlineKeyboardMarkup(inline_keyboard =
            [[types.InlineKeyboardButton(self.locales[lang].view, callback_data = str(post_id) +
            ' ' + PostMode.parse_key(PostMode.EXCEPT))]])
        message_content = types.InputTextMessageContent(self.locales[lang].except_message % scope_string)
        return types.InlineQueryResultArticle(
            id = str(PostMode.EXCEPT), title = self.locales[lang].except_title % scope_string,
            input_message_content = message_content,
            reply_markup = keyboard,
            description = body,
            thumb_url = 'https://telegra.ph/file/8563f0df6e8581900de8d.jpg')

    def mode_spoiler(self, lang: str, post_id, body):
        keyboard = types.InlineKeyboardMarkup(inline_keyboard =
            [[types.InlineKeyboardButton(self.locales[lang].view, callback_data = str(post_id) +
            ' ' + PostMode.parse_key(PostMode.SPOILER))]])
        message_content = types.InputTextMessageContent(self.locales[lang].spoiler_message)
        return types.InlineQueryResultArticle(
            id = str(PostMode.SPOILER), title = self.locales[lang].spoiler_title,
            input_message_content = message_content,
            reply_markup = keyboard,
            description = body,
            thumb_url = 'https://telegra.ph/file/8563f0df6e8581900de8d.jpg')

class Keyboards:
    def info_keyboard(self):
        
        return types.InlineKeyboardMarkup(inline_keyboard=
             [[types.InlineKeyboardButton('➪ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓',    url='https://teletype.in/@wetemp/wisper')],
              [types.InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ',    url='https://t.me/botXdesk')
               types.InlineKeyboardButton('ʙᴏᴛ x ɴᴇᴛᴡᴏʀᴋ',   url='https://t.me/botxnetwork')]])

class Media:
    def group_greeting_sticker_id(self):
        return random.choice(('CAACAgIAAxkBAAECkihg7Y5tYnlKz9jRe6QCNOyvEZri2wACSQ4AAliyaUuDPYCgY_2GXiAE',
                              'CAACAgIAAxkBAAECkilg7Y5tzJPtIX4UMDgYaoxD6zcrogAC8Q0AAvMraEvkpXQDG5qEbyAE',
                              'CAACAgIAAxkBAAECkipg7Y5tQk6MZlccqoudX9PEnxPbUwACfBAAAhJpcEuU9SdfdRAPdiAE'))

class Resources:
    def __init__(self, locales: LocalesDict):
        self.query_results = QueryResults(locales)
        self.keyboards = Keyboards()
        self.media = Media()
