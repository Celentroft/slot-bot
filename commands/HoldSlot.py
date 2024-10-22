# Github: https://github.com/Celentroft
# Don't be a skid, ty

import discord
from functions import *
from Views.EndView import *
from discord.ext import commands

class HoldSlot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="hold", description="Hold a slot")
    async def hold(self, ctx):
        config = load_json()
        if ctx.author.id not in config['whitelist'] and ctx.author.id != int(config['buyer']):
            return await ctx.reply("You are not allowed to do this", ephemeral=True)
        db_config = json.load(open("database.json", 'r'))
        for user in db_config:
            if db_config[user]['channel_id'] == ctx.channel.id:
                member = discord.utils.get(ctx.guild.members, id=db_config[user]['owner_id'])
                if member:
                    perms_holded = {
                        ctx.guild.default_role: discord.PermissionOverwrite(
                            create_instant_invite=True,
                            add_reactions=True, 
                            read_messages=True, 
                            view_channel=True, 
                            send_messages=False, 
                            read_message_history=True,
                        ),
                        member: discord.PermissionOverwrite(
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
                        )
                    }
                    await ctx.channel.edit(overwrites=perms_holded)
                    embed = discord.Embed(
                        title="Slot On Hold",
                        description="This slot is on hold right now",
                        color=embed_color()
                    )
                    embed.set_footer(text=footer())
                    view = discord.ui.View(timeout=None)
                    view.add_item(RemoveSlot(self.bot))
                    view.add_item(UnHodl(self.bot))
                    return await ctx.respond(embed=embed, view=view)
                
        await ctx.respond("This channel is not a slot, please use this command into a slot channel", ephemeral=True)

def setup(bot):
    bot.add_cog(HoldSlot(bot))