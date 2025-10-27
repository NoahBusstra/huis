import states
import huis
import keuken
import zolder
import slaapkamer
import tuin
while True:
    if (states.loc == "huis"):
        huis.huis()
    elif (states.loc == "keuken"):
        keuken.keuken()
    elif (states.loc == "zolder"):
        zolder.zolder()
    elif (states.loc == "slaapkamer"):
        slaapkamer.slaapkamer()
    elif (states.loc == "tuin"):
        tuin.tuin()
    