import json
import os
from datetime import datetime

SAVE_FILE = "save.json"

def save_game(player, current_scene=1):
    save_data = {
        "player": {
            "name": player.name,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "attack": player.attack,
            "level": getattr(player, "level", 1),
            "exp": getattr(player, "exp", 0)
        },
        "current_scene": current_scene,
        "last_saved": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=4)
    
    print("Oyun kaydedildi!")


def load_game():
    if not os.path.exists(SAVE_FILE):
        print("Henüz kayıt bulunamadı.")
        return None
    
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            save_data = json.load(f)
        
        print(f"Kayıt yüklendi! ({save_data['last_saved']})")
        return save_data
    except:
        print("Kayıt dosyası bozuk.")
        return None


def delete_save():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("Kayıt silindi.")