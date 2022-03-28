import mysql.connector

Servername = '127.0.0.1'  # Rechnername (localhost ist dein eigener Rechner)
Benutzer = 'root'
Passwort = ''
Datenbank = 'db_autoteile'

con = mysql.connector.connect(
    host=Servername,
    user=Benutzer,
    database=Datenbank,
    password=Passwort)


def run_sql(sql):
    cursor = con.cursor()

    SQLBefehl = sql
    cursor.execute(SQLBefehl)
    row = cursor.fetchone()

    while (row != None):
        print(row)
        row = cursor.fetchone()


#1) all Aricles
#run_sql('SELECT * FROM tbl_artikel')

#2) all Names an Prices
#run_sql('SELECT Artikelbezeichnung, ArtikelPreis FROM tbl_artikel')

#3) typ feder
#run_sql('SELECT Artikelbezeichnung, ArtikelPreis FROM tbl_artikel WHERE Warentyp = "Feder"')

#4) price > 20
#run_sql('SELECT Artikelbezeichnung, ArtikelPreis FROM tbl_artikel WHERE ArtikelPreis > 20')

#5) Date = 04.1.2022
#run_sql('SELECT Artikelbezeichnung FROM tbl_artikel WHERE Kaufdatum = "2022-01-04"')

#6) Date between 1.1.2020 and 1.1.2022
#run_sql('SELECT Artikelbezeichnung FROM tbl_artikel WHERE (Kaufdatum BETWEEN "2020-01-01" AND "2022-01-01")')

#7) contains liqui
#run_sql('SELECT Artikelbezeichnung, ArtikelPreis FROM tbl_artikel WHERE Artikelbezeichnung LIKE "%Liqui%"')

#8) typ Schmierstoff
#run_sql('SELECT Artikelbezeichnung, ArtikelPreis FROM tbl_artikel WHERE Warentyp = "Schmierstoff"')

#9) typ Schmierstoff alphabetisch order
#run_sql('SELECT Artikelbezeichnung, ArtikelPreis FROM tbl_artikel WHERE Warentyp = "Schmierstoff" ORDER BY Artikelbezeichnung ASC')

#10) all WarenTyp
#run_sql('SELECT WarenTyp FROM tbl_artikel GROUP BY WarenTyp')