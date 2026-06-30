class Animal():
    def __init__(self, *args):
        self.nome = args[0],
        self.idade = args[1],
        self.especie = args[2],
        self.extincao = args[3],
        self.peso = args[4]
    

    def comer(self):
        print(f"Está {self} comendo!")

    def brincar(self)
        print(f"Está {self} brincando!")

    def andar(self)
        print(f"Está {self} andando!")

    def deitar(self)
        print(f"Está {self} deitado!")


Cobra = Animal("Luciene", 12, "Cobra Coral", True, "15kg")
