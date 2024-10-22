# Github: https://github.com/Celentroft
# Don't be a skid, ty

import pytz
import discord
from functions import *
from datetime import datetime
from Views.EndView import RemoveSlot
from discord.ext import commands, tasks

class SlotsManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.slotsmanager.start()

    @tasks.loop(hours=24)
    async def slotsmanager(self):
        now = datetime.now(pytz.timezone("Europe/Paris"))
        formatted = now.strftime("%d/%m/%Y")
        db_config = json.load(open("database.json", 'r'))
        config = load_json()
        for user in db_config:
            end_date = db_config[user]['end_date']
            if end_date == formatted:
                guild = discord.utils.get(self.bot.guilds, id=config['guildid'])
                if guild:
                    member = discord.utils.get(guild.members, id=db_config[user]['owner_id'])
                    channel = discord.utils.get(guild.text_channels, id=db_config[user]['channel_id'])
                    role = discord.utils.get(guild.roles, id=config['seller_roles'])
                    if member and channel and role:
                        perms = {
                            guild.default_role: discord.PermissionOverwrite(
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
                                send_messages=False, 
                                read_message_history=True,   
                                attach_files=True,
                                mention_everyone=True,
                                use_slash_commands=True,
                                embed_links=True                 
                            )
                        }
                        await channel.edit(overwrites=perms)
                        await member.remove_roles(role)
                        embed = discord.Embed(
                            title="Slot Ended",
                            description=f"Slot are ended, Contact staff to expand subscription",
                            color=embed_color()
                        )
                        embed.set_footer(text=footer())
                        embed.set_thumbnail(url=guild.icon)
                        view = discord.ui.View(timeout=None)
                        view.add_item(RemoveSlot(self.bot))
                        await channel.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(SlotsManager(bot))