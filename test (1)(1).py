class cal():
    #Klassi konstruktor, mis võtab kaks numbrit parameetriteks
    def __init__(self, a, b):
        #Salvestame esimese numbri objekti muutujasse
        self.a = a
        #Salvestame teise numbri objekti muutujasse
        self.b = b

    #Liitmise funktsioon
    def liitmine(self):
        #Tagastame kahe numbri summa
        return self.a + self.b

    #Lahutamise funktsioon
    def lahutamine(self):
        #Tagastame esimesest numbrist teise numbri lahutamise tulemuse
        return self.a - self.b

    #Korrutamise funktsioon
    def korrutamine(self):
        #Tagastame kahe numbri korrutise
        return self.a * self.b

    #Jagamise funktsioon
    def jagamine(self):
        #Kontrollime, kas teine number on null
        if self.b == 0:
            #Kui on null, tagastame veateate
            return "Viga: nulliga ei saa jagada!"
        #Kui ei ole null, tagastame jagamise tulemuse
        return self.a / self.b

    #Astendamise funktsioon
    def astendamine(self):
        #Tagastame esimese numbri astendatuna teise numbri astmesse
        return self.a ** self.b

    #Ruutjuure funktsioon
    def ruutjuur(self):
        #Kontrollime, kas esimene number on negatiivne
        if self.a < 0:
            #Kui on negatiivne, tagastame veateate
            return "Viga: negatiivse arvu ruutjuur!"
        #Tagastame esimese numbri ruutjuure (astendame 0.5 astmesse)
        return self.a ** 0.5

    #Jäägi leidmise funktsioon
    def jaak(self):
        # Kontrollime, kas teine number on null
        if self.b == 0:
            #Kui on null, tagastame veateate
            return "Viga: nulliga ei saa jagada!"
        #Tagastame jagamise jäägi (modulo operaator)
        return self.a % self.b

    # Absoluutväärtuse funktsioon
    def absoluut(self):
        #Tagastame esimese numbri absoluutväärtuse
        return abs(self.a)

    #Keskmise leidmise funktsioon
    def keskmine(self):
        #Tagastame kahe numbri aritmeetilise keskmise
        return (self.a + self.b) / 2

def menu():
    #Prindime tühja rea menüü ette
    print("\n=== KALKULAATOR ===")
    #Prindime esimese valiku - liitmine
    print("1. Liitmine")
    #Prindime teise valiku - lahutamine
    print("2. Lahutamine")
    #Prindime kolmanda valiku - korrutamine
    print("3. Korrutamine")
    #Prindime neljanda valiku - jagamine
    print("4. Jagamine")
    #Prindime viienda valiku - astendamine
    print("5. Astendamine")
    #Prindime kuuenda valiku - ruutjuur
    print("6. Ruutjuur")
    #Prindime seitsmenda valiku - jäägi leidmine
    print("7. Jäägi leidmine")
    #Prindime kaheksanda valiku - absoluutväärtus
    print("8. Absoluutväärtus")
    #Prindime üheksanda valiku - keskmine
    print("9. Keskmine")
    #Prindime nulli valiku - väljumine programmist
    print("0. Välju")

#Prindime tervituse kasutajale
print("Tere tulemast kalkulaatorisse!")

#Küsime kasutajalt esimest numbrit ja teisendame selle ujukomaarvuks
a = float(input("Sisesta esimene number: "))
#Küsime kasutajalt teist numbrit ja teisendame selle ujukomaarvuks
b = float(input("Sisesta teine number: "))

# Loome kalkulaatori objekti, andes talle kaks numbrit
kalk = cal(a, b)

#Alustame lõpmatut tsüklit, mis kestab kuni kasutaja valib väljumise
while True: menu()
    try:
        # Küsime kasutajalt valikut ja teisendame selle täisarvuks
        valik = int(input('\nSinu valik: '))
        # Kontrollime, kas kasutaja valis liitmise
        if valik == 1:
            #Kutsume keskmise meetodi ja prindime tulemuse
            print(f"Vastus: {kalk.liitmine()}")
            # Kontrollime, kas kasutaja valis väljumise
        elif valik == 2:
            print(f"Vastus: {kalk.lahutamine()}")
        elif valik == 3:
            print(f"Vastus: {kalk.korrutamine()}")
        elif valik == 4:
            print(f"Vastus: {kalk.jagamine()}")
        elif valik == 5:
            print(f"Vastus: {kalk.astendamine()}")
        elif valik == 6:
            print(f"Vastus: {kalk.ruutjuur()}")
        elif valik == 7:
            print(f"Vastus: {kalk.jaak()}")
        elif valik == 8:
            print(f"Vastus: {kalk.absoluut()}")
        elif valik == 9:
            print(f"Vastus: {kalk.keskmine()}")
        elif valik == 0:
            print("Head aega!")
            # Lõpetame tsükli ja programmi
            break
        # Kui kasutaja sisestas numbri väljaspool vahemikku 0-9
        else:
            # Prindime veateate
            print("Vale valik! Vali 0-9.")

    #Püüame kinni ValueError vea
    except ValueError:
        #Prindime veateate kui sisend ei olnud number
        print("Viga! Sisesta number.")