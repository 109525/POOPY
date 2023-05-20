#POO
#permite segmentar el codigo en pequeñas tareas

"""class Vehiculos:
    Color = "Rosado"
    Marca = "Audi"
    Modelo = 2023
    Precio = 300000000 
    Cilindraje = "2000 CC"
#Instancia del objeto
vehiculo1 = Vehiculo()
print(vehiculo1.Color)"""

class Vehiculo: 
    def __init__(self, Color, Marca, Modelo, Precio, Cilindraje, Encender): 
        self.color = Color
        self.marca = Marca 
        self.modelo = Modelo
        self.precio = Precio
        self.cilindraje = Cilindraje
        self.rebaja = False
        self.encender = Encender
    def InfoProducto(self):
        print(f"Las caracteristicas del vehiculo son:\nColor: {self.color}\nMarca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio}\nCilindraje: {self.cilindraje}")
    def andar(self):
        if self.encender:
            print("Iniciar marcha")
        else:
            print("Debe encender el vehiculo para poder iniciar la marcha")
    def Descuento(self, porcentaje):
        self.precio = self.precio - (self.precio*porcentaje/100)
        if porcentaje < 100:
            self.rebaja = True
            print("Este producto obtuvo un descuento")
#instancia del objeto 
Vehiculo1 = Vehiculo("Rosado", "Audi", 2023, 200000000, "2000 CC", True)
Vehiculo2 = Vehiculo("Blanco", "Chevrolet", 2020, 70000000, "1600 CC", False)
print(Vehiculo1.modelo)
print(Vehiculo2.marca)
Vehiculo1.InfoProducto()

Vehiculo.marca = "Kia"
print(Vehiculo1.marca)
Vehiculo1.andar()
print("El precio del vehiculo 2 es: ", Vehiculo2.precio)
Vehiculo2.Descuento(30)
print("El precio del vehiculo 2 con descuente es: ", Vehiculo2.precio)
Vehiculo1.InfoProducto()
Vehiculo2.InfoProducto()




        