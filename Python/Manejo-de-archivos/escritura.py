"""
a para añadir
w para escribr
"""

try:
    archivo = open("archivo_prueba.txt","w",encoding = "UTF-8")
    archivo.write("Hola Albert\n")
    archivo.write("Adiós Albert")
except Exception as e:
    print(e)
