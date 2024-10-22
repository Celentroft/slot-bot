# Github: https://github.com/Celentroft
# Don't be a skid, ty

import asyncio
import discord
from functions import *
from discord.ui import Button

class RemoveSlot(Button):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(
            label=f"Delete",
            style=discord.ButtonStyle.red
        )

    async def callback(self, interaction: discord.Interaction):
        config = load_json()
        if interaction.user.id not in config['whitelist'] and interaction.user.id != int(config['buyer']):
            return await interaction.response.send_message(f"You are not allowed to do this", ephemeral=True)
        db_config = json.load(open("database.json", 'r'))
        if db_config == {}:
            return
        for user in db_config:
            if db_config[user]["channel_id"] == interaction.channel.id:
                del db_config[user]
                with open("database.json", 'w') as f:
                    json.dump(db_config, f, indent=4)
                    f.close()
                await interaction.response.send_message(f"Channel will be removed and user was remove from database", ephemeral=True)
                await asyncio.sleep(5)
                await interaction.channel.delete()  
                break

class UnHodl(Button):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(
            label="UnHold",
            style=discord.ButtonStyle.green
        )
    
    async def callback(self, interaction: discord.Interaction):
        config = load_json()
        if interaction.user.id not in config['whitelist'] and interaction.user.id != int(config['buyer']):
            return await interaction.response.send_message(f"You are not allowed to do this", ephemeral=True)
        db_config = json.load(open("database.json", 'r'))
        for user in db_config:
            if db_config[user]['channel_id'] == interaction.channel.id:
                member = discord.utils.get(interaction.guild.members, id=db_config[user]['owner_id'])
                if member:
                    perms_unhold = {
                        interaction.guild.default_role: discord.PermissionOverwrite(
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
                    await interaction.channel.edit(overwrites=perms_unhold)
                    await interaction.response.send_message("Slot successfuly unholded", ephemeral=True)
                    break

