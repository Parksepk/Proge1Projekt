


def kaal(kaal):
    if kaal < 210 and kaal > 50:
        if kaal >= 130:
            kaal_pkt = (210 - kaal) / 2
        elif kaal < 130:
            kaal_pkt = (50 - kaal) / 2 * -1
        return kaal_pkt
    else: 
        print("Kaal ebareaalne!")

def vanus(vanus):
    if vanus <= 28:
        vanus_pkt = 80
    elif vanus < 0 or vanus > 120:
        print("Vanus ebareaalne!")
    else: 
        vanus_pkt = 80 - ((vanus - 28) * 0.025)
        if vanus_pkt < 0:
            vanus_pkt = 0
    return vanus_pkt

def pikkus(pikkus):
    if pikkus >= 198:
        pikkus_pkt = 100
    elif pikkus < 198:
        pikkus_pkt = 100 - (198 - pikkus) * (100/58)
    elif pikkus < 40:
        print("Pikkus ebareaalne!")
    return pikkus_pkt

def siruulatus(siruulatus):
    if siruulatus >= 213:
        siruulatus_pkt = 110
    elif siruulatus <213:
        siruulatus_pkt = 110 - (213-siruulatus) * (110/53)
    return siruulatus_pkt

#def rinnalevõtt(rinnalevõtt):

#def rebimine(rebimine):

#def kükk(kükk):

#def rinnalt_surumine(rinnalt_surumine):

#def jõutõmme(jõutõmme):

#def ketta_pb(ketta_pb):

#def paigalt_pb(paigalt_pb):

#def p_kaugus(p_kaugus):


def main(): 
    potentsiaaliindeks= (kaal(kaal_in) + vanus(vanus_in) + pikkus(pikkus_in) + siruulatus(siruulatus_in)) / 330 * 100
    potentsiaal = round(((potentsiaaliindeks/100) * 75.00), 2)
    print(f"Sinu potentsiaalne kettaheite PB on {potentsiaal} meetrit. ")

kaal_in = int(input("Sisesta kaal: "))
vanus_in = int(input("Sisesta vanus:"))
pikkus_in = int(input("Sisesta pikkus (cm):"))
siruulatus_in = int(input("Sisesta siruulatus (cm): "))


if __name__ == "__main__":
    main()