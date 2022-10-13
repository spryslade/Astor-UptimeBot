import asyncio
import datetime
import pytz

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

#vars
API_ID = 0
API_HASH = "arsh"
BOT_LIST = [i.strip() for i in "mewdekobot mangaprobot".split(' ')]
BOT_ADMIN_IDS = [int(i.strip()) for i in "1922 1982 1928291".split(' ')]
CHANNEL_OR_GROUP_ID = -132121442
MESSAGE_ID = 7
SESSION_STRING = "dwwewe"
TIME_ZONE = "Asia/Kolkata"

app = Client(
    name = "meow",
    api_id = API_ID,
    api_hash = API_HASH,
    session_string = SESSION_STRING
)

async def nigga():
    async with app:
            while True:
                print("Checking...")
                shinobi = "Bot's Working Status"
                for bot in BOT_LIST:
                    try:
                        bakufu = await app.send_message(bot, "/start")
                        aaa = bakufu.id
                        await asyncio.sleep(10)
                        sern = app.get_chat_history(bot, limit = 1)
                        async for ccc in sern:
                            bbb = ccc.id
                        if aaa == bbb:
                            shinobi += f"\n\n@{bot}\n          **Down** ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"**@{bot} is down**")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            shinobi += f"\n\n@{bot}\n          **Alive** ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                shinobi += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n**♻️ Refreshes automatically**"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, shinobi)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(nigga())
