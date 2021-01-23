import discord
from discord.ext import commands


class ClearLast(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear_last(self, context, amount=5):
        print("Cleared Last {} commands".format(amount))
        await context.channel.purge(limit=amount)


def setup(client):
    client.add_cog(ClearLast(client))
