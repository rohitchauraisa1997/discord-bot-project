import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands
    @commands.command()
    async def test(self, context):
        await context.send("TESTING 2nd COG")


def setup(client):
    client.add_cog(Test(client))
