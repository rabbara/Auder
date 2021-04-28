import pandas as pd
import numpy as np

import sys

sys.path.append("../model")
from model.my_model import My_model

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

dataset = pd.read_csv("datas\dataset.csv", sep=",", header=0)
dataset = dataset.dropna(axis=0, how="any")

X = dataset.iloc[:, 4:12].values
Y = dataset.loc[:, "RATIO_VICTOIRES"].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

list_algo = [DecisionTreeRegressor(), RandomForestRegressor(), LinearRegression()]

list_score = dict()
list_score["Algorithme"] = list()
list_score["SCORE"] = list()

for algo in list_algo:
    model = My_model(model=algo)
    model.fit(X_train, Y_train)  # On entraine le model avec le jeu d'entrainement
    Y_predict = model.predict(X_test)  # On fait une prédiction avec notre jeu de test
    score = r2_score(Y_test, Y_predict)  # On évalue notre prédictions
    list_score["Algorithme"].append(model)
    list_score["SCORE"].append(score)

# ---------------------------------------------------------------- EVALUATION -------------------------------------------------------------------------------
print("________________________________EVALUATION________________________________")
df_score = pd.DataFrame(list_score).sort_values("SCORE", ascending=False)
print(df_score)

# On sauvegarde le model avec le meilleur score
model = My_model(model=RandomForestRegressor())
model.fit(X_train, Y_train)
model.save("mod/mod_pokemon.mod")
