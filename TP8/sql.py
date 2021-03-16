#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Author : Mégane Boujeant
"""


import mysql.connector


monServeur = "localhost"
monLogin = "root"
monMdp = "141116!"
maDb = "INLO"
monPort = 3307
connexion = mysql.connector.connect(host=monServeur, user=monLogin,
                                    password=monMdp, database=maDb, port=3307)

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