import json

CHARSTAT = "charstats.json"


def character_stats(player):
    return {
        "Karakter": player.name,
        "stats": {
            "Level": player.level,
            "Total Exp": player.exp,
            "Next": f"{player.exp} / {100 * player.level}",
            "AD": player.attack,
            "Health": f"{player.hp} / {player.max_hp}",
            "Defense": player.defense,
        },
    }


def save_to_json(stats):
    with open(CHARSTAT, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)
