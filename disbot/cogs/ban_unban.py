import discord
from discord.ext import commands


class BanUnban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def banning(self, context, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await context.send("banned {}".format(member.mention))

    @commands.command()
    async def unbanning(self, context, *, member):
        banned_users = await context.guild.bans()
        member_name, member_discriminator = member.split("#")
        for banned in banned_users:
            user = banned.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await context.guild.unban(user)
                await context.send(
                    "Unbanned {}#{}".format(user.name, user.discriminator)
                )
                return


def setup(client):
    client.add_cog(BanUnban(client))
