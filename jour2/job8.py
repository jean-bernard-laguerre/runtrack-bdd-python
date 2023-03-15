import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Zoo"
)

db = bdd.cursor()

db.execute("SELECT * FROM Animal")
data = db.fetchall()

print(data)

class Animal:
    def __init__(self, nom, race, naissance, pays):
        self.nom = nom
        self.race = race
        self.naissance = naissance
        self.pays = pays

    def create(self, db):
        db.execute(f"INSERT INTO Animal (nom, race, naissance, pays) VALUES ('{self.nom}', '{self.race}', {self.naissance}, {self.pays})")

    def read(self, db):
        db.execute(f"SELECT * FROM Animal WHERE nom = '{self.nom}' AND race = '{self.race}' AND naissance = {self.naissance} AND pays = {self.pays}")
        data = db.fetchone()
        return data
    
    def update(self, db, nom, race, naissance, pays):
        db.execute(f"UPDATE Animal SET nom = '{nom}', race = '{race}', naissance = {naissance}, pays = {pays} WHERE nom = '{self.nom}' AND race = '{self.race}' AND naissance = {self.naissance} AND pays = {self.pays}")
        self.nom = nom
        self.race = race
        self.naissance = naissance
        self.pays = pays

    def delete(self, db):
        db.execute(f"DELETE FROM Animal WHERE nom = '{self.nom}' AND race = '{self.race}' AND naissance = {self.naissance} AND pays = {self.pays}")
