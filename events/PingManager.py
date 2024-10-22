# Github: https://github.com/Celentroft
# Don't be a skid, ty

import json
import discord
from functions import *
from discord.ext import commands
from Views.EndView import RemoveSlot, UnHodl

class PingManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "@everyone" in message.content or "@here" in message.content:
            with open("database.json", 'r') as f:
                db_config = json.load(f)
                
            for user in db_config:
                if user == message.author.name:
                    channel = discord.utils.get(message.guild.text_channels, id=db_config[user]['channel_id'])
                    if not channel or message.channel.id != channel.id:
                        continue
                    
                    max_everyone = db_config[user]["max_everyone"]
                    everyone_rn = db_config[user]['everyone']
                    max_here = db_config[user]['max_here']
                    here_rn = db_config[user]['here']
                    
                    if "@everyone" in message.content:
                        if everyone_rn < max_everyone:
                            db_config[user]["everyone"] = everyone_rn + 1
                            with open("database.json", 'w') as f:
                                json.dump(db_config, f, indent=4)
                            embed = discord.Embed(
                                title="Use MM To Be Safe",
                                description=f"{max_everyone - (everyone_rn + 1)}x @everyone ping left\n{max_here - here_rn}x @here ping left",
                                color=embed_color()
                            )
                            embed.set_footer(text=footer())
                            await message.channel.send(embed=embed)
                        else:
                            perms_holded = {
                                message.guild.default_role: discord.PermissionOverwrite(
                                    create_instant_invite=True,
                                    add_reactions=True, 
                                    read_messages=True, 
                                    view_channel=True, 
                                    send_messages=False, 
                                    read_message_history=True,
                                ),
                                message.author: discord.PermissionOverwrite(
                                    create_instant_invite=True,
                                    add_reactions=True, 
                                    read_messages=True, 
                                    view_channel=True, 
                                    send_messages=False, 
                                    read_message_history=True,   
                                    attach_files=True,
                                    mention_everyone=True,
                                    use_slash_commands=True,
                                    embed_links=True                 
                                )
                            }
                            await channel.edit(overwrites=perms_holded)
                            embed = discord.Embed(
                                title="OverPing Detected",
                                description=f"Slot on hold because overping detected",
                                color=embed_color()
                            )
                            embed.set_footer(text=footer())
                            view = discord.ui.View(timeout=None)
                            view.add_item(RemoveSlot(self.bot))
                            view.add_item(UnHodl(self.bot))
                            await channel.send(embed=embed, view=view)

                    elif "@here" in message.content:
                        if here_rn < max_here:
                            db_config[user]["here"] = here_rn + 1
                            with open("database.json", 'w') as f:
                                json.dump(db_config, f, indent=4)
                            embed = discord.Embed(
                                title="Use MM To Be Safe",
                                description=f"{max_everyone - everyone_rn}x @everyone ping left\n{max_here - (here_rn + 1)}x @here ping left",
                                color=embed_color()
                            )
                            embed.set_footer(text=footer())
                            await message.channel.send(embed=embed)
                        else:
                            perms_holded = {
                                message.guild.default_role: discord.PermissionOverwrite(
                                    create_instant_invite=True,
                                    add_reactions=True, 
                                    read_messages=True, 
                                    view_channel=True, 
                                    send_messages=False, 
                                    read_message_history=True,
                                ),
                                message.author: discord.PermissionOverwrite(
                                    create_instant_invite=True,
                                    add_reactions=True, 
                                    read_messages=True, 
                                    view_channel=True, 
                                    send_messages=False, 
                                    read_message_history=True,   
                                    attach_files=True,
                                    mention_everyone=True,
                                    use_slash_commands=True,
                                    embed_links=True                 
                                )
                            }
                            await channel.edit(overwrites=perms_holded)
                            embed = discord.Embed(
                                title="OverPing Detected",
                                description=f"Slot on hold because overping detected",
                                color=embed_color()
                            )
                            embed.set_footer(text=footer())
                            view = discord.ui.View(timeout=None)
                            view.add_item(RemoveSlot(self.bot))
                            view.add_item(UnHodl(self.bot))
                            await channel.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(PingManager(bot))