#zródło: https://www.biznes.gov.pl/pl/portal/0083, https://poradnikpracownika.pl/-jak-obliczyc-swoje-wynagrodzenie, https://earthly.dev/blog/csv-python/

import csv
class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.wynagrodzenie_brutto}"

    def oblicz_netto(self):
        return self.wynagrodzenie_brutto - self.wynagrodzenie_brutto * 0.0976 - self.wynagrodzenie_brutto * 0.015 - self.wynagrodzenie_brutto * 0.0245
    
    def oblicz_koszty_pracodawcy(self):
        return self.wynagrodzenie_brutto + self.wynagrodzenie_brutto * 0.0976 + self.wynagrodzenie_brutto * 0.065 + self.wynagrodzenie_brutto * 0.0167 + self.wynagrodzenie_brutto * 0.0245 + self.wynagrodzenie_brutto * 0.010

pracownicy = []

with open("pracownicy.csv", 'r') as file: #import csv
    csvreader = csv.reader(file)
    next(csvreader) #pominiecie pierwszego wiersza
    for row in csvreader:
        imie, nazwisko, wynagrodzenie_brutto = row
        pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
        pracownicy.append(pracownik)

koszty_wszystkich_pracowników = 0
    
for pracownik in pracownicy:
    netto = pracownik.oblicz_netto()
    koszty_pracodawcy = pracownik.oblicz_koszty_pracodawcy()
    koszt_calkowity = pracownik.wynagrodzenie_brutto - netto + koszty_pracodawcy

    print(f"Pracownik {pracownik.imie} {pracownik.nazwisko}:")
    print(f"- pensja brutto: {pracownik.wynagrodzenie_brutto}")
    print(f"- pensja netto: {netto}")
    print(f"- koszty pracodawcy: {koszty_pracodawcy}")
    print(f"- koszt całkowity: {koszt_calkowity}\n")

    koszty_wszystkich_pracowników += koszt_calkowity

print(f"Suma kosztów to: {koszty_wszystkich_pracowników}")
