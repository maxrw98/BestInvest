import sqlite3
from sqlite3 import Error

#Verbindungsaufbau mit Fehlerbehandlung
try:
    verbindung = sqlite3.connect("aktien.db")
except sqlite3.Error as e:
    print(e)

#Zeiger zum durchgehen der Daten wird erstellt
zeiger = verbindung.cursor()

#Sql Anfrage wird erstellt
#Es wird eine Tabelle mit dem Angegebenen Werten erstellt
sql = """
CREATE TABLE IF NOT EXISTS aktien (
    Name CHAR(60) PRIMARY KEY,
    Anzahl integer NOT NULL,
    Datum DATE NOT NULL,
    Gebuehren FLOAT NOT NULL,
    Kurs DOUBLE NOT NULL);"""

#Ausführung der Anfrage
zeiger.execute(sql)
#Speichern der Datenbank
verbindung.commit()
#Schließen der Verbindung
verbindung.close()
