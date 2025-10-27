import states
def slaapkamer():
    print("Je bent op de slaapkamer.")
    antwoord = input("Ga je naar ZOLDER of naar de BENEDEN?")
    if antwoord == "ZOLDER":
        states.loc = "zolder"
    elif antwoord == "BENEDEN":
        states.loc = "huis"