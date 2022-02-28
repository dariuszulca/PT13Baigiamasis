from tkinter import *
import datetime
import sqlite3

# TK islaidu
islaidu_lent = Tk()
islaidu_lent.title("MINI APSKAITOS PROGRAMA")

# Sukurti duombaze

conn = sqlite3.connect("Biudzetas.db")

c = conn.cursor()

# Sukuriame lentele

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS Biudzetas (

              Prekes pavadinimas TEXT, 
              Tiekejas TEXT, 
              Mokejimo budas TEXT, 
              Data TEXT,
              Islaidos INTEGER
              )""")

# Irasymo Submit komanda

def itraukti_irasus():
    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()

    # Iterpti i lentele
    with conn:
        c.execute("INSERT INTO Biudzetas VALUES (:p_pavadinimas, :tiekejas, :mok_budas, :data, :islaidos)",
              {

                  'p_pavadinimas': p_pavadinimas.get(),
                  'tiekejas': tiekejas.get(),
                  'mok_budas': mok_budas.get(),
                  'data': data.get(),
                  'islaidos': islaidos.get()
              })
    status["text"]="Išlaidos Įvestos"

    # Istrinti po nuspaudimo laukus
    p_pavadinimas.delete(0, END)
    tiekejas.delete(0, END)
    mok_budas.delete(0, END)
    data.delete(0, END)
    islaidos.delete(0, END)

# Visu irasu rodymas
def visi_irasai():
    islaidu_suvest = Tk()
    islaidu_suvest.title("IšLAIDOS")
    islaidu_suvest.geometry("800x800")

    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()
    with conn:
        c.execute("SELECT *, oid FROM Biudzetas")
    irasai = c.fetchall()

    spausdinti_irasus = ''
    for irasas in irasai:
        spausdinti_irasus += str(irasas[0]) + " " + str(irasas[1]) + " " + str(
            irasas[2]) + " " + str(irasas[3]) + " " + str(irasas[4]) + " " + "\t" + str(
            irasas[5]) + " " "\n"

    visi_irasai = Label(islaidu_suvest, text=spausdinti_irasus)
    visi_irasai.grid(row=2, column=1, columnspan=1, ipady=50, ipadx=50)
    status["text"] = "Kitame lange rasite atpausdintus Visus Išlaidų Įrašus"
    c.execute("SELECT SUM(Islaidos) FROM Biudzetas")
    suma_irasu3= c.fetchall()

    islaidu_suma = Label(islaidu_suvest, text=suma_irasu3)
    islaidu_suma.grid(row=1, column=1, columnspan=1, ipady=25, ipadx=40)

    islaidu_suma2 = Label(islaidu_suvest, text="Viso: ")
    islaidu_suma2.grid(row=1, column=0, columnspan=1, ipady=25, ipadx=40)

    # uzdaryti langa
    isjungti_langa_islaidu = Button(islaidu_suvest, text="Uždaryti langą arba <Esc>", command=islaidu_suvest.destroy)
    isjungti_langa_islaidu.grid(row=0, column=0, columnspan=6, ipadx=50, ipady=50)
    islaidu_suvest.bind("<Escape>", lambda x: islaidu_suvest.destroy())

    islaidu_suvest.mainloop()
# Sukurti duombaze

conn = sqlite3.connect("Biudzetas.db")

c = conn.cursor()

# Sukuriame lentele2
with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS Pajamos (


              pajamos_islaidos INTEGER,
              pajamos_data STRING
              )""")

# Irasymo irasu komanda

def itraukti_pajamas():
    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()

    # Iterpti i lentele
    with conn:
        c.execute("INSERT INTO Pajamos VALUES (:pajamos_islaidos, :pajamos_data)",
              {

                  'pajamos_islaidos': pajamos_islaidos.get(),
                  'pajamos_data': pajamos_data.get()

              })

    status["text"]="Pajamos Įvestos"



    # Istrinti po nuspaudimo laukus
    pajamos_islaidos.delete(0, END)
    pajamos_data.delete(0, END)


# Visu irasu rodymas
def pajamu_irasai():
    pajamu_suvest = Tk()
    pajamu_suvest.title("PAJAMOS")
    pajamu_suvest.geometry("400x400")

    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()
    with conn:
        c.execute("SELECT *, oid FROM Pajamos")
    irasai = c.fetchall()

    spausdinti_irasus2 = ''
    for irasas in irasai:
        spausdinti_irasus2 += str(irasas[0]) + " " + str(irasas[1]) + " " + "\t" + str(irasas[2])+  "\n"

    pajamu_irasai = Label(pajamu_suvest, text=spausdinti_irasus2)
    pajamu_irasai.grid(row=2, column=1, columnspan=1, ipady=25, ipadx=40)
    status["text"] = "Kitame lange rasite atspausdintus Visus Pajamų Įrašus"
    with conn:
        c.execute("SELECT SUM(pajamos_islaidos) FROM Pajamos")
    suma_irasu2=c.fetchall()

    pajamu_suma = Label(pajamu_suvest, text=suma_irasu2)
    pajamu_suma.grid(row=1, column=1, columnspan=1, ipady=25, ipadx=40)

    pajamu_suma2 = Label(pajamu_suvest, text="Viso: ")
    pajamu_suma2.grid(row=1, column=0, columnspan=1, ipady=25, ipadx=40)

    # Lango Isjungimo mygtukas

    isjungti_langa_pajamu = Button(pajamu_suvest, text="Uždaryti langą arba <Esc>", command=pajamu_suvest.destroy)
    isjungti_langa_pajamu.grid(row=0, column=0, columnspan=2, ipadx=40, ipady=50)
    pajamu_suvest.bind("<Escape>", lambda x: pajamu_suvest.destroy())

    pajamu_suvest.mainloop()

# Istrinti islaidu irasus

def istrinti_islaidu_irasus():
    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()
    with conn:
        c.execute("DELETE from Biudzetas WHERE oid=" + istrinti_islaidu_nr.get())
    status["text"] = "Įrašas Ištrintas"


    istrinti_islaidu_nr.delete(0, END)

# Istrinti pajamu irasus

def istrinti_pajamu_irasus():
    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()
    with conn:
        c.execute("DELETE from Pajamos WHERE oid=" + istrinti_pajamu_nr.get())
    status["text"] = "Pajamų Įrašas Ištrintas"


    istrinti_pajamu_nr.delete(0, END)


# Sukurti Balansa

def Balansas():
    balans_suvest = Tk()
    balans_suvest.title("Balansas")


    conn = sqlite3.connect("Biudzetas.db")

    c = conn.cursor()
    with conn:
        c.execute("SELECT (SELECT SUM(pajamos_islaidos) AS Total FROM Pajamos) - (SELECT SUM(Islaidos) AS Total FROM Biudzetas) AS Skirtumas")
    Skirtumas = c.fetchall()
    balans = Label(balans_suvest, text=Skirtumas)
    balans.grid(row=1, column=1, columnspan=1, ipady=25, ipadx=40)

    balans2 = Label(balans_suvest, text="Viso: ")
    balans2.grid(row=1, column=0, columnspan=1, ipady=25, ipadx=40)

    # Lango Isjungimo mygtukas

    isjungti_langa_pajamu = Button(balans_suvest, text="Uždaryti langą arba <Esc>", command=balans_suvest.destroy)
    isjungti_langa_pajamu.grid(row=0, column=0, columnspan=2)
    balans_suvest.bind("<Escape>", lambda x: balans_suvest.destroy())

    status["text"]="Balansas/Likutis"

    balans_suvest.mainloop()

# Mygtukai

balanso_btn = Button(islaidu_lent, text="Balansas", command=Balansas)
balanso_btn.grid(row=14, column=0, columnspan=1, ipadx=50)

    # istrinti Balanso mygtukas

istrinti_pajamu_btn = Button(islaidu_lent, text="Ištrinti Pajamų Įrašus", wraplength=65, justify=CENTER,
                                  command=istrinti_pajamu_irasus)
istrinti_pajamu_btn.grid(row=4, column=2, columnspan=1, ipadx=50, padx=25, pady=(15, 0))

    # istrinti Islaidas mygtukas

istrinti_islaidu_btn = Button(islaidu_lent, text="Ištrinti Išlaidų Įrašus", wraplength=65, justify=CENTER,
                                  command=istrinti_islaidu_irasus)
istrinti_islaidu_btn.grid(row=12, column=2, columnspan=1, ipadx=50, padx=25, pady=(15, 0))

# Statuso eilute

status = Label(islaidu_lent, text="", bd=3, relief=SUNKEN, anchor=W, font='sans 10 bold')

# Sukurti Pajamu mygtuka

pajamos_islaidos_btn = Button(islaidu_lent, text="Įtraukti pajamas", command=itraukti_pajamas)
pajamos_islaidos_btn.grid(row=3, column=0, columnspan=1, ipadx=50)

pajamu_data_btn = Button(islaidu_lent, text="Rodyti Pajamų Įrašus", command=pajamu_irasai)
pajamu_data_btn.grid(row=3, column=1, columnspan=1, ipadx=50)

# Sukurti Duomenu Irasymo mygtuka

islaidu_lent.bind("<Return>", lambda y: itraukti_irasus())
irasym_btn = Button(islaidu_lent, text="Įtraukti Įrašą arba <Enter>", wraplength=65, justify=CENTER, command=itraukti_irasus)
irasym_btn.grid(row=11, column=0, columnspan=1, ipadx=50, padx=25, pady=(15, 0))


# Irasu rodymo mygtukas

visi_irasai_btn = Button(islaidu_lent, text="Rodyti Išlaidų Įrašus", wraplength=65, justify=CENTER,command=visi_irasai)
visi_irasai_btn.grid(row=11, column=1, columnspan=1, ipadx=50, ipady=7)

# TK Entry lauku kurimas


pajamos_islaidos = Entry(islaidu_lent, width=45)
pajamos_islaidos.grid(row=1, column=1)

pajamos_data = Entry(islaidu_lent, width=45)
pajamos_data.grid(row=2, column=1)

istrinti_pajamu_nr=Entry(islaidu_lent, width=35)
istrinti_pajamu_nr.grid(row=4, column=1)

p_pavadinimas = Entry(islaidu_lent, width=45)
p_pavadinimas.grid(row=5, column=1)

tiekejas = Entry(islaidu_lent, width=45)
tiekejas.grid(row=6, column=1)

mok_budas = Entry(islaidu_lent, width=45)
mok_budas.grid(row=7, column=1)

data = Entry(islaidu_lent, width=45)
data.grid(row=8, column=1)

islaidos = Entry(islaidu_lent, width=45)
islaidos.grid(row=9, column=1)

istrinti_islaidu_nr=Entry(islaidu_lent, width=35)
istrinti_islaidu_nr.grid(row=12, column=1)

# Label kurimas
pajamos_islaidos_label = Label(islaidu_lent, text="Pajamos")
pajamos_islaidos_label.grid(row=1, column=0)

pajamos_data_label = Label(islaidu_lent, text="Pajamų data (Pvz., 2021-09-09)")
pajamos_data_label.grid(row=2, column=0)

istrinti_pajamu_nr_label=Label(islaidu_lent, text="Trinamo Pajamų Įrašo Sąrašo Nr.", font='sans 12 bold')
istrinti_pajamu_nr_label.grid(row=4, column=0)

p_pavadinimas_label = Label(islaidu_lent, text="Prekės pavadinimas")
p_pavadinimas_label.grid(row=5, column=0)

tiekejas_label = Label(islaidu_lent, text="Tiekėjas")
tiekejas_label.grid(row=6, column=0)

mok_budas_label = Label(islaidu_lent, text="Mokėjimo būdas")
mok_budas_label.grid(row=7, column=0)

data_label = Label(islaidu_lent, text="Data (Pvz., 2021-09-09)")
data_label.grid(row=8, column=0)

islaidos_label = Label(islaidu_lent, text="Išlaidų suma")
islaidos_label.grid(row=9, column=0)

istrinti_islaidu_nr_label=Label(islaidu_lent, text="Trinamo Įrašo Sąrašo Nr.", font='sans 12 bold')
istrinti_islaidu_nr_label.grid(row=12, column=0)

status.grid(row=18, columnspan=5, sticky=W+E)

# Lango Isjungimo mygtukas

isjungti_langa_islaidu=Button(islaidu_lent, text="Uždaryti langą arba <Esc>", wraplength=65, justify=CENTER, command=islaidu_lent.quit)
isjungti_langa_islaidu.grid(row=14, column=1, columnspan=1, ipadx=50, ipady=7)
islaidu_lent.bind("<Escape>", lambda x: islaidu_lent.destroy())

islaidu_lent.mainloop()