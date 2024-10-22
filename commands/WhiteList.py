# Github: https://github.com/Celentroft
# Don't be a skid, ty

import discord
from functions import *
from discord import option
from discord.ext import commands

ping_types = ['here', 'everyone']

class WhiteListCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def ping_type_autocomplete(self, ctx: discord.AutocompleteContext):
        return [discord.OptionChoice(name=ping_type, value=ping_type) for ping_type in ping_types]

    @commands.slash_command(name="add-ping", description="Add everyone or here ping for a slot user")
    @option("member", description="Member for who ping should be added", type=discord.Member)
    @option("pingtype", description="Here or everyone ping", autocomplete=ping_type_autocomplete)
    @option("amount", description="Amount of ping will be added", type=int)
    async def add_ping(self, ctx, member: discord.Member, pingtype: str, amount: int):
        await ctx.defer()
        config = load_json()
        if ctx.author.id not in config['whitelist'] and ctx.author.id != int(config['buyer']):
            return await ctx.respond("You are not allowed to do this", ephemeral=True)
        with open("database.json", 'r') as f:
            db_config = json.load(f)
        ping_to_add = None
        if pingtype == "here":
            ping_to_add = "max_here"
        elif pingtype == "everyone":
            ping_to_add = "max_everyone"
        else:
            return await ctx.respond("Invalid ping type selected", ephemeral=True)
        for user in db_config:
            if user == member.name:
                db_config[user][ping_to_add] = db_config[user][ping_to_add] + amount
                with open("database.json", 'w') as f:
                    json.dump(db_config, f, indent=4)
                    f.close()
                embed = discord.Embed(
                    title="Ping Added",
                    description=f"{amount} @{pingtype} added for {member.mention}",
                    color=embed_color()
                )
                embed.set_footer(text=footer())
                return await ctx.respond(embed=embed)
        await ctx.respond("User not found, please provide a valid user", ephemeral=True)
        
    @commands.slash_command(name="remove-ping", description="Remove everyone or here ping for a slot user")
    @option("member", description="Member for who ping should be removed", type=discord.Member)
    @option("pingtype", description="Here or everyone ping", autocomplete=ping_type_autocomplete)
    @option("amount", description="Amount of ping will be removed", type=int)
    async def remove_ping(self, ctx, member: discord.Member, pingtype: str, amount: int):
        await ctx.defer()
        config = load_json()
        if ctx.author.id not in config['whitelist'] and ctx.author.id != int(config['buyer']):
            return await ctx.respond("You are not allowed to do this", ephemeral=True)
        with open("database.json", 'r') as f:
            db_config = json.load(f)
        ping_to_add = None
        if pingtype == "here":
            ping_to_add = "max_here"
        elif pingtype == "everyone":
            ping_to_add = "max_everyone"
        else:
            return await ctx.respond("Invalid ping type selected", ephemeral=True)
        for user in db_config:
            if user == member.name:
                db_config[user][ping_to_add] = db_config[user][ping_to_add] - amount
                with open("database.json", 'w') as f:
                    json.dump(db_config, f, indent=4)
                    f.close()
                embed = discord.Embed(
                    title="Ping Added",
                    description=f"{amount} @{pingtype} removed for {member.mention}",
                    color=embed_color()
                )
                embed.set_footer(text=footer())
                return await ctx.respond(embed=embed)
        await ctx.respond("User not found, please provide a valid user", ephemeral=True)

def setup(bot):
    bot.add_cog(WhiteListCommands(bot))