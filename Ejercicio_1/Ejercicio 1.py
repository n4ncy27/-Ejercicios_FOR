#  Hacer el diagrama de flujo y programa en python, que lea 100 numeros enteros y que averigue e imprima
#  cuantos son pares y cuantos son impares

print("--------------------------------------------")
print("-------------Pares y impares ---------------")
print("--------------------------------------------")

pares = 0
impares = 0

for i in range (5):
    x =int (input("digite un numero"))
    if x % 2 == 0:
        pares = pares + 1 
    else:
        impar= impar + 1
print(pares)
print(impares)

