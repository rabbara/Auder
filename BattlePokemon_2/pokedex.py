import pandas as pd
from pokemon import *

import sys
sys.path.append("../model")
from model.my_model import My_model

class Pokedex:
    def __init__(self, data):
        self.data = data  
    
    def find(self,num):   
        index_pokemon = self.data[self.data["NUMERO"] == num].index
        df_pokemon = self.data.iloc[index_pokemon,:]
        pokemon = Pokemon(
            num=df_pokemon["NUMERO"].values[0],
            nom=df_pokemon["NOM"].values[0], 
            type_1=df_pokemon["TYPE_1"].values[0], 
            type_2=df_pokemon["TYPE_2"].values[0], 
            pts_de_vie=df_pokemon["POINTS_DE_VIE"].values[0], 
            attaque=df_pokemon["POINTS_ATTAQUE"].values[0], 
            attaque_speciale=df_pokemon["POINTS_ATTAQUE_SPECIALE"].values[0], 
            defense=df_pokemon["POINTS_DEFFENCE"].values[0], 
            defense_speciale=df_pokemon["POINT_DEFENSE_SPECIALE"].values[0], 
            vitesse=df_pokemon["POINTS_VITESSE"].values[0], 
            generation=df_pokemon["NOMBRE_GENERATIONS"].values[0], 
            legendaire=df_pokemon["LEGENDAIRE"].values[0]
        )
        
        return pokemon