import discord
from discord.ext import commands


class NewJoinee(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member, context):
        print("{} has joined the Discord Server".format(member))
        await context.send("{} has joined the Discord Server".format(member))

    @commands.Cog.listener()
    async def on_member_leave(self, member, context):
        print("{} has left the Discord Server".format(member))
        await context.send("{} has left the Discord Server".format(member))


def setup(client):
    client.add_cog(NewJoinee(client))
