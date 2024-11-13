import tkinter as tk
from tkinter import ttk

# Funktsioon, mis vahetab lehti
def show_frame(frame):
    frame.tkraise()  

# tkinter window
root = tk.Tk()
root.geometry("500x500")
root.title("Kettaheite potentsiaali kalkulaator")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# lehed
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')

algaja_frame = ttk.Frame(root)
algaja_frame.grid(row=0, column=0, sticky='nsew')

edasijõudnud_frame = ttk.Frame(root)
edasijõudnud_frame.grid(row=0, column=0, sticky='nsew')

# esimese lehe sisu
pealkiri = ttk.Label(main_frame, text="Kettaheite potentsiaali kalkulaator", font=("Arial", 18, "bold"))
pealkiri.grid(padx=10, pady=20, row=0, column=0, columnspan=2)

button_algaja = tk.Button(main_frame, text="Algaja", font=("Arial", 18), command=lambda: show_frame(algaja_frame))
button_algaja.grid(row=1, column=0, padx=20, pady=50)

button_edasijõudnud = tk.Button(main_frame, text="Edasijõudnud", font=("Arial", 18), command=lambda: show_frame(edasijõudnud_frame))
button_edasijõudnud.grid(row=1, column=1, padx=20, pady=50)

# agaja sisu
label_algaja = ttk.Label(algaja_frame, text="Tere tulemast Algaja lehele!", font=("Arial", 18))
label_algaja.grid(pady=20, row=0, column=0)
back_button_algaja = tk.Button(algaja_frame, text="Tagasi", font=("Arial", 18), command=lambda: show_frame(main_frame))
back_button_algaja.grid(pady=20, row=1, column=0)

# edasijõudnud sisu
label_edasijõudnud = ttk.Label(edasijõudnud_frame, text="Tere tulemast Edasijõudnud lehele!", font=("Arial", 18))
label_edasijõudnud.grid(pady=20, row=0, column=0)
back_button_edasijõudnud = tk.Button(edasijõudnud_frame, text="Tagasi", font=("Arial", 18), command=lambda: show_frame(main_frame))
back_button_edasijõudnud.grid(pady=20, row=1, column=0)

show_frame(main_frame)

root.mainloop()
