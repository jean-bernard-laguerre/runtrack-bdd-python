import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

db = bdd.cursor()

db.execute("SELECT nom, capacite FROM salle")
data = db.fetchall()

print(data)