# Github: https://github.com/Celentroft
# Don't be a skid, ty

import json
import discord
from functions import *
from discord import option
from discord.ext import commands

class BackupSlots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="backup", description="Get back your slot if you got termed")
    @option("backup_key", description="backup key", type=str)
    async def backup(self, ctx, backup_key: str):
        await ctx.defer()
        db_config = json.load(open("database.json", 'r')) 
        for user in db_config:
            if db_config[user]['backupkey'] == backup_key:
                old_member = discord.utils.get(ctx.guild.members, id=db_config[user]['owner_id'])
                if old_member.id == ctx.author.id:
                    return await ctx.respond("You can't backup your slot if you are already the actual owner", ephemeral=True)
                db_config[user]['owner_id'] = ctx.author.id
                channel = discord.utils.get(ctx.guild.text_channels, id=db_config[user]['channel_id'])
                with open("database.json", 'w') as f:
                    json.dump(db_config, f, indent=4)
                    f.close()
                if channel:
                    embed = discord.Embed(
                        title="Backup Slot",
                        description="Your backup key are valid. You will get your slot back right now",
                        color=embed_color()
                    )
                    embed.set_footer(text=footer())
                    perms_holded = {
                        ctx.guild.default_role: discord.PermissionOverwrite(
                            create_instant_invite=True,
                            add_reactions=True, 
                            read_messages=True, 
                            view_channel=True, 
                            send_messages=False, 
                            read_message_history=True,
                        ),
                        ctx.author: discord.PermissionOverwrite(
                            create_instant_invite=True,
                            add_reactions=True, 
                            read_messages=True, 
                            view_channel=True, 
                            send_messages=True, 
                            read_message_history=True,   
                            attach_files=True,
                            mention_everyone=True,
                            use_slash_commands=True,
                            embed_links=True                 
                        ),
                        old_member: discord.PermissionOverwrite(
                            create_instant_invite=True,
                            add_reactions=True, 
                            read_messages=True, 
                            view_channel=True, 
                            send_messages=False, 
                            read_message_history=True,
                        ),
                    }
                    await channel.edit(overwrites=perms_holded)
                    await ctx.respond(embed=embed)
                    return

        await ctx.respond("Your backup key are invalid, please retry with a valid backup key", ephemeral=True)

def setup(bot):
    bot.add_cog(BackupSlots(bot))