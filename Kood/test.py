def pikkus(pikkus):
    if pikkus >= 198:
        pikkus_pkt = 100
    elif pikkus < 198:
        pikkus_pkt = 100 - (198 - pikkus) * (100/58)
    elif pikkus < 40:
        print("Pikkus ebareaalne!")
    return pikkus_pkt

pikkus = 190
print(pikkus(pikkus))