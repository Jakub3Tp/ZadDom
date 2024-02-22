def szyfr_cezara(text, przesun):
    zaszyfrowany_tekst = ""
    for literka in tekst:
        if literka.isalpha():  # Sprawdzamy, czy znak jest literą
            if literka.islower():  # Sprawdzamy, czy litera jest mała
                zaszyfrowana_litera = chr(((ord(literka) - 97 + przesun) % 26) + 97)
            else:  # Jeśli litera jest wielka
                zaszyfrowana_litera = chr(((ord(literka) - 65 + przesun) % 26) + 65)
        else:  # Jeśli znak nie jest literą
            zaszyfrowana_litera = literka
        zaszyfrowany_tekst += zaszyfrowana_litera
    return zaszyfrowany_tekst

def przesun_o():
    while True:
        try:
            przesun = int(input("Podaj przesunięcie (liczba całkowita od 1 do 25): "))
            if 1 <= przesun <= 25:
                return przesun
            else:
                print("Przesunięcie musi być liczbą całkowitą od 1 do 25.")
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")

def main():
    tekst = input("Podaj tekst do zaszyfrowania: ")
    przesun = przesun_o()
    zaszyfrowany_tekst = szyfr_cezara(tekst, przesun)
    print("Zaszyfrowany tekst:", zaszyfrowany_tekst)

    main()
