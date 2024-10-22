# Github: https://github.com/Celentroft
# Don't be a skid, ty

import pytz
import json
import discord
from functions import *
from discord import option
from discord.ext import commands
from datetime import datetime, timedelta

class ExpandDuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="extend-subscription", description="Extend slot duration")
    @option("member", description="Slot owner", type=discord.Member)
    @option("days", description="Day amount will be added", type=int)
    async def extend_subscription(self, ctx, member:discord.member, days: int):
        config = load_json()
        if ctx.author.id not in config['whitelist'] and ctx.author.id != int(config['buyer']):
            return await ctx.respond("You are not allowed to do this", ephemeral=True)
        db_config = json.load(open("database.json", 'r'))
        for user in db_config:
            if db_config[user]['owner_id'] == member.id:
                converted = datetime.strptime(db_config[user]['end_date'], "%d/%m/%Y")
                updated = converted + timedelta(days=days)
                db_config[user]['end_date'] = updated.strftime("%d/%m/%Y")
                with open("database.json", 'w') as f:
                    json.dump(db_config, f, indent=4)
                    f.close()
                embed = discord.Embed(
                    title="Slot Extended",
                    description=f"Slot subscription for {member.mention} get {days}days more",
                    color=embed_color()
                )
                embed.set_footer(text=footer())
                await ctx.respond(embed=embed)
                return
        await ctx.respond(f"Member Not Found, please provide a slot owner", ephemeral=True)

def setup(bot):
    bot.add_cog(ExpandDuration(bot))

