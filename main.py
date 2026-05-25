import time
import json
import os
import keyboard

CHARSTAT="charstats.json"

level=1
#gained_exp=monster_exp
exp=0
#exp=exp+gained_exp
level_score=100*level
if exp >= level_score:
    level=level+1
attackdamage=5*level
health=20+(5*level)
defense=1

name=input("Karakterinizin ismini girin: ")
time.sleep(1)
print(f"Karakteriniz oluşturuldu. Merhaba {name}!")

def character_stats(name, level, attackdamage, health, defense):
    stat = {
        "Karakter": name,
        "stats": {
            "Level": level,
            "AD": attackdamage,
            "Health": health,
            "Defense": defense
        }
    }
    return stat

def save_to_json(stats):
    try:
        with open(CHARSTAT, "w", encoding="utf-8") as f:
            tum_veriler = json.load(f)
    except:
        tum_veriler = []
    
    tum_veriler.append(stats)
    
    if len(tum_veriler) > 100:        # son 100 kaydı tut
        tum_veriler = tum_veriler[-100:]
    
    with open(CHARSTAT, "w", encoding="utf-8") as f:
        json.dump(tum_veriler, f, ensure_ascii=False, indent=4)

stat = character_stats(name, level, attackdamage, health, defense)
save_to_json(stat)

i=0
def secis(i):
    while True:
        secim=int(input("Seçiminiz:"))
        if secim!=i and secim > i:
            print("Geçersiz seçim")
        else:
            break
def unrelated_choice():
    pass

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

questions=["Nasıl?","Ne?"]
def choice(questions):
    for i, soru in enumerate(questions, start=1):
        print(f"[{i}] {soru}")
    secis(i)

choice(questions)
print(health)
print(CHARSTAT)