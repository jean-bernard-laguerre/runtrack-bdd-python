import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

db = bdd.cursor()

db.execute("CREATE TABLE Etage(id INT NOT NULL AUTO_INCREMENT,nom VARCHAR(255) NOT NULL,numero INT NOT NULL,superficie INT NOT NULL,PRIMARY KEY (id));")

db.execute("CREATE TABLE Salle(id INT NOT NULL AUTO_INCREMENT,nom VARCHAR(255) NOT NULL,id_etage INT NOT NULL,capacite INT NOT NULL,PRIMARY KEY (id));")
