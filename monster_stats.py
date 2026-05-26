import random
import os


takedown=["yere yığıldı!","kaçmaya çalışırken taşa takıldı. Öldü..","gözlerindeki ışık yavaşça söndü.","havalı bir ölüm pozu vermeye çalıştı.",
          "acı bir çığlık atarak küle dönüştü.","yarasını tutarak geriye doğru adımladı, gözlerinde pişmanlık vardı.","yıllardır sürdürdüğü bu lanetli nöbetin bitmesine sevinir gibi gülümsedi.",
          "karanlığın içinden gelen ruhlar onu nazikçe sarıp sonsuzluğa götürdü.","gözlerindeki öfke yerini derin bir huzura bıraktı ve yavaşça silindi.","etrafına saçılan kadim ışık huzmeleriyle birlikte yok oldu.",
          "silahını gururla göğsüne bastırarak son nefesini verdi."]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Monster:
    # Canavar ilk yaratıldığında çalışacak olan yapıcı (constructor) metot
    def __init__(self, mname, mhp, mdamage, monster_exp):
        self.name = mname
        self.hp = mhp
        self.damage = mdamage
        self.exp = monster_exp
        self.is_alive = True

    # Canavarın durumunu ekrana yazdırmak için bir metot
    def status_report(self):
        if self.is_alive:
            return f" {self.name} | HP: {self.hp} | Hasar: {self.damage}"
        else:
            return f" {self.name} (Elendi)"

    # Canavar hasar aldığında çalışacak metot
    def take_damage(self, amount):
        if self.is_alive:
            self.hp -= amount
            print(f"-> {self.name} {amount} hasar aldı!")
            if self.hp <= 0:
                self.is_alive = False
                clear_screen()
                print(f" {self.name} {random.choice(takedown)}")
    def __str__(self):
        return self.status_report()
    def __repr__(self):
        return f"Monster(name={self.name!r}, hp={self.hp}, damage={self.damage}, exp={self.exp})"