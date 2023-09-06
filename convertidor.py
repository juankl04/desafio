import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen=="celsius" and unidad_destino == "fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    else:
        return None
    
def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen =="kilogramos" and unidad_destino == "gramos":
        return temperatura.kilogramos_a_gramos(valor)
    else:
        return None
    
def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen=="segundos" and unidad_destino == "minutos":
        return temperatura.celsius_a_fahrenheit(valor)
    else:
        return None
    
if __name__=="__main__":
    valor = 20
    unidad_de_origen = "celsius"
    unidad_de_destino = "fahrenheit"
    resultados = convertir_temperatura(valor, unidad_de_origen, unidad_de_destino )
    print(f"{valor} de {unidad_de_origen} son equivalentes a {resultados} {unidad_de_destino}")
     
    valor = 70
    unidad_de_origen = "segundos"
    unidad_de_destino = "minutos"
    resultados = convertir_temperatura(valor, unidad_de_origen, unidad_de_destino )
    print(f"{valor} de {unidad_de_origen} son equivalentes a {resultados} {unidad_de_destino}")
    
    valor = 100
    unidad_de_origen = "kilogramos"
    unidad_de_destino = "gramos"
    resultados = convertir_temperatura(valor, unidad_de_origen, unidad_de_destino )
    print(f"{valor} de {unidad_de_origen} son equivalentes a {resultados} {unidad_de_destino}")