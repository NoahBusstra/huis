import states
def huis():
    print("Je staat voor een huis.")
    antwoord = input("Ga je naar KEUKEN of naar de TUIN?")
    if antwoord == "KEUKEN":
        states.loc = "keuken"
    elif antwoord == "TUIN":
        states.loc = "tuin"