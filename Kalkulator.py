
# Moduł 4
# Zadanie 2

import logging
logging.basicConfig(level=logging.INFO)
czy_kontynuowac = "t"
wynik = 0

while czy_kontynuowac == "t":

    dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie :")
    składnik_pierwszy = int(input("Podaj składnik 1:"))
    składnik_drugi = int(input("Podaj składnik 2:"))

    if dzialanie == "1":
        wynik = składnik_pierwszy + składnik_drugi
        logging.info(f"dodaję {składnik_pierwszy} i {składnik_drugi}")
        print(f"wynik to: {wynik}")
    elif dzialanie == "2":
        wynik = składnik_pierwszy - składnik_drugi
        logging.info(f"odejmuję {składnik_drugi} od {składnik_pierwszy}")
        print(f"wynik to: {wynik}")
    elif dzialanie == "3":
        wynik = składnik_pierwszy * składnik_drugi
        logging.info(f"mnożę {składnik_pierwszy} i {składnik_drugi}")
        print(f"wynik to: {wynik}")
    elif dzialanie == "4":
        wynik = składnik_pierwszy / składnik_drugi
        logging.info(f"dzielę {składnik_pierwszy} przez {składnik_drugi}")
        print(f"wynik to: {wynik}")
    else:
        print("Wybierz jedno z czterech działań")
        logging.info(f"podałeś : {dzialanie}")

    czy_kontynuowac = input("Jeśli chcesz kontynuować wpisz (t):")
