import random
import discord
from discord.ext import commands
from decouple import config

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot Started")


@client.event
async def on_member_join(member):
    print("{} has joined the Discord Server".format(member))


@client.event
async def on_member_remove(member):
    print("{} has left the Discord Server".format(member))



# changed
@client.command()
async def ping(context):
    await context.send("Pong {}ms".format(round(client.latency*1000)))


@client.command(aliases=["8ball", 'test'])
async def _8ball(context, *, question):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
                "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
                "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
                "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
    await context.send("Question: {} \n Answer: {}".format(question, random.choice(responses)))


client.run(config('KEY'))

