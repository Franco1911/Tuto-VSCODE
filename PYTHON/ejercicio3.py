class Usuario:
    nombre = "Franco"

    def__init__(self,nombre):
    # Metodo Constructor
    self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)

franco= Usuario()
franco.nombre= "Franco"

franco.saludar("hello! mi nombre es franco: ")
