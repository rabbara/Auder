class Battle:
    def __init__(self, model):
        self.model = model
        
    def simple(self, player_1, player_2):
        print("---------------------- COMBAT SIMPLE ----------------------")
        print("Combat entre {0} et {1}".format(player_1.nom, player_2.nom))
        score = player_1.against(player_2, self.model)
        if score == 1:
            print("VAINQUEUR: \033[32m {0} ({1}) \033[39m".format(player_1.nom, player_1.score))
            print("PERDANT: \033[31m {0} ({1}) \033[39m".format(player_2.nom, player_2.score))
        elif score == 0:
            print("\033[34m EGALITE \033[39m")
        else:
            print("VAINQUEUR: \033[32m {0} ({1}) \033[39m".format(player_2.nom, player_2.score))
            print("PERDANT: \033[31m {0} ({1}) \033[39m".format(player_1.nom, player_1.score))