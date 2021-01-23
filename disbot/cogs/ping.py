import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Started via Cog.")

    # commands
    @commands.command()
    async def ping(self, context):
        await context.send("Pong {}ms".format(round(self.client.latency * 1000)))


# async def on_ready():
#     print("Bot Started")


def setup(client):
    client.add_cog(Ping(client))
