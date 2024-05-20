# Definujeme funkci s jedním parametrem
def pozdrav(jmeno):
    # Funkce vrací pozdrav s daným jménem
    return f"Ahoj, {jmeno}!"

# Hlavní část programu
def hlavni():
    # Vstup a přetypování
    cislo_str = input("Zadejte číslo: ")  # Získání vstupu od uživatele jako řetězec
    cislo = int(cislo_str)  # Přetypování vstupu na celé číslo

    # Práce s podmínkou a logickými funkcemi - and, or, not
    if cislo > 0 and cislo % 2 == 0:
        # Pokud je číslo kladné a sudé
        print(f"Číslo {cislo} je kladné a sudé.")
    elif cislo > 0 and cislo % 2 != 0:
        # Pokud je číslo kladné a liché
        print(f"Číslo {cislo} je kladné a liché.")
    elif cislo < 0:
        # Pokud je číslo záporné
        print(f"Číslo {cislo} je záporné.")
    else:
        # Pokud je číslo nula
        print(f"Číslo je nula.")

    # Operace s polem - přidání do pole pomocí čísla a názvu, odebrání z pole
    muj_list = []  # Inicializace prázdného seznamu
    muj_list.append(5)  # Přidání čísla do seznamu
    muj_list.append("jablko")  # Přidání řetězce do seznamu
    print("Přidané prvky do pole:", muj_list)  # Výpis seznamu po přidání prvků

    # Odebrání prvků ze seznamu
    if 5 in muj_list:
        muj_list.remove(5)  # Odebrání čísla ze seznamu
    if "jablko" in muj_list:
        muj_list.remove("jablko")  # Odebrání řetězce ze seznamu

    print("Pole po odebrání prvků:", muj_list)  # Výpis seznamu po odebrání prvků

    # Cyklus s pevným počtem opakování
    for i in range(5):
        # Tento cyklus se provede 5x
        print(f"For cyklus iterace {i}")

    # Cyklus s podmínkou
    j = 0
    while j < 5:
        # Tento cyklus se provede, dokud je j menší než 5
        print(f"While cyklus iterace {j}")
        j += 1  # Inkrementace proměnné j

    # Výstup
    jmeno = input("Zadejte své jméno: ")  # Získání jména od uživatele
    print(pozdrav(jmeno))  # Výstup funkce s parametrem

# Spuštění hlavní části programu
if __name__ == "__main__":
    hlavni()