from sqlite3 import *

konekcija = connect("bazapodataka.db")
c = konekcija.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Registar (ime TEXT, prezime TEXT, mjesto TEXT, ulica TEXT, zupanija TEXT)')

konekcija.close()
