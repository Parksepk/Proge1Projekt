import tkinter as tk

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
        vanus = 28
    elif vanus < 0 or vanus > 120:
        print("Vanus ebareaalne!")
    else: 
        #vanus_pkt = 80 - ((vanus - 28) * 0.025)
        if vanus_pkt < 0:
            vanus = 0
    return vanus

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

def main():
    try:
        kaal_in = float(sisend_kaal.get())
        vanus_in = int(sisend_vanus.get())
        pikkus_in = float(sisend_pikkus.get())
        siruulatus_in = float(sisend_siruulatus.get())
        potentsiaaliindeks = (kaal(kaal_in) + pikkus(pikkus_in) + siruulatus(siruulatus_in)) / 250 * 100
        potentsiaal_ilma_vanuseta = round(((potentsiaaliindeks / 100) * 75.00), 2)
        potentsiaal = potentsiaal_ilma_vanuseta * (1-((vanus-28)* 0.025))
        tulemus_box.config(text=f"Sinu potentsiaalne kettaheite PB on {potentsiaal} meetrit.")

    except ValueError:
        tulemus_box.config(text="Palun sisesta kõik väärtused korrektselt!")

    except Exception as e:
        tulemus_box.config(text=f"Palun sisesta kõik väärtused korrektselt!")

# Funktsioon, mis vahetab lehti
def näita_frame(frame):
    frame.tkraise()

# tkinter window
root = tk.Tk()
root.geometry("550x600")
root.title("Kettaheite potentsiaali kalkulaator")
root.resizable(False, False)

# lehed
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')

algaja_frame = tk.Frame(root)
algaja_frame.grid(row=0, column=0, sticky='nsew')

edasijõudnud_frame = tk.Frame(root)
edasijõudnud_frame.grid(row=0, column=0, sticky='nsew')

# esimese lehe sisu
pealkiri = tk.Label(main_frame, text="Kettaheite potentsiaali kalkulaator", font=("Arial", 18, "bold"))
pealkiri.grid(padx=10, pady=60, row=0, column=0, columnspan=2)

button_algaja = tk.Button(main_frame, text="Algaja", width = 15, height = 2, bg = "red", font=("Arial", 18), command=lambda: näita_frame(algaja_frame))
button_algaja.grid(row=1, column=0, padx=20, pady=50)

button_edasijõudnud = tk.Button(main_frame, text="Edasijõudnud",width = 15, height = 2, bg = "blue", font=("Arial", 18), command=lambda: näita_frame(edasijõudnud_frame))
button_edasijõudnud.grid(row=1, column=1, padx=20, pady=50)

# algaja sisu
label_algaja = tk.Label(algaja_frame, text="ALGAJA", font=("Arial", 18, "bold"))
label_algaja.grid(row=0, column= 0, pady=10, padx=10, sticky="nw")
label_sisesta_andemed_a = tk.Label(algaja_frame, text="Sisesta oma andmed:", font=("Arial", 16))
label_sisesta_andemed_a.grid(row=1, column=0, pady=10, padx=10, sticky="w")

label_kaal = tk.Label(algaja_frame, text="Kaal (kg):", font=("Arial", 16))
label_kaal.grid(row=2, column=0, padx=10, pady=5, sticky="w")
sisend_kaal = tk.Entry(algaja_frame, font=("Arial", 16))
sisend_kaal.grid(row=2, column=1, padx=10, pady=5)

label_vanus = tk.Label(algaja_frame, text="Vanus (aastates):", font=("Arial", 16))
label_vanus.grid(row=3, column=0, padx=10, pady=5, sticky="w")
sisend_vanus = tk.Entry(algaja_frame, font=("Arial", 16))
sisend_vanus.grid(row=3, column=1, padx=10, pady=5)

label_pikkus = tk.Label(algaja_frame, text="Pikkus (cm):", font=("Arial", 16))
label_pikkus.grid(row=4, column=0, padx=10, pady=5, sticky="w")
sisend_pikkus = tk.Entry(algaja_frame, font=("Arial", 16))
sisend_pikkus.grid(row=4, column=1, padx=10, pady=5)

label_siruulatus = tk.Label(algaja_frame, text="Siruulatus (cm):", font=("Arial", 16))
label_siruulatus.grid(row=5, column=0, padx=10, pady=5, sticky="w")
sisend_siruulatus = tk.Entry(algaja_frame, font=("Arial", 16))
sisend_siruulatus.grid(row=5, column=1, padx=10, pady=5)

tulemus_box = tk.Label(algaja_frame, text="Tulemus kuvatakse siin.", font=("Arial", 16), bg="lightgrey", width=40, height=5, relief="sunken", anchor="nw", justify="left")
tulemus_box.grid(row=7, column=0, columnspan=2, padx=10, pady=20)
vastus_button = tk.Button(algaja_frame, text="Esita", font=("Arial", 18), command=main)
vastus_button.grid(row=6, column=0, columnspan=2, pady=10)

back_button_algaja = tk.Button(algaja_frame, text="Tagasi", font=("Arial", 18), command=lambda: näita_frame(main_frame))
back_button_algaja.grid(pady=60, padx=10, sticky="sw")

# edasijõudnud sisu
label_edasijõudnud = tk.Label(edasijõudnud_frame, text="EDASIJÕUDNUD", font=("Arial", 18, "bold"))
label_edasijõudnud.grid(row=0, column= 0, pady=10, padx=10, sticky="nw")
label_sisesta_andemed_e = tk.Label(edasijõudnud_frame, text="Sisesta oma andmed:", font=("Arial", 16))
label_sisesta_andemed_e.grid(row=1, column=0, pady=10, padx=10, sticky="w")

back_button_edasijõudnud = tk.Button(edasijõudnud_frame, text="Tagasi", font=("Arial", 18), command=lambda: näita_frame(main_frame))
back_button_edasijõudnud.grid(pady=60, padx=10, sticky="sw")


näita_frame(main_frame)

root.mainloop()
