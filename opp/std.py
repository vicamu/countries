# Crear un objeto estadística que reciba un valor X y otro valor Y, deben ser listas

class Estadistica:

    def __init__(self,x,y):
        self.x = x if type(x) == list else []
        self.y = y if type(y) == list else []


    @property
    def n(self):
        return len(self.x)

    @property
    def x_mean(self):
        return sum(self.x)/self.n

    @property
    def y_mean(self):
        return sum(self.y)/self.n

    @property
    def x_var(self):
        count = 0
        for value in self.x:
            count += (value - self.x_mean) ** 2 
        return count / self.n

    @property
    def y_var(self):
        count = 0
        for value in self.y:
            count += (value - self.y_mean) ** 2 
        return count / self.n

    @property
    def cov(self):
        valores = list(zip(self.x, self.y))
        XY = 0
        for tupla in valores:
            XY += tupla[0] * tupla[1]
        return (XY / self.n) - (self.x_mean * self.y_mean)

    @property
    def rxy(self):
        return self.cov / ((self.x_var ** 0.5) * (self.y_var ** 0.5))

    @property
    def B(self):
        return self.rxy * ((self.y_var ** 0.5) / (self.x_var ** 0.5))

    @property
    def B0(self):
        return self.y_mean - (self.B * self.x_mean)

    def prediction(self, value):
        return (self.B * value) + self.B0    

    


