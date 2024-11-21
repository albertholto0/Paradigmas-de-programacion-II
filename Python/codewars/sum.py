numbers = [1, 2, 2]

def suma(numbers):
    square_sum = 0
    for i in numbers:
        square_sum += (i * i)
        print(square_sum)
    return square_sum

total = suma(numbers)
print(f"La suma de los cuadrados del arreglo: {total}")
