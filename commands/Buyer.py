# Github: https://github.com/Celentroft
# Don't be a skid, ty

import json
import discord
from functions import *
from discord import option
from discord.ext import commands

class BuyerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="wl", description="Add user into whitelist")
    @option("member", description="Member added into whitelist", type=discord.Member)
    async def wl(self, ctx, member: discord.Member):
        config = load_json()
        if ctx.author.id != int(config['buyer']):
            return await ctx.respond("You are not allowed to do this.", ephemeral=True)
        wl = config['whitelist']
        if member.id in wl:
            return await ctx.respond(f"Member {member.mention} is already in whitelist", ephemeral=True)
        wl.append(member.id)
        config['whitelist'] = wl
        with open("config.json", 'w') as f:
            json.dump(config, f, indent=4)
            f.close()
        embed = discord.Embed(
            title="Whitelist",
            description=f"Member {member.mention} successfuly added into whitelist",
            color=embed_color()
        )
        embed.set_footer(text=footer())
        return await ctx.respond(embed=embed)
    
    @commands.slash_command(name="unwl", description="Remove user from whitelist")
    @option("member", description="Member removed from whitelist", type=discord.Member)
    async def unwl(self, ctx, member: discord.Member):
        config = load_json()
        if ctx.author.id != int(config['buyer']):
            return await ctx.respond("You are not allowed to do this.", ephemeral=True)
        wl = config['whitelist']
        if member.id not in wl:
            return await ctx.respond(f"Member {member.mention} are not in whitelist", ephemeral=True)
        wl.remove(member.id)
        config['whitelist'] = wl
        with open("config.json", 'w') as f:
            json.dump(config, f, indent=4)
            f.close()
        embed = discord.Embed(
            title="Whitelist",
            description=f"Member {member.mention} successfuly removed from whitelist",
            color=embed_color()
        )
        embed.set_footer(text=footer())
        return await ctx.respond(embed=embed)
    
    @commands.slash_command(name="wl-list", description="Show all user into whitelist")
    async def wllist(self, ctx):
        config = load_json()
        if ctx.author.id != int(config['buyer']):
            return await ctx.respond("You are not allowed to do this.", ephemeral=True)
        joined = "".join(f"<@{uid}> `{uid}`\n" for uid in config['whitelist'])
        embed = discord.Embed(
            title=f"Whitelist",
            description=joined,
            color=embed_color()
        )
        embed.set_footer(text=footer())
        await ctx.respond(embed=embed)

    @commands.slash_command(name="config-role", description="Config Slot Owner Role")
    @option("role", description="role given for slots owners", type=discord.Role)
    async def config_roles(self, ctx, role: discord.Role):
        config = load_json()
        if ctx.author.id != int(config['buyer']):
            return await ctx.reply("You are not allowed to do this", ephemeral=True)
        config['seller_roles'] = role.id
        with open("config.json", 'w') as f:
            json.dump(config, f, indent=4)
            f.close()
        embed = discord.Embed(
            title="Slot Owner Role",
            description=f"Role {role.mention} successfuly configured for slots owners",
            color=embed_color()
        )        
        embed.set_footer(text=footer())
        await ctx.respond(embed=embed)


    @commands.slash_command(name="config-channel-reset", description="Config Slot Owner Role")
    @option("channel", description="reset ping announce channel", type=discord.abc.GuildChannel)
    async def config_channel_reset(self, ctx, channel: discord.abc.GuildChannel):
        config = load_json()
        if ctx.author.id != int(config['buyer']):
            return await ctx.reply("You are not allowed to do this", ephemeral=True)
        config['reset_channel'] = channel.id
        with open("config.json", 'w') as f:
            json.dump(config, f, indent=4)
            f.close()
        embed = discord.Embed(
            title="Reset Ping Channel",
            description=f"Channel {channel.mention} successfuly configured for reset pîng",
            color=embed_color()
        )        
        embed.set_footer(text=footer())
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BuyerCommand(bot))

        

