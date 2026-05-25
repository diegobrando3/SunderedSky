import time
import json
import os
import keyboard

level=1
#gained_exp=monster_exp
exp=0
#exp=exp+gained_exp
level_score=200*level
if exp >= level_score:
    level=level+1
attackdamage=5*level
health=20+(5*level)
defense=1



    


def character_creation():
    name=input("Karakterinizin ismini girin: ")
    time.sleep(1)
    print(f"Karakteriniz oluşturuldu. Merhaba {name}!")
def character_stats():
    stats={
        "Karakter": {name},
        stats:{

        }

    }
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
    secis(i

choice(questions)
print(health)