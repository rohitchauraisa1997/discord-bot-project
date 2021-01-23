import discord
from discord.ext import commands


class Kicks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, context, member: discord.Member, *, reason=None):
        print("Kicking member {} from guild".format(member))
        await member.kick(reason=reason)


def setup(client):
    client.add_cog(Kicks(client))


# @client.command()
# async def kick(context, member:discord.Member, *, reason=None):
#     await member.kick(reason=reason)
