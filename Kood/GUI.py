import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Kettaheite projekt")

label = tk.Label(root, text="Kettaheite potentsiaali kalkulaator", font = ("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 18))
textbox.pack(padx=10)

button = tk.Button(root, text = "Alusta!", font=("Arial", 18))
button.pack()

root.mainloop()