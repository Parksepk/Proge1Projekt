################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
#
# Teema: Kettaheite potentsiaali kalkulaator (Meestele)
# Arvutab potentsiaalse kettaheite tulemuse vastavalt kasutaja 
# füüsilistele näitajatele (Teoreetiliste ideaalsete tehniliste aspektide valdamisel)
#
# Autorid: Hannes Remmelgas, Kaspar Parksepp
#
# mõningane eeskuju: Puudub
#
# Lisakommentaar (nt käivitusjuhend):
# Vaja tõmmata endale tkinter extension (Terminalis: "pip install tk")
#
##################################################

import tkinter as tk #Impordime GUI liidese

#Edaspidi defineerime kõik vajaminevad funktsioonid
#Iga füüsilise ja/või jõulise näitaja kohta eraldi funktsioon,
#  mis arvutab vastava punktiskoori

def kaal(kaal_input):
    if kaal_input < 210 and kaal_input > 50:
        if kaal_input >= 130:
            kaal_pkt = (210 - kaal_input) / 2    
        elif kaal_input < 130:
            kaal_pkt = (50 - kaal_input) / 2 * -1
    else: 
        print("Kaal ebareaalne!")
        kaal_pkt = 0
    
    return kaal_pkt

def vanus(vanus_input):
    if vanus_input <= 28:
        vanus_pkt = 0
    elif vanus_input < 0 or vanus_input > 120:
        vanus_pkt = 100
        print("Vanus ebareaalne!")
    else: 
        vanus_pkt = vanus_input - 28
        
    return vanus_pkt

def pikkus(pikkus_input):
    if pikkus_input >= 198:
        pikkus_pkt = 100
    elif pikkus_input < 198:
        pikkus_pkt = 100 - (198 - pikkus_input) * (100/58)
    elif pikkus_input < 40:
        print("Pikkus ebareaalne!")
        
    return pikkus_pkt

def siruulatus(siruulatus_input):
    if siruulatus_input >= 213:
        siruulatus_pkt = 110
    elif siruulatus_input <213:
        siruulatus_pkt = 110 - (213-siruulatus_input) * (110/53)
        
    return siruulatus_pkt

def rinnalevõtt(rinnalevõtt_input):
    if rinnalevõtt_input < 20:
        rinnalevõtt_pkt = 0
    elif rinnalevõtt_input >= 200:
        rinnalevõtt_pkt = 90
    elif rinnalevõtt_input < 0:
        rinnalevõtt_pkt = 0
        print("Number on ebareaalne")
    else:
        rinnalevõtt_pkt = (rinnalevõtt_input - 20) / 2
        
    return rinnalevõtt_pkt

def rebimine(rebimine_input):
    if rebimine_input < 20:
        rebimine_pkt = 0
    elif rebimine_input >= 160:
        rebimine_pkt = 90
    elif rebimine_input < 0:
        rebimine_input = 0
        print("Number on ebareaalne")
    else:
        rebimine_pkt = (rebimine_input - 20) / 1.55
        
    return rebimine_pkt

def kükk(kükk_input):
    if kükk_input < 20:
        kükk_pkt = 0
    elif kükk_input >= 300:
        kükk_pkt = 80
    elif kükk_input < 0:
        kükk_pkt = 0
        print("Number on ebareaalne")
    else:
        kükk_pkt = (kükk_input - 20) / 3.5
    
    return kükk_pkt

def rinnalt_surumine(rinnalt_surumine_input):
    if rinnalt_surumine_input < 20:
        rinnalt_surumine_pkt = 0
    elif rinnalt_surumine_input >= 220:
        rinnalt_surumine_pkt = 60
    elif rinnalt_surumine_input < 0:
        rinnalt_surumine_pkt = 0
        print("Number on ebareaalne")
    else:
        rinnalt_surumine_pkt = (rinnalt_surumine_input - 20) / 3.33

    return rinnalt_surumine_pkt

def jõutõmme(jõutõmme_input):
    if jõutõmme_input < 60:
        jõutõmme_pkt = 0
    elif jõutõmme_input >= 320:
        jõutõmme_pkt = 60
    elif jõutõmme_input < 0:
        jõutõmme_pkt = 0
        print("Number on ebareaalne")
    else:
        jõutõmme_pkt = (jõutõmme_input - 60) / 4.33

    return jõutõmme_pkt

def p_kaugus(p_kaugus_input):
    if p_kaugus_input < 190:
        p_kaugus_pkt = 0
    elif p_kaugus_input >= 340:
        p_kaugus_pkt = 90
    elif p_kaugus_input < 0:
        p_kaugus_pkt = 0
        print("Number on ebareaalne")
    else:
        p_kaugus_pkt = (p_kaugus_input - 190) / 1.67
    
    return p_kaugus_pkt 

#Tulemuste funktsioon ehk n.ö. main funktsioon
#Selgitab välja, kas kasutaja valis "algaja" või "edasijõudnud" variandi ning seejärel 
# proovib kõikide funktsioonide tulemuste abil leida optimaalne tulemus, juhul kui mõni sisend on
# puudu või ei sobi, palub programm sisestada kõik väärtused korrektselt.

def tulemused(haru):
    if haru == "algaja":
        try:
            kaal_input = float(sisend_kaal.get())
            vanus_input = int(sisend_vanus.get())
            pikkus_input = float(sisend_pikkus.get())
            siruulatus_input = float(sisend_siruulatus.get())

            potentsiaaliindeks = kaal(kaal_input) + pikkus(pikkus_input) + siruulatus(siruulatus_input) / 250 * 100
            potentsiaal_ilma_vanuseta = float((potentsiaaliindeks/100) * 45)
            potentsiaal = round(potentsiaal_ilma_vanuseta - (potentsiaal_ilma_vanuseta * vanus(vanus_input) * 0.01), 2)
            tulemus_box_algaja.config(text=f"Sinu potentsiaalne kettaheite PB on {potentsiaal} meetrit.")

        except ValueError:
            tulemus_box_algaja.config(text="Palun sisesta kõik väärtused korrektselt!")


    if haru == "edasijõudnud":
        try:
            kaal_input = float(sisend_kaal_edasijõudnud.get())
            vanus_input = int(sisend_vanus_edasijõudnud.get())
            pikkus_input = float(sisend_pikkus_edasijõudnud.get())
            siruulatus_input = float(sisend_siruulatus_edasijõudnud.get())
            rinnalevõtt_input = int(sisend_rinnalevõtt_edasijõudnud.get())
            rebimine_input = int(sisend_rebimine_edasijõudnud.get())
            kükk_input = int(sisend_kükk_edasijõudnud.get())
            rinnalt_surumine_input = int(sisend_rinnalt_surumine_edasijõudnud.get())
            jõutõmme_input = int(sisend_jõutõmme_edasijõudnud.get())
            p_kaugus_input = int(sisend_p_kaugus_edasijõudnud.get())

            potentsiaaliindeks = (kaal(kaal_input) + pikkus(pikkus_input) + siruulatus(siruulatus_input) + rinnalevõtt(rinnalevõtt_input) + rebimine(rebimine_input) + kükk(kükk_input) + rinnalt_surumine(rinnalt_surumine_input) + jõutõmme(jõutõmme_input) + p_kaugus(p_kaugus_input)) / 720 * 100
            potentsiaal_ilma_vanuseta = float(potentsiaaliindeks)
            potentsiaal = round(potentsiaal_ilma_vanuseta - (potentsiaal_ilma_vanuseta * vanus(vanus_input) * 0.01), 2)
            if potentsiaal > 80:
                potentsiaal *= 0.8
                potentsiaal = round(potentsiaal, 2)
            tulemus_box_edasijõudnud.config(text=f"Sinu potentsiaalne kettaheite PB on {potentsiaal} meetrit.")

        except ValueError:
            tulemus_box_edasijõudnud.config(text="Palun sisesta kõik väärtused korrektselt!")

#SIIT EDASI PUHTALT GUI 

#Funktsioon, mis vahetab frame/lehti
def näita_frame(frame):
    frame.tkraise()

#Loob tkinter akna
root = tk.Tk()
root.geometry("550x600")
root.title("Kettaheite potentsiaali kalkulaator")
root.resizable(False, False)

#Loob framed/lehed
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')

algaja_frame = tk.Frame(root)
algaja_frame.grid(row=0, column=0, sticky='nsew')

edasijõudnud_frame = tk.Frame(root)
edasijõudnud_frame.grid(row=0, column=0, sticky='nsew')

#Pealehe lehe sisu
#Loob pealehe pealkirja
pealkiri = tk.Label(main_frame, text="Kettaheite potentsiaali kalkulaator", font=("Arial", 18, "bold"))
pealkiri.grid(padx=10, pady=60, row=0, column=0, columnspan=2)
#Loob algaja nupu
button_algaja = tk.Button(main_frame, text="Algaja", width = 15, height = 2, bg = "red", font=("Arial", 18), command=lambda: näita_frame(algaja_frame)) #nupp kutsub välja funktsiooni näita_frame()
button_algaja.grid(row=1, column=0, padx=20, pady=50)
#Loob edasijõudnud nupu
button_edasijõudnud = tk.Button(main_frame, text="Edasijõudnud",width = 15, height = 2, bg = "blue", font=("Arial", 18), command=lambda: näita_frame(edasijõudnud_frame)) #nupp kutsub välja funktsiooni näita_frame()
button_edasijõudnud.grid(row=1, column=1, padx=20, pady=50)

#Algaja lehe sisu
#Loob algaja teksti
label_algaja = tk.Label(algaja_frame, text="ALGAJA", font=("Arial", 18, "bold"))
label_algaja.grid(row=0, column= 0, pady=10, padx=10, sticky="nw")

#Loob sisesta andmed teksti
label_sisesta_andemed_a = tk.Label(algaja_frame, text="Sisesta oma andmed:", font=("Arial", 16))
label_sisesta_andemed_a.grid(row=1, column=0, pady=10, padx=10, sticky="w")

#Loob teksti kaal
label_kaal = tk.Label(algaja_frame, text="Kaal (kg):", font=("Arial", 14))
label_kaal.grid(row=2, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi kaal
sisend_kaal = tk.Entry(algaja_frame, font=("Arial", 14))
sisend_kaal.grid(row=2, column=1, padx=10, pady=3)

#Loob teksti vanus
label_vanus = tk.Label(algaja_frame, text="Vanus (aastates):", font=("Arial", 14))
label_vanus.grid(row=3, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi vanus
sisend_vanus = tk.Entry(algaja_frame, font=("Arial", 14))
sisend_vanus.grid(row=3, column=1, padx=10, pady=3)

#Loob teksti pikkus
label_pikkus = tk.Label(algaja_frame, text="Pikkus (cm):", font=("Arial", 14))
label_pikkus.grid(row=4, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi pikkus
sisend_pikkus = tk.Entry(algaja_frame, font=("Arial", 14))
sisend_pikkus.grid(row=4, column=1, padx=10, pady=3)

#Loob teksti siruulatus
label_siruulatus = tk.Label(algaja_frame, text="Siruulatus (cm):", font=("Arial", 14))
label_siruulatus.grid(row=5, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi siuruulatus
sisend_siruulatus = tk.Entry(algaja_frame, font=("Arial", 14))
sisend_siruulatus.grid(row=5, column=1, padx=10, pady=3)

#Loob esita nupu, mida vajutades kutsub välja tulemused funktsiooni
esita_button_algaja = tk.Button(algaja_frame, text="Esita", font=("Arial", 18), command=lambda: tulemused("algaja"))
esita_button_algaja.grid(row=6, column=0, columnspan=2, pady=10)
#Loob tulemuste kuvamiseks kasti
tulemus_box_algaja = tk.Label(algaja_frame, text="Tulemus kuvatakse siin.", font=("Arial", 16), bg="lightgrey", width=40, height=5, relief="sunken", anchor="nw", justify="left")
tulemus_box_algaja.grid(row=7, column=0, columnspan=2, padx=10, pady=20)
#Loob lehe jaoks tagasi nupu, mida vajutades kutsub välja näita_frame funktsiooni
back_button_algaja = tk.Button(algaja_frame, text="Tagasi", font=("Arial", 18), command=lambda: näita_frame(main_frame))
back_button_algaja.grid(pady=60, padx=10, sticky="sw")

#Edasijõudnud lehe sisu
#Loob edasijõudnud teksti
label_edasijõudnud = tk.Label(edasijõudnud_frame, text="EDASIJÕUDNUD", font=("Arial", 18, "bold"))
label_edasijõudnud.grid(row=0, column= 0, pady=10, padx=10, sticky="nw")
#Loob sisesta andmed teksti
label_sisesta_andemed_e = tk.Label(edasijõudnud_frame, text="Sisesta oma andmed:", font=("Arial", 16))
label_sisesta_andemed_e.grid(row=1, column=0, pady=10, padx=10, sticky="w")

#Loob teksti kaal
label_kaal_edasijõudnud = tk.Label(edasijõudnud_frame, text="Kaal (kg):", font=("Arial", 14))
label_kaal_edasijõudnud.grid(row=2, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi kaal
sisend_kaal_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_kaal_edasijõudnud.grid(row=2, column=1, padx=10, pady=3)

#Loob teksi vanus
label_vanus_edasijõudnud = tk.Label(edasijõudnud_frame, text="Vanus (aastates):", font=("Arial", 14))
label_vanus_edasijõudnud.grid(row=3, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi vanus
sisend_vanus_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_vanus_edasijõudnud.grid(row=3, column=1, padx=10, pady=3)

#Loob pikkus teksti
label_pikkus_edasijõudnud = tk.Label(edasijõudnud_frame, text="Pikkus (cm):", font=("Arial", 14))
label_pikkus_edasijõudnud.grid(row=4, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi pikkus
sisend_pikkus_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_pikkus_edasijõudnud.grid(row=4, column=1, padx=10, pady=3)

#Loob siruulatus teksti
label_siruulatus_edasijõudnud = tk.Label(edasijõudnud_frame, text="Siruulatus (cm):", font=("Arial", 14))
label_siruulatus_edasijõudnud.grid(row=5, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi surulatus
sisend_siruulatus_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_siruulatus_edasijõudnud.grid(row=5, column=1, padx=10, pady=3)

#Loob teksti rinnalevõtt
label_rinnalevõtt_edasijõudnud = tk.Label(edasijõudnud_frame, text="Rinnalevõtt (kg):", font=("Arial", 14))
label_rinnalevõtt_edasijõudnud.grid(row=6, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi rinnalevõtt
sisend_rinnalevõtt_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_rinnalevõtt_edasijõudnud.grid(row=6, column=1, padx=10, pady=3)

#Loob teksti rebimine
label_rebimine_edasijõudnud = tk.Label(edasijõudnud_frame, text="Rebimine (kg):", font=("Arial", 14))
label_rebimine_edasijõudnud.grid(row=7, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi rebimine
sisend_rebimine_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_rebimine_edasijõudnud.grid(row=7, column=1, padx=10, pady=3)

#Loob teksti kükk
label_kükk_edasijõudnud = tk.Label(edasijõudnud_frame, text="Kükk (kg):", font=("Arial", 14))
label_kükk_edasijõudnud.grid(row=8, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi kükk
sisend_kükk_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_kükk_edasijõudnud.grid(row=8, column=1, padx=10, pady=3)

#Loob teksti rinnalt surumine
label_rinnalt_surumine_edasijõudnud = tk.Label(edasijõudnud_frame, text="Rinnalt surumine (kg):", font=("Arial", 14))
label_rinnalt_surumine_edasijõudnud.grid(row=9, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi rinnalt surumine
sisend_rinnalt_surumine_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_rinnalt_surumine_edasijõudnud.grid(row=9, column=1, padx=10, pady=3)

#Loob teksti jõutõmme
label_jõutõmme_edasijõudnud = tk.Label(edasijõudnud_frame, text="Jõutõmme (kg):", font=("Arial", 14))
label_jõutõmme_edasijõudnud.grid(row=10, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi jõutõmme
sisend_jõutõmme_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_jõutõmme_edasijõudnud.grid(row=10, column=1, padx=10, pady=3)

#Loob teksti paigalt kaugus
label_p_kaugus_edasijõudnud = tk.Label(edasijõudnud_frame, text="Paigalt kaugus (cm):", font=("Arial", 14))
label_p_kaugus_edasijõudnud.grid(row=11, column=0, padx=10, pady=3, sticky="w")
#Loob sisendi paigalt kaugus
sisend_p_kaugus_edasijõudnud = tk.Entry(edasijõudnud_frame, font=("Arial", 14))
sisend_p_kaugus_edasijõudnud.grid(row=11, column=1, padx=10, pady=3)

#Loob esita nupu, mida vajutades kutsutaksevälja tulemused funktsiooni
esita_button_edasijõudnud = tk.Button(edasijõudnud_frame, text="Esita", font=("Arial", 16), command=lambda: tulemused("edasijõudnud"))
esita_button_edasijõudnud.grid(row=12, column=0, columnspan=2, pady=5)
#Loob tulemuste akna, kus kuvatakse tulemus
tulemus_box_edasijõudnud = tk.Label(edasijõudnud_frame, text="Tulemus kuvatakse siin.", font=("Arial", 16), bg="lightgrey", width=40, height=1, relief="sunken", anchor="nw", justify="left")
tulemus_box_edasijõudnud.grid(row=13, column=0, columnspan=2, padx=10, pady=5)

#Loob tagasi nupu, mida vajutades kutsutakse välja funktsioon näita_frame
back_button_edasijõudnud = tk.Button(edasijõudnud_frame, text="Tagasi", font=("Arial", 16), command=lambda: näita_frame(main_frame))
back_button_edasijõudnud.grid(padx=5,pady=10,	 sticky="sw")

#Teeb kindlaks, et programmi avades avaneks esimesena main_frame
näita_frame(main_frame)
#Tkinteri loop, mis hoiab programmi töös ja aktiivsena
root.mainloop()
