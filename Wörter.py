import random
Wörter = [
    ["das Haus","la casa"],
    ["die Katze","el gato"],
    ["die Maus","el raton"],
    ["das Flugzeug","el avión"],
    ["der Zug","el tren"],
    ["das Schiff","el barco"],
    ["das Fahrrad","la bicicleta"],    
    ]

Antwort = ""

while Antwort != "Stopp":
    Wort = random.choice(Wörter)
    
    i = random.randint(0, 1)
    j = 1-i
    if i == 0:
        Antwort = input("Wie sagt man '" + Wort[i] + "' auf Spanisch? ")
    else:
        Antwort = input("Wie sagt man '" + Wort[i] + "' auf Deutsch? ")
    
    if Antwort == Wort[j]:
        print("Richtig! ")
    else:
        print("Die Antwort war '" + Wort[j] + "'")
        

    
    
    
