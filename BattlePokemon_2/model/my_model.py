from sklearn.linear_model import LinearRegression
import joblib

class My_model:
    def __init__(self,model = None, fichier=None):
        if fichier is not None:
            self.model = self.load(fichier)
        else:
            self.model = model
    
    def fit(self,x,y):
        self.model.fit(x,y)
    
    def predict(self,x):
       return self.model.predict(x)
    
    def save(self, fichier):
        joblib.dump(self,fichier)
    
    def load(self, fichier):
        return joblib.load(fichier)
        
    def __str__(self):
        return str(self.model)