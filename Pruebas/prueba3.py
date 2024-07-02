#Ejercicio 3
def zero_locator(*args):
    lista = list(map(int, args[0].split(','))) 
    for n in range(len(lista) - 1):
        if lista[n] and lista[n+1] == 0:
            return True
    return False

numbers = input("Enter a list of numbers separated by commas: ")
zero_pair_fount = zero_locator(numbers)

print("Zero pair found: ", zero_pair_fount)