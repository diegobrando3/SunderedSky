# ⚔️ Python Text RPG

Terminalde oynanan, sıra tabanlı bir metin macera oyunu.

## 🎮 Oyun Hakkında

Karakterini oluştur, canavarlarla savaş, seviye atla ve güçlen. Her savaş sonrası kazandığın EXP ile karakterin gelişir; saldırı gücün, canın ve savunman artar.

## 🚀 Kurulum

**Gereksinimler:**
- Python 3.x

**Oyunu başlat:**

```bash
# 1. Repoyu klonla
git clone https://github.com/diegobrando3/SunderedSky

# 2. Klasöre gir
cd kufur-makinesi

# 3. Çalıştır
python main.py
```

## 📁 Dosya Yapısı

```
├── main.py            # Ana oyun dosyası
├── monster_stats.py   # Canavar sınıfı ve istatistikleri
├── charstats.json     # Karakter kayıt dosyası (otomatik oluşur)
└── README.md
```

## ⚙️ Özellikler

- Karakter oluşturma (isim girişi)
- Sıra tabanlı savaş sistemi (Saldır / Savun)
- EXP kazanma ve seviye atlama
- Seviye başına artan hasar, can ve savunma
- Karakter istatistiklerini JSON'a otomatik kaydetme
- Rastgele canavar seçimi
- Tutorial savaşı (kaçamazsın 😄)

## 📊 Karakter İstatistikleri

| Stat | Formül |
|---|---|
| Attack Damage | `5 × level` |
| Max Health | `20 + (5 × level)` |
| Defense | `1 + (level / 3)` |
| EXP to Level | `100 × current level` |

## 👾 Canavarlar (Şimdilik)

| İsim | HP | Hasar | EXP |
|---|---|---|---|
| Furkan | 30 | 1 | 25 |
| Efe | 10 | 5 | 20 |
| Enes | 20 | 2.5 | 15 |

## 🔧 Bilinen Sorunlar

- Savaş sırasında yeniden doğduğunda bazı yazılar ekrana gelmiyor
- Savunma yapıldığında `clear_screen()` yanlış yeri temizliyor
