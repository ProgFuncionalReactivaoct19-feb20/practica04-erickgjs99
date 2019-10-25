"""
    autor = erickgjs_99
    file = practica,py

"""
import codecs
import json
# para abrir el archivo
archivo = codecs.open("datos.txt", "r")
# para leer todas las lineas de cadenas del archivo
line_dic = archivo.readlines()
# para que se guarde todas las cadenas en una lista
line_dic = [json.loads(l) for l in line_dic]
# funcion para los goles 
funcion = lambda x: list((x.items()))[1][1] > 3
#para que se guarde 
gol = list(filter(funcion, line_dic))
print(list(gol))
# JUgadores de nigeria
funcion2 = lambda x: list((x.items()))[0][1] == "Nigeria"
country = list(filter(funcion2, line_dic)) 
#impresion de los resultados de jugadores de nigeria
print(list(country))
#el valor minimo 
#el valor maximo
funcion3 = list(map(lambda x: list(x.items()) [2][1], line_dic))
minimo_p = min(funcion3)
maximo_p = max(funcion3) 
#impresion de los resultados del minimo peso
print((minimo_p))
#impresion de los resultados del maximo peso
print((maximo_p))  