#Ejercicio 4
def get_prime(num_range):
    primes = []
    for num in num_range:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

n = input ("Ingrese un numero: ")
m = input ("Ingrese otro numero: ")

ranged = get_prime(list(range(int(n), int(m)+1)))
print(ranged)
