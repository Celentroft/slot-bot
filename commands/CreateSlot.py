# Github: https://github.com/Celentroft
# Don't be a skid, ty

import pytz
import json
import discord
from discord import option
from discord.ext import commands
from datetime import datetime, timedelta
from functions import load_json, embed_color, backupkey, footer

class CreateSlotCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="create-slot", description="Create a slot")
    @option("member", description="Member own slot", type=discord.Member)
    @option("name", description="Channel Name", type=str)
    @option("category", description="Categorie where slot created", type=discord.CategoryChannel)
    @option("duration", description="Slot duration in days", type=int)
    @option("here per day", description="Max here ping per day", type=int)
    @option("everyone per day", description="Max everyone ping per day", type=int)
    async def createslots(self, ctx, member: discord.Member, name: str, category: discord.CategoryChannel, duration: int, here: int, everyone: int):
        await ctx.defer()
        config = load_json()
        if ctx.author.id not in config['whitelist'] and ctx.author.id != int(config['buyer']):
            return await ctx.respond('You are not allowed to do this', ephemeral=True)
        with open("database.json", 'r') as f:
            db_config = json.load(f)
            for elem in db_config:
                if elem == str(member.name):
                    return await ctx.respond("This member already have a slot", ephemeral=True)
        end_date = (datetime.now(pytz.timezone("Europe/Paris")) + timedelta(days=duration)).strftime("%d/%m/%Y")
        role_to_add = discord.utils.get(ctx.guild.roles, id=int(config['seller_roles']))
        if not role_to_add:
            return await ctx.respond(f"The seller role are undefined, please setup a valid role", ephemeral=True)
        backup = backupkey()
        perms = {
            ctx.guild.default_role: discord.PermissionOverwrite(
                create_instant_invite=True,
                add_reactions=True, 
                read_messages=True, 
                view_channel= True, 
                send_messages=False, 
                read_message_history=True,
                ),
            member: discord.PermissionOverwrite(
                create_instant_invite=True,
                add_reactions=True, 
                read_messages=True, 
                view_channel= True, 
                send_messages=True, 
                read_message_history=True,   
                attach_files=True,
                mention_everyone=True,
                use_slash_commands=True,
                embed_links=True                 
            )
        }
        channel = await category.create_text_channel(name=name, overwrites=perms)
        payload = {
            "owner_id": int(member.id),
            "backupkey": str(backup),
            "duration": int(duration),
            "category_id": int(category.id),
            "channel_id": int(channel.id),
            "here": 0,
            "max_here": int(here),
            "everyone": 0,
            "max_everyone": int(everyone),
            "end_date": str(end_date)
        }
        with open("database.json", 'r') as f:
            db_config = json.load(f)
            f.close()
        db_config[str(member.name)] = payload
        with open("database.json", 'w') as f:
            json.dump(db_config, f, indent=4)
            f.close()
        embed = discord.Embed(
            title="Slot",
            description=f"""
```
Purshased Date -> {datetime.now(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y")}
```
```
Pushase End At -> {end_date}
```
**Ping Informations**
```
x{here} @here ping per day
x{everyone} @everyone ping per day
```
**Always Use MiddleMan**
**If You Buy, You Already Accept Tos**
""",
            color=embed_color()
        )
        embed.set_footer(text=footer())
        embed.set_thumbnail(url=member.avatar)
        await member.add_roles(role_to_add)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Backup Key",
            description=f"Here Your Backup Key: {backup}",
            color=embed_color()
        )
        embed.set_footer(text=footer())
        try:
            await member.send(embed=embed)
        except Exception as e:
            await ctx.channel.send(f"I can't send backup key into {member.mention}, send it manually: {backupkey}", ephemeral=True)
        embed = discord.Embed(
            title="Slot Created",
            description=f"Slot Created for {member.mention} in {channel.mention}.",
            color=embed_color()
        )
        embed.set_footer(text=footer())
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(CreateSlotCommand(bot))
