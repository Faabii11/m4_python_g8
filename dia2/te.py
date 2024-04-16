# Clase Te_artesanal para representar informacion sobre variedades de te artesanal
class Te_artesanal():
    # Duración del te (sin preparar)
    duracion = "365 días o 1 año"
        
    # Metodo estatico para obtener la preparacion recomendada de un te especifico
    @staticmethod
    def obt_preparacion_recomendacion(n):
        # Menu de te con sus respectivos detalles de preparacion. El usuario tendrá que ingresar el número de la alternativa deseada
        menu =  {
            1 : ['Té negro' , '3 min' , 'Desayuno'] ,
            2 : ['Té verde' , '5 min' , 'Medio Día'] ,
            3 : ['Agua de hierbas' , '6 min' , 'Atardecer']
        }
        # Retorna los detalles de preparacion del te seleccionado
        return tuple(menu[n])
    
    # Metodo estatico para obtener el precio del te en un formato especifico
    @staticmethod
    def obt_precio_formato(precio):
        # Precios del te con un formato específico
        menu =  {
            300 : 3000 ,  # 300 gramos a $3000
            500 : 5000   # 500 gramos a $5000
        }
        # Retorna el precio formateado del te
        return menu[precio]