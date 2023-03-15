import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

db = bdd.cursor()

db.execute("SELECT SUM(superficie) FROM etage")
data = db.fetchall()

print(f"La superficie de la Plateforme est de {data[0][0]} m²")