import states 
def keuken():
    print("Je staat in de keuken.")
    antwoord = input("Ga je naar TRAP of naar de TUIN?")
    if antwoord == "TRAP":
        states.loc = "zolder" 
    elif antwoord == "TUIN":
        states.loc = "tuin"
