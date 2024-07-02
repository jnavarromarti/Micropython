#Ejercicio 2
def listofwords (*args):
    word = ''.join(args)
    letters = list(word)
    setters = []
    for l in letters:
        if l not in setters:
            setters.append(l)
    setters.sort()
    return setters

word = input("Ingrese una palabra: ")

input = listofwords(word)
print(input)
