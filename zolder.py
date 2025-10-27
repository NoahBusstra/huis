import states
def zolder():
    print("Je bent op de zolder.")
    antwoord = input("Ga je naar SLAAPKAMER of naar de TUIN?")
    if antwoord == "SLAAPKAMER":
        states.loc = "slaapkamer"
    elif antwoord == "TUIN":
        states.loc = "tuin"