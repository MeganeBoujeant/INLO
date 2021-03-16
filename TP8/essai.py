#!/usr/bin/python3
import mysql.connector

monServeur = "club.i2m.univ-amu.fr"
monLogin = "megane"
monMdp = "eYkNM4Hfd8WacBdnF"
maDb="megane_inlo"
connexion = mysql.connector.connect(host = monServeur, user = monLogin, password=monMdp, database=maDb)
curseur = connexion.cursor()

curseur.execute("SELECT * FROM `user` ")
# ne retourne qu’une seule ligne
#row = curseur.fetchone()
# on récupère la ligne résultat
#print("ligne 1 : ", row[0])
myresult = curseur.fetchall()
for x in myresult:
  print(x)

curseur.close()
connexion.close()