import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

db = bdd.cursor()

etages = [["RDC", 0, 500],["R+1", 1, 500]]

salles = [["Lounge", 1, 100],
         ["Studio Son", 1, 5],
         ["Broadcasting", 2, 50],
         ["Bocal pPeda", 2, 4],
         ["Coworking", 2, 80],
         ["Studio Video", 2, 5]]

for etage in etages:
    db.execute(f"INSERT INTO Etage (nom, numero, superficie) VALUES ('{etage[0]}', {etage[1]}, {etage[2]});")

for salle in salles:
    db.execute(f"INSERT INTO Salle (nom, id_etage, capacite) VALUES ('{salle[0]}', {salle[1]}, {salle[2]});")
