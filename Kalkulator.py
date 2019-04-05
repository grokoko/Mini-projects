#Przelicznik

def main():
    choice = None
    while choice != "0":
        print \
            ("""
            Przelicznik dla hexów, binarów i decimali
            
            0 - zakończ
            1 - przelicz hexa
            2 - przelicz binary
            3 - przelicz decimal
            """)

        choice = input("Wybierasz: ")
        print()

        if choice == "0":
            print("Do widzenia.")

        elif choice == "1":
            h = input("Podaj liczbę: ")
            dec = int(h, 16)
            b = format(dec, '0>42b')
            print(h, "hex = ", dec, "decimal i ", b, "binary.")

        elif choice == "2":
            b2 = input("Podaj liczbę: ")
            liczba = int(b2, 2)
            hexa = hex(liczba)
            print(b2, "binary = ", liczba, "decimal i ", hexa, "hex.")

        elif choice == "3":
            d = int(input("Podaj liczbę: "))
            he = hex(d)
            bi = format(d, '0>42b')
            print(d, "decimal =", he, "hex i", bi, "binary.")

        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij Enter.")