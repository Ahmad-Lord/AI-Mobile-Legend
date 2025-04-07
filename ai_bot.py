# ai_bot.py
# Simple AI Bot untuk rekomendasi hero Mobile Legends

def rekomendasi_hero(pick_musuh):
    counter_hero = {
        "Layla": "Natalia",
        "Zilong": "Khufra",
        "Gusion": "Chou",
        "Lesley": "Helcurt",
        "Miya": "Saber"
    }

    return counter_hero.get(pick_musuh, "Tigreal (default tank)")

if __name__ == "__main__":
    print("=== AI Mobile Legend Bot ===")
    pick = input("Musuh pick hero apa? ")
    saran = rekomendasi_hero(pick)
    print(f"Saran hero terbaik untuk counter: {saran}") 
Add simple AI bot for ML strategy
