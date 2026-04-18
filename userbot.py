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

BRIDGE_BOT = "@MissRose_bot"

# Yahan se 'filters.me' aur 'filters.user' hata diya hai
# Ab ye command PUBLIC hai (Bots aur Users dono ke liye)
@app.on_message(filters.command("fetch", prefixes="."))
async def fetch_data(client, message):
    """
    Command: .fetch @username
    Ab ye command koi bhi (user ya bot) aapke Userbot ko bhej sakta hai.
    """
    try:
        # Check if there is a target username
        if len(message.command) < 2:
            return
        
        target = message.command[1]
        print(f"📡 Global Request for: {target}")
        
        # 1. Rose Bot ko message bhejna
        await client.send_message(BRIDGE_BOT, f"/info {target}")
        
        # 2. 4 seconds wait (Thoda extra buffer safety ke liye)
        await asyncio.sleep(4)
        
        # 3. Rose ka reply uthana
        async for msg in client.get_chat_history(BRIDGE_BOT, limit=1):
            if msg.text:
                # Jisne bhi command bheji, usko Rose ka data reply kar dena
                await message.reply_text(msg.text)
                print(f"✅ Data delivered for {target}")
            else:
                print(f"⚠️ Rose bot didn't send a text response.")
                
    except Exception as e:
        print(f"❌ Userbot Error: {e}")

if __name__ == "__main__":
    print("🚀 Userbot is now PUBLIC. Listening to all users/bots...")
    app.run()
    
