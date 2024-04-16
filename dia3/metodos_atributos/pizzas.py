#creamos una variable para validar los valores true/false 
import ingredientes import vegetales,masas,proteina

#se crea la clase de objeto pizza 
class Pizzas:
    vegetales = ["tomate","aceituna","champiñon"]
    masas = ["delgada","tradicional"]
    proteina = ["Pollo","vacuno","carne vegetal"]
    precio = 10000
    tamaño = "familiar"
    
#se crea el metodo estatico para darle una funcion al metodo de la clase sin crear otro objeto.
    @staticmethod
    def validar_elemento(elemento,posible_valores): 
        return elemento.lower in posible_valores
    
#se debe crear un metodos para llamar al usuario a elegir su ingrediente
    def hacer_pedido(self):
        self.proteina = input("""ingrese el ingrediente proteina.
            las proteina son:
            pollo,vacuno,carne vegetal""") 

        #creamos una variable para validar los valores true/false 
        self.pizza_validar = self.validar_elemento(self.proteina)

        self.vegetales = []
        vegetal1 = input ("""ingrese el  ingrediente vegetal 1 .
                las opciones son : tomate,aceituna,champiñon""")
        self.vegetales.append(vegetal1) 
        self.pizza_validar = self.validar_elemento(self.vegetales)

        self.vegetales.append(input("""ingrese el ingrediente vegetal.
                            las opciones son: tomate,aceituna,champiñon"""))

#metodo para las masas ingrediente al usuario 
        self.masas = input("""ingrese su tipo de masa a utilizar.
                las opciones son: delgada.tradicional""")

if __name__="_main_": 
    Pizzas = Pizzas()
    Pizzas = hacer_pedido()


#no logre ejecutar bien el codigo profesor la importacion u error no lo decifre !!!!