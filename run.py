from pyrogram import Client, filters
import tgcrypto


#CREATE YOUR BOT IN https://t.me/BotFather
token = "PUT YOUR BOT TOKEN HERE"

#GENERATOR YOUR API ID/HASH IN https://my.telegram.org/
api_id = ""
api_hash = ""

app = Client(name="remove_forward", bot_token=token, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command(["start"]))
async def start_message(client, message):
    await message.reply(f"""Hi {message.from_user.first_name} 👋
Put the bot in your group with the privileges to delete message.""")


@app.on_message(filters.forwarded)
async def delete_message(client, message):
    await message.delete(message.id)


app.run()