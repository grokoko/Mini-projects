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
            print("Do widzenia.")

        elif choice == "2":
            print("Do widzenia.")

        elif choice == "3":
            print("Do widzenia.")

        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij Enter.")