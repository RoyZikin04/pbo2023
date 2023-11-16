import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from Fungsi import luasbalok, volumebalok

def hitung_luas():
    panjang = float(txtpanjang.get())
    lebar   = float(txtlebar.get())
    tinggi  = float(txttinggi.get())

    L = luasbalok (panjang, lebar, tinggi)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    panjang = float(txtpanjang.get())
    lebar   = float(txtlebar.get())
    tinggi  = float(txttinggi.get())

    V = volumebalok (panjang, lebar, tinggi)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Balok")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

#Nametag
nametag = tk.Frame(frame, bg="Green", height=50)
nametag.grid(row=6, column=1, columnspan=1, sticky='ew', pady=10)

nama = Label(nametag, text="Roy Zikin", bg='Green')
nama.grid(row=6, column=1, sticky='nsew' , padx=5, pady=5)

nametag.grid_rowconfigure(6, weight=1)
nametag.grid_columnconfigure(1, weight=1)

# Label panjang
panjang = Label(frame, text="Panjang:") 
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label lebar
lebar = Label(frame, text="Lebar:") 
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label tinggi
tinggi = Label(frame, text="Tinggi:") 
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

# Textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()