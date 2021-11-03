import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Bot is now online and ready to roll')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'valo':
        await message.channel.send('valorant mo mukha mo')



client.run('OTA0OTMwNDQxNTM3MTUwOTk2.YYCsJg.26ZlC-zEevtHAC_hSGwGF3twtGs')
