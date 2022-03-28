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


def all_articles():
    cursor = con.cursor()

    SQLBefehl = 'SELECT * FROM tbl_artikel'
    cursor.execute(SQLBefehl)
    row = cursor.fetchone()

    while (row != None):
        print(row)
        row = cursor.fetchone()


all_articles()