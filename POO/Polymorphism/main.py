class Coche():

    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#La función desplazamientoVehiculo() hace el polimorfismo cuando recibe como parámetro el objeto miVehiculo de la clase Camion()
#De esta forma sabe que la llamada al metodo .desplazamientO() hace referencia a la clase Camion()
miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)