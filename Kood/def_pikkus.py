

def pikkus_punktid(pikkus):
    if pikkus <= 140:
        return 0
    elif pikkus >= 198:
        return 100
    else:
        return round(((pikkus-140)/(198-140)) * 100)
    
pikkus = 190
print(pikkus_punktid(pikkus))