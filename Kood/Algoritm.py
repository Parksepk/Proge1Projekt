


def algaja(kaal, vanus, pikkus, siruulatus):
    if kaal < 210 and kaal > 50:
        if kaal >= 130:
            kaal_pkt = (210 - kaal) / 2
        elif kaal < 130:
            kaal_pkt = (50 - kaal) / 2 * -1
    else: 
        print("Kaal ebareaalne!")
    if vanus <= 28:
        vanus_pkt = 80
    elif vanus < 0 or vanus > 120:
        print("Vanus ebareaalne!")
    else: 
        vanus_pkt = 80 - ((vanus - 28) * 0.025)
        if vanus_pkt < 0:
            vanus_pkt = 0
    if pikkus >= 198:
        pikkus_pkt = 100
    elif pikkus < 198:
        pikkus_pkt = 
    if siruulatus >= 213:
        siruulatus_pkt = 110
    elif 