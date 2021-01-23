import random
import discord
from discord.ext import commands


class Eight_Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def eight_response(self, context, *, question):
        responses = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes, definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most Likely",
            "Outlook Good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very Doubtful",
        ]

        await context.send(
            "Question: {} \n Answer: {}".format(question, random.choice(responses))
        )


def setup(client):
    client.add_cog(Eight_Ball(client))
