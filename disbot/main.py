import os
import random
import discord
from discord.ext import commands
from decouple import config

client = commands.Bot(command_prefix=".")


# @client.event
# async def on_member_join(member):
#     print("{} has joined the Discord Server".format(member))


# @client.event
# async def on_member_remove(member):
#     print("{} has left the Discord Server".format(member))


# changed
# @client.command()
# async def ping(context):
#     await context.send("Pong {}ms".format(round(client.latency*1000)))


# @client.command(aliases=["8ball", 'test8ball'])
# async def _8ball(context, *, question):
#     responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
#                 "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
#                 "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
#                 "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
#                 "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
#     await context.send("Question: {} \n Answer: {}".format(question, random.choice(responses)))


# @client.command()
# async def clear(context, amount=5):
#     await context.channel.purge(limit=amount)

# @client.command()
# async def kick(context, member:discord.Member, *, reason=None):
#     await member.kick(reason=reason)

# @client.command()
# async def ban(context, member:discord.Member, *, reason=None):
#     await member.ban(reason=reason)
#     await context.send("banned {}".format(member.mention))

# @client.command()
# async def unban(context, *, member):
#     banned_users = await context.guild.bans()
#     member_name, member_discriminator = member.split("#")
#     for banned in banned_users:
#         user = banned.user
#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await context.guild.unban(user)
#             await context.send("Unbanned {}#{}".format(user.name,user.discriminator))
#             return

# @client.command()
# async def load(context, *extension):
#     print("loading {}".format(extension))
#     client.load_extension("cogs.{}".format(extension))

# @client.command()
# async def unload(context, extension):
#     print("Unloading {}".format(extension))
#     client.unload_extension("cogs.{}".format(extension))


@client.command()
async def load(context, *extension):
    for ext in extension:
        print("loading {}".format(ext))
        client.load_extension("cogs.{}".format(ext))


@client.command()
async def unload(context, *extension):
    for ext in extension:
        print("Unloading {}".format(ext))
        client.unload_extension("cogs.{}".format(ext))


@client.command()
async def reload(context, extension):
    print("Unloading {}".format(extension))
    client.unload_extension("cogs.{}".format(extension))
    print("Loading {}".format(extension))
    client.load_extension("cogs.{}".format(extension))


for dir in os.listdir(os.getcwd()):
    print(dir)
    if dir == "cogs":
        print("found cogs")
        os.chdir(dir)
        for filename in os.listdir(os.getcwd()):
            print("found {} in cogs folder".format(filename))
            if filename.endswith(".py"):
                print("working on cog {}".format(filename))
                print("loading extension {}".format(filename[:-3]))
                client.load_extension("cogs.{}".format(filename[:-3]))

client.run(config("KEY"))
