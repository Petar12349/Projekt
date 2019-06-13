from tkinter import *
from sqlite3 import *

master = Tk()
master.title("Zute Stranice") 
master.geometry('450x850+0+0')
master.configure(background='#CCCC00')
naslov = Label(master, text="Zute stranice", font=("arial",30,"bold"), fg="white", bg="Black", relief="raised", bd="7").place(x=100, y=30)
img = PhotoImage(file="")

con = connect('bazapodataka.db') 
c = con.cursor() 





L1 = Label(master, text = "Ime", font=("arial",18) ,bg="#FFFF00", bd="1").place(x=10,y=250)
L2 = Label(master, text = "Prezime", font=("arial",18) ,bg="#FFFF00", bd="1").place(x=10,y=300)
L3 = Label(master, text = "Mjesto", font=("arial",18) ,bg="#FFFF00", bd="1").place(x=10,y=350)
L4 = Label(master, text = "Ulica", font=("arial",18) ,bg="#FFFF00", bd="1").place(x=10,y=400)
L5 = Label(master, text = "Zupanija", font=("arial",18) ,bg="#FFFF00", bd="1").place(x=10,y=450)
L6 = Label(master, text="Dodavanje u Registar:", font=("arial", 20), bg="#FFFF00", bd="5").place(x=90,y=160)






ime= Entry(master, bd="6")
ime.place(x=300,y=250)

prezime= Entry(master, bd="6")
prezime.place(x=300,y=300)

mjesto= Entry(master, bd="6")
mjesto.place(x=300,y=350)

ulica= Entry(master, bd="6")
ulica.place(x=300,y=400)

zupanija= Entry(master, bd="6")
zupanija.place(x=300,y=450)

frame = Frame(master)
frame.place(x= 10, y = 550)           
Lb = Listbox(frame, height = 15, width = 67,font=("arial", 8)) 
Lb.pack(side = LEFT, fill = Y)           
scroll = Scrollbar(frame, orient = VERTICAL)
scroll.config(command = Lb.yview)
scroll.pack(side = RIGHT, fill = Y)
Lb.config(yscrollcommand = scroll.set)           
Lb.insert(0, "ime, prezime, mjesto, ulica, zupanija")






def pretraga():
    
        print("Pretraga izvrsena")
        
        c.execute('SELECT ime FROM Registar WHERE ime = ?', (ime.get(),))
        if c.fetchone():
            L7 = Label(master, text="Pronadjeni korisnici", fg="blue", bd="5", width="17").place(x=10, y=790)
        else:
            L7 = Label(master, text="Nema odgovarajucih korisnika", fg="red", bd="5").place(x=10, y=790)  
        a = c.execute('SELECT * FROM Registar WHERE ime LIKE (?)', (ime.get(),))
        podaci = c.fetchall()
        for a in podaci:
                Lb.insert(1,a)
        '''
        c.execute('SELECT prezime FROM Registar WHERE prezime = ?', (prezime.get(),))
        if c.fetchone():
            L7 = Label(master, text="Pronadjeni korisnici", fg="greem", bd="5", width="17").place(x=260, y=440)
        else:
            L7 = Label(master, text="Nema odgovarajucih korisnika", fg="red", bd="5").place(x=260, y=440)
        b = c.execute('SELECT * FROM Registar WHERE prezime LIKE (?)', (prezime.get(),))
        podaci = c.fetchall()
        for b in podaci:
                Lb.insert(1,b)

        c.execute('SELECT mjesto FROM Registar WHERE mjesto = ?', (mjesto.get(),))
        if c.fetchone():
            L7 = Label(master, text="Pronadjeni korisnici", fg="greem", bd="5", width="17").place(x=260, y=440)
        else:
            L7 = Label(master, text="Nema odgovarajucih korisnika", fg="red", bd="5").place(x=260, y=440)
        d = c.execute('SELECT * FROM Registar WHERE mjesto LIKE (?)', (mjesto.get(),))
        podaci = c.fetchall()
        for d in podaci:
                Lb.insert(1,d)

        c.execute('SELECT ulica FROM Registar WHERE ulica = ?', (ulica.get(),))
        if c.fetchone():
            L7 = Label(master, text="Pronadjeni korisnici", fg="green", bd="5", width="17").place(x=260, y=440)
        else:
            L7 = Label(master, text="Nema odgovarajucih korisnika", fg="red", bd="5").place(x=260, y=440)
        e = c.execute('SELECT * FROM Registar WHERE ulica LIKE (?)', (ulica.get(),))
        podaci = c.fetchall()
        for e in podaci:
                Lb.insert(1,e)

        c.execute('SELECT prezime FROM Registar WHERE zupanija = ?', (zupanija.get(),))
        if c.fetchone():
            L7 = Label(master, text="Pronadjeni korisnici", fg="green", bd="5", width="17").place(x=260, y=440)
        else:
            L7 = Label(master, text="Nema odgovarajucih korisnika", fg="red", bd="5").place(x=260, y=440)
        f = c.execute('SELECT * FROM Registar WHERE zupanija LIKE (?)', (zupanija.get(),))
        podaci = c.fetchall()
        for f in podaci:
                Lb.insert(1,f)
                
        '''
        con.commit()
        
        

        ime.delete(0, END)
        prezime.delete(0, END)
        mjesto.delete(0, END)
        ulica.delete(0, END)
        zupanija.delete(0, END)








def dodaj_korisnika():
    
        print("Korisnik dodan")

        c.execute('INSERT INTO Registar (ime, prezime, mjesto, ulica, zupanija) VALUES (?, ?, ?, ?, ?)',
                  (ime.get(), prezime.get(), mjesto.get(), ulica.get(),zupanija.get()))
        con.commit()
        ime.delete(0, END)
        prezime.delete(0, END)
        mjesto.delete(0, END)
        ulica.delete(0, END)
        zupanija.delete(0, END)




def izbrisi_korisnika():
    
        print ("Korisnik je izbrisan")
        c.execute("DELETE FROM Registar WHERE ime = '" + ime.get() + "'")
        con.commit()
        ime.delete(0, END)
        prezime,delete(0, END)
        mjesto.delete(0, END)
        ulica.delete(0, END)
        zupanija.delete(0, END)




       
def ispis():
        print("Podaci iz baze podataka ispisani")
        c.execute('SELECT * FROM Registar')
        podaci = c.fetchall()
            
        for row in podaci:
                Lb.insert(1,row)         

        con.commit()







button1 = Button(master, text="Pretraga korisnika",command=pretraga)
button1.place(x=10,y=500)

button2 = Button(master, text="Dodaj korisnika",command=dodaj_korisnika)
button2.place(x=118,y=500)

button3 = Button(master, text="Izbrisi korisnika",command=izbrisi_korisnika)
button3.place(x=213,y=500)

button4 = Button(master, text="Ispis podataka", command=ispis)
button4.place(x=350, y=790)






master.mainloop()
c.close()
conn.close()
