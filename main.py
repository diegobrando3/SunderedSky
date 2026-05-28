import time
import random

import printers
import gamesave
import character
from player import Player
import combat


def load_or_create_player():
    save_data = gamesave.load_game()
    if save_data and save_data.get("player"):
        player_data = save_data["player"]
        player = Player(
            player_data.get("name", "Bilinmeyen"),
            level=player_data.get("level", 1),
            exp=player_data.get("exp", 0),
            hp=player_data.get("hp"),
            max_hp=player_data.get("max_hp"),
            attack=player_data.get("attack"),
            defense=player_data.get("defense")
        )
        return player, save_data.get("current_scene", 1)
    return None, None


def main():
    random.seed()
    player, current_scene = load_or_create_player()

    name = input("Karakterinizin ismini girin: ")
    time.sleep(1)
    printers.slow_print(f"Karakteriniz oluşturuldu. Merhaba {name}!")

    if player is None:
        player = Player(name)
        current_scene = 1

    gamesave.save_game(player, current_scene)
    character.save_to_json(character.character_stats(player))

    questions = ["deneme1", "deneme2"]
    combat.choice(questions)

    questions = ["Evet!", "Hayır.."]
    printers.slow_print("Merhaba.")
    time.sleep(1)
    printers.clear_screen()
    printers.slow_print("Önünde bir yaratık var, dövüşecek misin?")
    selected = combat.choice(questions)

    if selected == 1:
        printers.clear_screen()
        combat.monsterencounter(player)
    else:
        printers.slow_print("Bu bir tutorial olduğu için zorla savaşacaksın :)", delay=0.01)
        time.sleep(2)
        printers.clear_screen()
        combat.monsterencounter(player)


if __name__ == "__main__":
    main()
