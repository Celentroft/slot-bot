# Github: https://github.com/Celentroft
# Don't be a skid, ty

import json
import random

def load_json():
    with open("config.json", 'r') as f:
        config = json.load(f)
        return config
    
def embed_color() -> int:
    config = load_json()
    return int(config['color'], 16)

def footer() -> str:
    return "Slot bot by Scarlxrd"

def backupkey(lenght=20) -> str:
    return "".join(random.choice("ABCDEFGHIJKLMONPQRSTUVWXYZ") for _ in range(lenght))