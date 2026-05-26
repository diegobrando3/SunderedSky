import time
import json
import os
import random
import monster_stats

random.seed()
CHARSTAT="charstats.json"

level=1

exp=0
level_score=100*level
if exp >= level_score:
    level=level+1
attackdamage=5*level
health=20+(5*level)
defense=1+(level/3)
global maxhp
maxhp=20+(5*level)

Canavar_prototypes = [
    ("Furkan", 30, 1, 25),
    ("Efe", 10, 5, 20),
    ("Enes", 20, 2.5, 15),
]
def monsterencounter():
    proto = random.choice(Canavar_prototypes)
    randommonster = monster_stats.Monster(*proto)
    print(f"Karşında bir canavar belirdi: {randommonster}")
    playerturn(randommonster)
name=input("Karakterinizin ismini girin: ")
time.sleep(1)
print(f"Karakteriniz oluşturuldu. Merhaba {name}!")

def character_stats(name, level, attackdamage, health, defense):
    stat = {
        "Karakter": name,
        "stats": {
            "Level": level,
            "EXP": exp,
            "Next": f"{exp} / {level_score}",
            "AD": attackdamage,
            "Health": f"{health} / {maxhp}",
            "Defense": defense
        }
    }
    return stat
#Karakter statlarını .json dosyasına yazar
def save_to_json(stats):
    with open(CHARSTAT, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)

stat = character_stats(name, level, attackdamage, health, defense)
save_to_json(stat)

#canavardan exp düşmesi ve level ile kazandığımız statlarımızı kontrol eden fonksiyon
def gain_exp(amount):
    global exp, level, attackdamage, health, level_score
    exp += amount
    print(f"Canavarı yendin! {amount} EXP kazandın.")
    leveled = False
    while exp >= level_score:
        exp -= level_score
        level += 1
        level_score = 100 * level
        attackdamage = 5 * level
        health = 20 + (5 * level)
        leveled = True
        print(f"Tebrikler! Seviye atladın: Level {level}")
    if leveled:
        print(f"Yeni hasarın {attackdamage}, canın {health} oldu.")
    save_to_json(character_stats(name, level, attackdamage, health, defense))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

i=0
#geçersiz seçim olmasın diye
def secis(i):
    while True:
        try:
            secim=int(input("Seçiminiz:"))
            if secim!=i and secim > i:
                print("Geçersiz seçim")
            else:
                break
        except:
            print("Lütfen geçerli karakter girin.")
    return secim
#canavarın sırası
def monsterattack(monster):
    global health
    health -= (monster.damage / defense)
    if health < 0:
        health = 0
    print(f"{name}'ın {health} kadar canı kaldı!")
    print(f"Canavarın HP: {monster.hp}")
    if health <= 0:
        print("Hayır.")
        print(f"{name} HP'si yenilendi!")
        health = 20 + (5 * level)
        print(f"{name}'ın canı {health} oldu!")
        clear_screen()
        print(monster)
#oyuncunun sırası
def playerturn(monster):
    print("Sıra sende!")
    while True:
        try:
            playerchoice = int(input("1. Saldır | 2. Savun "))
            if playerchoice == 1:
                print("Saldırdın!")
                monster.take_damage(attackdamage)
                print(f"Canavarın kalan HP: {monster.hp}")
                time.sleep(3)
                clear_screen()
                if not monster.is_alive:
                    gain_exp(monster.exp)
                    break
                monsterattack(monster)
            elif playerchoice == 2:
                print("Savunma yaptın!")
                monsterattack(monster)
                time.sleep(2)
                clear_screen()
            else:
                print("Geçerli seçenek girin!")
        except ValueError:
            print("Geçerli seçenek girin!")

#Yavaş ve güzel gözükerek yazar 
#örnek: slow_print("Merhaba!", delay=0.1)
#delay yazının ne hızda yazılacağını gösterir

def slow_print(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

questions=["deneme1","deneme2"]
def choice(questions):
    for i, soru in enumerate(questions, start=1):
        print(f"[{i}] {soru}")
    return secis(i)

choice(questions)

questions=["Evet!", "Hayır.."]
slow_print("Merhaba.")
time.sleep(1)
clear_screen()
slow_print("Önünde bir yaratık var, dövüşecek misin?")
selected = choice(questions)
# spawn a fresh Monster instance from prototypes for this encounter
proto = random.choice(Canavar_prototypes)
randommonster = monster_stats.Monster(*proto)
if selected == 1:
    clear_screen()
    print(f"Karşında bir canavar belirdi: {randommonster}")
    playerturn(randommonster)
else:
    slow_print("Bu bir tutorial olduğu için zorla savaşacaksın :)")
    time.sleep(2)
    clear_screen()
    monsterencounter()



#Canavar ile savaşırken yeniden doğduğumuzdaki yazılar girmiyor.
#Savunma yapıldığında clear_screen() düzgün çalışmıyor, yanlış yeri siliyor.