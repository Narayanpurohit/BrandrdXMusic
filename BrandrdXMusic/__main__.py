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

STRING1="BQEPlikAtoPyhSCyVdmH6fZ7TJlfc7gEOxAH2jfXLlNVmGy_B15gGIvxPq9Wqjyby1OcqVoFnjWWFkx_NfPlyZjZUpvDPMUZkYN-kM06YOY00HZrJzBrnBu3zrEmQ8IByqDAcxlxueg-EI2SilaPskX_GL2oMEzCE41ZcLz6KaLladCkem9tC73ubdOikVqbqwmBbQktrsMSDZ7YRshyupB4smkOi303PIFyPbwxOQfYu3NJ0F8hwh5DToBG624jW6emgjMzb8-4kHm5L5__I0n6659IeSya0mxxEKn-ZRNbovi7vMEQxPGqFfQvh4CQPMnlbdIjz4vl0AFeJ5qNQ9u7sOFWpgAAAAFsS4jiAA"
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
