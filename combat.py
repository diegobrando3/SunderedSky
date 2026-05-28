import random
import time

import printers
import monster_stats
import character

Canavar_prototypes = [
    ("Furkan", 30, 1, 25),
    ("Efe", 10, 5, 20),
    ("Enes", 20, 2.5, 15),
]


def choice(questions):
    for i, soru in enumerate(questions, start=1):
        print(f"[{i}] {soru}")
    return secis(len(questions))


def secis(count):
    while True:
        try:
            secim = int(input("Seçiminiz:"))
            if secim < 1 or secim > count:
                print("Geçersiz seçim")
            else:
                return secim
        except ValueError:
            print("Lütfen geçerli karakter girin.")


def gain_exp(player, amount):
    player.exp += amount
    printers.slow_print(f"Canavarı yendin! {amount} EXP kazandın.")
    leveled = False
    level_score = 100 * player.level
    while player.exp >= level_score:
        player.exp -= level_score
        player.level += 1
        level_score = 100 * player.level
        player.attack = 5 * player.level
        player.max_hp = 20 + (5 * player.level)
        player.defense = 1 + (player.level / 3)
        leveled = True
        printers.slow_print(f"Tebrikler! Seviye atladın: Level {player.level}")
    if leveled:
        printers.slow_print(f"Yeni hasarın {player.attack}, canın {player.max_hp} oldu.")
    character.save_to_json(character.character_stats(player))


def monsterattack(player, monster):
    damage_taken = player.take_damage(monster.damage)
    print(f"{player.name}'ın {player.hp} kadar canı kaldı!")
    print(f"Canavarın HP: {monster.hp}")
    if player.hp <= 0:
        printers.clear_screen()
        printers.slow_print("Hayır.")
        time.sleep(2)
        printers.slow_print(f"{player.name} HP'si yenilendi!")
        time.sleep(1)
        player.heal_full()
        printers.slow_print(f"{player.name}'ın canı {player.hp} oldu!")
        time.sleep(2.5)
        printers.clear_screen()
        print(monster)


def playerturn(player, monster):
    print("Sıra sende!")
    while True:
        try:
            playerchoice = int(input("1. Saldır | 2. Savun "))
            if playerchoice == 1:
                print("Saldırdın!")
                monster.take_damage(player.attack)
                print(f"Canavarın kalan HP: {monster.hp}")
                time.sleep(3)
                printers.clear_screen()
                if not monster.is_alive:
                    gain_exp(player, monster.exp)
                    break
                monsterattack(player, monster)
            elif playerchoice == 2:
                print("Savunma yaptın!")
                monsterattack(player, monster)
                time.sleep(2)
                printers.clear_screen()
            else:
                print("Geçerli seçenek girin!")
        except ValueError:
            print("Geçerli seçenek girin!")


def monsterencounter(player):
    proto = random.choice(Canavar_prototypes)
    randommonster = monster_stats.Monster(*proto)
    printers.slow_print(f"Karşında bir canavar belirdi: {randommonster}")
    playerturn(player, randommonster)
