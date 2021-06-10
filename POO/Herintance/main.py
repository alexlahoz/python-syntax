
class Vehiculos():

    #constructor
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
  
    def acelerar(self):
        self.acelera = True

    def frena(self):
        self.frena = True

    def estado(self):
        print(
            " Marca:", self.marca, "\n",
            "Modelo:", self.modelo, "\n",
            "En marcha:", self.enmarcha, "\n",
            "Acelerando:", self.acelera, "\n",
            "Frenando:", self.frena, "\n"
        )

#Heritance
class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Haciendo caballito"

    def estado(self):
        print(
            " Marca:", self.marca, "\n",
            "Modelo:", self.modelo, "\n",
            "En marcha:", self.enmarcha, "\n",
            "Acelerando:", self.acelera, "\n",
            "Frenando:", self.frena, "\n",
            "Caballito:", self.hcaballito, "\n"
        )

# motoObject = Moto("Honda", "CBR")
# motoObject.frena()
# motoObject.estado()

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
            
# FurgonetaObject = Furgoneta("Renault", "Kangoo")
# FurgonetaObject.arrancar()
# FurgonetaObject.estado()
# print(FurgonetaObject.carga(True))

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

#Herencia multiple, se hace caso al costructor del primero que se mencione
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

biciObject = BicicletaElectrica("Orbea", "H100")
