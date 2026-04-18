import os
import asyncio
from pyrogram import Client, filters

# Railway Variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

# Userbot Client
app = Client(
    "ub_worker",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    in_memory=True
)

@app.on_message(filters.command("fetch", prefixes=".") & filters.me)
async def fetch_data(client, message):
    """Command: .fetch @username (Ye aapka main bot bhejega)"""
    try:
        if len(message.command) < 2:
            return
        
        target = message.command[1]
        bridge_bot = "@MissRose_bot" # Ya @userinfobot
        
        # Rose ko command bhejna
        await client.send_message(bridge_bot, f"/info {target}")
        
        # 3 second wait karna Rose ke reply ke liye
        await asyncio.sleep(3)
        
        # Rose ka reply uthana
        async for msg in client.get_chat_history(bridge_bot, limit=1):
            if msg.text:
                # Wapas apne main bot ko reply bhej dena
                await message.reply_text(msg.text)
    except Exception as e:
        print(f"Error: {e}")

print("Userbot is running...")
app.run()
