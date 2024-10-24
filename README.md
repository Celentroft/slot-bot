# 🚀 discord-slot-bot

## 📜 Description

This bot is intended for discord marketplaces, it has several functions, such as managing subscription days, pings, permissions and access, it can also hold and unhold slots, buttons are available for more pleasant use

## 🛠️ Commands
```
/add-ping: Add pings per day for a slot owner
/backup: Backup your slot with backup key
/config-channel-reset: Configuration of reset ping announcement channel 
/config-role: Configuration of role added for slots owners
/create-slot: Create a slot for a member
/extend-subscription: Add time for a slots subscription
/hold: Hold a slot
/remove-ping: Remove pign per day for a slot owner
/unwl: Remove an user from the whitelist
/wl: add an user into the whitelist
/wl-list: Show all users into the whitelist
/help: Show help command
```

## 📦 Installation

Clone this repository:

```
git clone https://github.com/Scarlxrd211/slot-bot.git 
```

Install requirements: 

```
pip install -r requirements.txt
```

Complete config.json file:

```json
{
    "token": "your_bot_token", 
    "color": "hex_color_code",
    "guildid": null, -> Guild id 
    "buyer": null, -> Bot owner id
    "whitelist": [], 
    "reset_channel": null, -> Reset ping channel id
    "seller_roles": null -> Slot owner role id
}
```

Run script:

```
python main.py
```

# ✨ Star

If you like this or if you just use it, please don't forgot to star this !

# 💎 Support

<a href="https://t.me/scarlxrd_1337" target="_blank"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a> 
<a href="https://discord.gg/purity-dev" target="_blank"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"></a> 
