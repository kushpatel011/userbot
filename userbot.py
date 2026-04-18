import os
import asyncio
from pyrogram import Client, filters

# Railway Variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

# --- OWNER SETTINGS ---
# Yahan apne CarloOsintBot ki numeric ID dalo taaki sirf wo hi command de sake
# Isse safety bani rahegi
ALLOWED_BOT_ID = 123456789 # <--- Apne Bot ki ID se replace karein

app = Client(
    "ub_worker",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    in_memory=True
)

BRIDGE_BOT = "@MissRose_bot"

# Command handler: filters.me hata diya gaya hai
@app.on_message(filters.command("fetch", prefixes="."))
async def fetch_data(client, message):
    # Safety Check: Sirf aapka Bot ya Aap khud command de sakein
    if message.from_user.id != ALLOWED_BOT_ID and not message.from_user.is_self:
        return

    try:
        if len(message.command) < 2:
            return
        
        target = message.command[1]
        print(f"📡 Request Received for: {target}")
        
        # 1. Rose Bot ko command bhejna
        await client.send_message(BRIDGE_BOT, f"/info {target}")
        
        # 2. 4 second wait (Rose kabhi kabhi slow hoti hai)
        await asyncio.sleep(4)
        
        # 3. Rose ka reply uthana
        async for msg in client.get_chat_history(BRIDGE_BOT, limit=1):
            if msg.text:
                # Bot ko reply dena
                await message.reply_text(msg.text)
                print(f"✅ Data sent back for {target}")
                
    except Exception as e:
        print(f"❌ Userbot Error: {e}")
        await message.reply_text(f"Error fetching data: {e}")

if __name__ == "__main__":
    print("🚀 Userbot Worker is Active on Railway...")
    app.run()
        
