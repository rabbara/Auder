import sys

sys.path.append("../model")
# from model.my_model import My_model

from pokedex import *
# from pokemon import *
from battle import *

import pandas as pd
# import numpy as np

# Chargement du Pokédex
dataset = pd.read_csv("datas\dataset.csv", sep=",", header=0)
pokedex = Pokedex(data=dataset.iloc[:, 0:12])

# Recherche de 2 pokémons
pokemon_1 = pokedex.find(num=7)
pokemon_2 = pokedex.find(num=31)

# Chargement du model
model = My_model(fichier="mod/mod_pokemon.mod")

# Création d'une arene
battle = Battle(model=model)

# Création d'un combat simple
battle.simple(pokemon_1, pokemon_2)
