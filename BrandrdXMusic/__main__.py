import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import sudo
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

STRING1="BAGZqnkAt5U5V5U6bxU-TLQPao-0T8kFLhIvgZT_5uDKo3pStQjpgzyW93UgBDPiyozY0uafKGXHtxN8W3E8HFDUlyQqiRTQjFyW2zuYBrD-aV0rT5PCzMd3vEIqWWEVNS5ricJ_jRLhVuxt1pBw0oSVkOCcd4AqAO_DbMip6h5zigvz7Af9U48LgNX9c8ZeajOBTrzgMh722sCdbSXsd-Ag1o8qxicDMHIAwT8Eqeyalh9FLA5pudiQ88oR4mFhThgjUw7If6hCF7LUbksmwDTxb6RDU-Fp6o4Dq_6f8c9WCcQWuZjsbt0QZRNMLuvKKQCeLIBPlUtiAOs9hHEoP0WHA1MbKgAAAAGUqifiAA"
STRING2=STRING1
STRING3=STRING1
STRING4=STRING1
STRING5=STRING1


async def init():
    if (
        not STRING1
        and not STRING2
        and not STRING3
        and not STRING4
        and not STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BrandrdXMusic.plugins" + all_module)
    LOGGER("BrandrdXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("BrandrdXMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @ʙʀᴀɴᴅᴇᴅᴋɪɴɢ82 ᴊᴏɪɴ @ʙʀᴀɴᴅʀᴅ_ʙᴏᴛ , @ʙʀᴀɴᴅᴇᴅ_ᴡᴏʀʟᴅ ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
