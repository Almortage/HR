
import pyrogram
from pyrogram import Client, filters
from driver.filters import command
from pyrogram.types import Message


@Client.on_message(command(["قول", "ول"]) & ~filters.edited)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)
    
    


