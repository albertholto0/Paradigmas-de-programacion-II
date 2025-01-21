"""
r lectura
"""

# try:
#     archivo = open("archivo_prueba.txt","r",encoding = "UTF-8")
#     lectura_archivo = archivo.read()
#     print(lectura_archivo)
# except Exception as e:
#     print(e)

try:
    archivo = open("archivo_prueba.txt", "r", encoding="UTF-8")
    lectura_archivo = archivo.read()
    print(lectura_archivo)
except FileNotFoundError as e:
    print(f"El archivo no está en esta ruta o no existe... | {e}")