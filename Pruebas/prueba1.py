import statistics
def devolver_distintos (*args):
    numbers = list(args)
    sum_numbers = sum(numbers)
    if sum_numbers > 15:
        return max(numbers)
    elif sum_numbers < 10:
        return min(numbers)
    else:
        return statistics.mean(numbers)
    
numbers = []
for i in range(3):
    number = int(input("Ingrese un número: "))
    numbers.append(number)

print(devolver_distintos(*numbers))
