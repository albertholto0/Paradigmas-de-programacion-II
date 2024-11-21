"""
Albert Alexis Contreras Mendoza
14 de noviembre del 2024
Uso de diccionarios
    son desordenadas y mutables
    # diccionario = {'key1' : 'valor1','key2' : 'valor2'}
"""

profesor = {'nombre' : 'alberto','correo' : 'alberto.mtba@unsij','cubo'  : 12}
print(profesor)
print(f"[Correo]: {profesor.get('correo')}")
print(f"[Cubo]: {profesor['cubo']}")