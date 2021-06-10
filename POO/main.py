
class Coche():

    # Constructor
    def __init__(self):
        # Proprieties
        self.__largoChasis = 250
        self.__anchoChasis = 120
        # Encapsulation
        # La propiedad ruedas no será accesible desde el exterior de la clase
        # Solo podra ser modificada desde el interior por ejemplo mediante un metodo
        # Para esto se utiliza __
        self.__ruedas = 4
        self.__enmarcha = False

    # Methods
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif (self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. No se puede arrancar"

        else:
            return "El coche esta parado"

    # Encapsulated Method
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True

        else:
            return False

    def estado(self):
        print(
            "Ruedas:", self.__ruedas, "Ancho:", self.__anchoChasis, "Largo:", self.__largoChasis
        )


# Object
# Instanciar la clase
micoche = Coche()

# print("El largo del coche es:", micoche.largoChasis)
# print("El Coche tiene:", micoche.__ruedas, "Ruedas")

print(micoche.arrancar(True))

print()
print("###########################")
print()

micoche2 = Coche()

micoche2.puertas = "abiertas"
print(micoche2.arrancar(False))
# micoche2.estado()
