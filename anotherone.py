import random

def random_greeting():
    # Kullanıcıdan isim al
    name = input("İsminiz nedir? ")

    # Rastgele bir sayı üret
    random_number = random.randint(1, 10)

    # Rastgele bir tebrik mesajı oluştur
    greetings = ["Tebrikler!", "Harika!", "Bravo!", "Mükemmel!", "Şahane!"]
    random_greeting = random.choice(greetings)

    # Oluşturulan mesajı ekrana yazdır
    print(f"{random_greeting} {name}! Rastgele bir sayıyla şanslı bir gün geçiriyorsunuz: {random_number}")

# Fonksiyonu çağır
random_greeting()
