import states
def tuin():
    print("Je bent in de tuin.")
    antwoord = input("Klim je via het dak naar de SLAAPKAMER of ga je terug naar BINNEN?")
    if antwoord == "SLAAPKAMER":
        states.loc = "slaapkamer"
    elif antwoord == "BINNEN":
        states.loc = "huis"