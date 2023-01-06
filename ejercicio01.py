#Implemente un algoritmo, usando una función recursiva, que resuelva la
#siguiente
#sumatoria: K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
#● El programa debe pedir al usuario que ingrese un número n, y un número P,
#● Luego debe calcular el valor de K(n, p) usando una función recursiva,
#● Debe imprimir el resultado de K(n, p)

n = int(input("Ingrese un numero: "))
p = int(input("Ingrese un numero: "))
def func_recursiva(n,p,acumulado):
    while n>0: 
        acumulado+= n*p
        n -=1
        func_recursiva(n,p,acumulado)
    return acumulado
print(func_recursiva(n,p,0))
