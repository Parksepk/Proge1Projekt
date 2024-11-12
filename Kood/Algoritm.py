


def kaal(kaal):
    if kaal < 210 and kaal > 50:
        if kaal >= 130:
            kaal_pkt = (210 - kaal) / 2
        elif kaal < 130:
            kaal_pkt = (50 - kaal) / 2 * -1
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

def pikkus(pikkus):
    if pikkus >= 198:
        pikkus_pkt = 100
    elif pikkus < 198:
        pikkus_pkt = 100 - (198 - pikkus) * (100/58)
    elif pikkus < 40:
        print("Pikkus ebareaalne!")

def siruulatus(siruulatus):
    if siruulatus >= 213:
        siruulatus_pkt = 110
    elif siruulatus <213:
        siruulatus_pkt = 110 - (213-siruulatus) * (110/53)

def rinnalevõtt(rinnalevõtt):

def rebimine(rebimine):

def kükk(kükk):

def rinnalt_surumine(rinnalt_surumine):

def jõutõmme(jõutõmme):

def ketta_pb(ketta_pb):

def paigalt_pb(paigalt_pb):

def p_kaugus(p_kaugus):


def main(): 
    
