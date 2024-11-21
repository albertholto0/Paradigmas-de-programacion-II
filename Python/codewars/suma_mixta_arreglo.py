def suma_mix(array):
    acum = 0
    for i in array:
        acum += int(i)
    return acum

string_array = [1,'9','3','5',8]
print(f"La suma de los valores del arreglo mixto es de: {suma_mix(string_array)}")


