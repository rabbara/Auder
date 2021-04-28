class Pokemon:
    def __init__(self, num, nom, type_1, type_2=None, pts_de_vie=None, attaque=None, defense=None,attaque_speciale=None, defense_speciale=None, vitesse=None, generation=None, legendaire=None):
        self.num = num
        self.nom = nom
        self.type_1 = type_1
        self.type_2 = type_2
        self.pts_de_vie = pts_de_vie
        self.attaque = attaque
        self.defense = defense
        self.attaque_speciale = attaque_speciale
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.generation = generation
        self.legendaire = legendaire
        self.score = None

    def predict(self, model):
        self.score = model.predict([[self.pts_de_vie,self.attaque,self.defense,self.attaque_speciale,self.defense_speciale,self.vitesse,self.generation,self.legendaire]])[0]
        return self.score
    
    def against(self, pokemon, model):
        self.predict(model)
        score_2 = pokemon.predict(model)
        if(self.score > score_2):
            return 1
        elif self.score == score_2:
            return 0
        else:
            return -1
    
    def print(self):
        print("ID:{0}, NOM:{1}".format(self.num, self.nom))