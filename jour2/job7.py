import mysql.connector

class Salariee:
    def __init__(self, nom, prenom, salaire, id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def create(self, db):
        db.execute(f"INSERT INTO employes (nom, prenom, salaire, id_service) VALUES ('{self.nom}', '{self.prenom}', {self.salaire}, {self.id_service})")

    def read(self, db):
        db.execute(f"SELECT * FROM employes WHERE nom = '{self.nom}' AND prenom = '{self.prenom}' AND salaire = {self.salaire} AND id_service = {self.id_service}")
        data = db.fetchone()
        return data
    
    def update(self, db, nom, prenom, salaire, id):
        db.execute(f"UPDATE employes SET nom = '{nom}', prenom = '{prenom}', salaire = {salaire}, id_service = {id} WHERE nom = '{self.nom}' AND prenom = '{self.prenom}' AND salaire = {self.salaire} AND id_service = {self.id_service}")
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id

    def delete(self, db):
        db.execute(f"DELETE FROM employes WHERE nom = '{self.nom}' AND prenom = '{self.prenom}' AND salaire = {self.salaire} AND id_service = {self.id_service}")

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Entreprise"
)

salarie = Salariee("Dupuis", "Gertrude", 2500.00, 2)

db = bdd.cursor()

salarie.create(db)
print(salarie.read(db))
salarie.update(db, "Dupuis", "Maxime", 2000, 1)

db.execute("SELECT * FROM employes JOIN Services ON id_service = Services.id")
data = db.fetchall()
salarie.delete(db)

for employe in data:
    print(f"{employe}")


