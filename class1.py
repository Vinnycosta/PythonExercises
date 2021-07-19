class Televisao():
    def __init__(self):
        self.ligada = True
        self.canal = 0

    def power(self):
        if self.ligada :
            self.ligada = False
        else:
            self.ligada = True

    def aumentacanal(self):
        if self.ligada:
            self.canal = self.canal + 1

    def diminuicanal(self):
        if self.ligada:
            self.canal = self.canal - 1
