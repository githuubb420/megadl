# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os


class Config:
    API_ID = 2419770
    API_HASH = 'eec8bf9b714bc4942e1cbfbdfb299063'
    BOT_TOKEN = '5780148364:AAFcCHgzhaIDj_cNUBOpSglQsADnHAnsCeE'
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = '1602757268'
    LOG_CHANNEL = '-1001874504630'
    UPDATES_CHANNEL = 'condomhub'


class TEXT:
    ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

"""

    HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @AsmSafone! 👑**
"""

    START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
