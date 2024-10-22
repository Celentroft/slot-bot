# Github: https://github.com/Celentroft
# Don't be a skid, ty

import discord
from discord.ext import commands
from functions import embed_color, footer

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Show bot latency")
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Bot Latency",
            description=f"Bot latency is `{round(self.bot.latency * 1000)}` ms",
            color=embed_color()
        )
        embed.set_footer(text=footer())
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(PingCommand(bot))