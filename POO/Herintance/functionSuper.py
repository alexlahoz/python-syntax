
class Persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print(
            " Nombre:", self.nombre, "\n",
            "Edad:", self.edad, "\n",
            "Residencia:", self.lugar_residencia, "\n"
        )

class Empleado(Persona):

    def __init__(self, nombre_empleado, edad_empleado, lugar_residencia_empleado, salario, antiguedad):

        #La instruccion super hace referencia al constructor de la clase padre
        super().__init__(nombre_empleado, edad_empleado, lugar_residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):

        #Hace referencia al metodo de la clase padre y lo ejecuta
        super().descripcion()

        print(
            " Salario:", self.salario, "\n",
            "Antiguedad:", self.antiguedad, "\n"
        )

Antonio = Empleado("Antonio", 55, "Spain", 1200, 5)

Antonio.descripcion()

print(isinstance(Antonio, Empleado))