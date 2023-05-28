class Trojkat:
    def __init__(self, a, b , c, h_a):
        self.a=a
        self.b=b
        self.c=c
        self.h_a=h_a
        #self.obwod=a+b+c
    
    def obwod(self):
        return self.a+self.b+self.c

trojkat_rownoboczny=Trojkat(10, 10, 10, 8)
#print(trojkat_rownoboczny)
#print(trojkat_rownoboczny.obwod())

class Romb:
    def __init__(self, e, f, a, h):
        self.e=e
        self.f=f
        self.a=a
        self.h=h

    def obwod(self):
        return self.a*4
    def pole(self):
        return self.e*self.f*0.5

romb_zwykly=Romb(10,5,6,7)
#print(romb_zwykly.obwod())
#print(romb_zwykly.pole())

class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie=imie
        self.nazwisko=nazwisko
        self.nr_indeksu=nr_indeksu
        self.oceny= []

    def __str__(self):
           # return self.imie+" "+self.nazwisko
            return f"{self.imie} {self.nazwisko} {self.nr_indeksu}"
    
    def __int__(self):
           return 0

    def dodaj_ocene(self, ocena):
           self.oceny.append(ocena)
    
    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)

student_ola=Student("Aleksandra","Wojewoda",123123)
student_ola.dodaj_ocene(4.5)
student_ola.dodaj_ocene(5)

#print(student_ola.oceny)

#Mieszkanie
class Mieszkanie:
    def __init__(self, wymiar_salonu_1, wymiar_salonu_2, wysokosc_salonu, pietro, wyposazenie, liczba_osob_mieszkajacych, powierzchnia, adres):
        self.wymiar_salonu_1 = wymiar_salonu_1
        self.wymiar_salonu_2 = wymiar_salonu_2 
        self.wysokosc_salonu = wysokosc_salonu
        self.pietro = pietro
        self.wyposazenie = wyposazenie
        self.liczba_osob_mieszkajacych = liczba_osob_mieszkajacych
        self.powierzchnia = powierzchnia
        self.adres = adres

    def __str__(self):
        return f"{self.adres}, {self.powierzchnia}, {self.liczba_osob_mieszkajacych}"

    def kwota_ubezpieczenie(self):
        return self.pietro * self.liczba_osob_mieszkajacych * (0.5 * self.wyposazenie) * (self.powierzchnia * 0.032)

    def powierzchnia_do_malowania(self):
        return (self.wymiar_salonu_1 * self.wysokosc_salonu) * 2 + (self.wymiar_salonu_2 * self.wysokosc_salonu) * 2


mieszkanie = Mieszkanie(5, 4, 3, 2, 50000, 3, 80, "ul. Testowa 123")

print(mieszkanie.powierzchnia_do_malowania())
print(mieszkanie.kwota_ubezpieczenie())
