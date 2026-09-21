import os
import asyncio
from pyrofork import Client, filters

# Data API dan Session String milikmu
api_id = 31715365
api_hash = "d1893dd5c254ac8372c5f1073d5dc417"
SESSION_STRING = "1BVtsOL0Bu7X1_FWLAHK2pKEO8TbWNsRXwnwgFdrHhXDJUrvYbVfLFfLrHgZ0m2kqTTnaaylQsiDKH7AJgVQ-GXPPVzLlURE850VTgroFnkThwDVA0hro1_v5-HAmdtuuOo3vtlCaI3itmKYm62x6ENRDu04NF4BQ2lI7vRIzR9CV4Ev5x_HTqgBsNf8DV5jFUUoKF-_VKw7oujfiw6Xh-uiGqt7KkZTnp5Vnzl22IDTP0UGnIyHBxHcYBgwVNHpRj3PEDIaROPdz5W-CnGQcFJrY2PZHXpQO2iWBNQ6TM2SQ6b44UiCeV4sgT1f3YHDaKZPf0zKpAPaTBhsaLxJELB4p2WG2JDs="

OWNER_USERNAME = "finzkawakawa1"
is_active = True

app = Client("userbot_session", api_id=api_id, api_hash=api_hash, session_string=SESSION_STRING)

# --- Fitur ON / OFF ---
@app.on_message(filters.command(["bot", "userbot"], prefixes=".") & filters.me)
async def toggle_bot(client, message):
    global is_active
    if message.from_user and message.from_user.username and message.from_user.username.lower() == OWNER_USERNAME.lower():
        command_args = message.text.split()
        if len(command_args) > 1:
            arg = command_args[1].lower()
            if arg == "on":
                is_active = True
                await message.edit_text("✅ Userbot berhasil **DIAKTIFKAN**.")
            elif arg == "off":
                is_active = False
                await message.edit_text("❌ Userbot berhasil **DINONAKTIFKAN**.")
            else:
                await message.edit_text("Gunakan perintah: `.bot on` atau `.bot off`")
        else:
            status = "Aktif" if is_active else "Nonaktif"
            await message.edit_text(f"Status Userbot saat ini: **{status}**")

# --- Fitur Replay Angka Dadu (1-6) ---
@app.on_message(filters.dice & ~filters.me)
async def reply_dice_number(client, message):
    global is_active
    if not is_active:
        return

    dice_value = message.dice.value
    await message.reply_text(str(dice_value))

print("Userbot berjalan...")
app.run()
          
