import tkinter as tk


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
label_algaja.grid(pady=10, padx=10, sticky="nw")
label_sisesta_andemed_a = tk.Label(algaja_frame, text="Sisesta oma andmed:", font=("Arial", 16))
label_sisesta_andemed_a.grid(pady=10, padx=10, row=1, column=0, sticky="w")
back_button_algaja = tk.Button(algaja_frame, text="Tagasi", font=("Arial", 18), command=lambda: näita_frame(main_frame))
back_button_algaja.grid(pady=60, padx=10, sticky="sw")

# edasijõudnud sisu
label_edasijõudnud = tk.Label(edasijõudnud_frame, text="EDASIJÕUDNUD", font=("Arial", 18, "bold"))
label_edasijõudnud.grid(pady=10, padx=10, sticky="nw")
label_sisesta_andemed_e = tk.Label(edasijõudnud_frame, text="Sisesta oma andmed:", font=("Arial", 16))
label_sisesta_andemed_e.grid(pady=10, padx=10, row=1, column=0, sticky="w")

label_question_e = tk.Label(edasijõudnud_frame, text="Mis on sinu pikkus?", font=("Arial", 14))
label_question_e.grid(pady=5, padx=10, row=2, column=0, sticky="w")
entry_answer_e = tk.Entry(edasijõudnud_frame, font=("Arial", 14), width=25)
entry_answer_e.grid(pady=5, padx=10, row=3, column=0, sticky="w")

back_button_edasijõudnud = tk.Button(edasijõudnud_frame, text="Tagasi", font=("Arial", 18), command=lambda: näita_frame(main_frame))
back_button_edasijõudnud.grid(pady=60, padx=10, sticky="sw")


näita_frame(main_frame)

root.mainloop()
