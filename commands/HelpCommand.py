import discord
from discord.ext import commands
from functions import embed_color, footer

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Show help panel")
    async def helpcommand(self, ctx):
        embed = discord.Embed(
            title="Help Panel",
            color=embed_color()
        )
        embed.add_field(name="/add-ping", value="Add ping per day for a slot owner", inline=False)
        embed.add_field(name="/backup", value="Backup your slot with backup key", inline=False)
        embed.add_field(name="/config-channel-reset", value="Configuration of reset ping announcement channel", inline=False)
        embed.add_field(name="/config-role", value="Configuration of role added for slot owners", inline=False)
        embed.add_field(name="/create-slot", value="Create a slot", inline=False)
        embed.add_field(name="/extend-subscription", value="Add time for a slot subscription", inline=False)
        embed.add_field(name="/hold", value="Hold a slot", inline=False)
        embed.add_field(name="/remove-ping", value="Remove ping per day for a slot owner", inline=False)
        embed.add_field(name="/unwl", value="Remove an user from whitelist", inline=False)
        embed.add_field(name="/wl", value="Add an user into whitelist", inline=False)
        embed.add_field(name="/wl-list", value="Show all users into the whitelist", inline=False)
        embed.set_footer(text=footer())
        embed.set_thumbnail(url=self.bot.user.avatar)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommand(bot))