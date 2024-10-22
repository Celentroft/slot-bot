# Github: https://github.com/Celentroft
# Don't be a skid, ty

import pytz
import discord
from functions import *
from datetime import datetime
from discord.ext import commands, tasks

class ResetPingManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.pingmanager.start()

    @tasks.loop(minutes=1)
    async def pingmanager(self):
        now = datetime.now(pytz.timezone("Europe/Paris"))
        if now.hour == int("00") and now.minute == int("50"):
            db_config = json.load(open('database.json', 'r'))
            config = load_json()
            guild = discord.utils.get(self.bot.guilds, id=config["guildid"])
            if guild:
                reset_channel = discord.utils.get(guild.text_channels, id=config["reset_channel"])
                role = discord.utils.get(guild.roles, id=config['seller_roles'])
                if reset_channel and role:
                    user_count = 0
                    for user in db_config:
                        db_config[user]['here'] = 0
                        db_config[user]['everyone'] = 0
                        with open("database.json", 'w') as f:
                            json.dump(db_config, f, indent=4)
                            f.close()
                        user_count += 1

                    embed = discord.Embed(
                        title="Ping reset",
                        description=f"@here and @everyone ping are reset for {user_count}{role.mention}",
                        color=embed_color()
                    )
                    embed.set_footer(text=footer())
                    embed.set_thumbnail(url=guild.icon)
                    await reset_channel.send(embed=embed, content=role.mention)

def setup(bot):
    bot.add_cog(ResetPingManager(bot))