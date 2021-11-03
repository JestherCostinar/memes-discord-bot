import discord

"""
client = discord.Client()


@client.event
async def on_ready():
    print('Online')

client.run('OTA0OTMwNDQxNTM3MTUwOTk2.YYCsJg.26ZlC-zEevtHAC_hSGwGF3twtGs')
"""

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 904946727612743741

    async def on_ready(self):
        print('Online')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '😈':
            role = discord.utils.get(guild.roles, name='Devil')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😇':
            role = discord.utils.get(guild.roles, name='Angel')
            await payload.member.add_roles(role)


    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '😈':
            role = discord.utils.get(guild.roles, name='Devil')
            await member.remove_roles(role)
        elif payload.emoji.name == '😇':
            role = discord.utils.get(guild.roles, name='Angel')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('OTA0OTMwNDQxNTM3MTUwOTk2.YYCsJg.26ZlC-zEevtHAC_hSGwGF3twtGs')
