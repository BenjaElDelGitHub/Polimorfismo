from Polimorfismo.Padre import Animal


class perro(Animal):
    def andar(self):
        print("Estoy andando a 4 patas")

class pato(Animal):
    def andar(self):
        print("Estoy andando a 2 patas")


for Animal in perro(), pato():
    Animal.andar()
