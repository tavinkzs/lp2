import math

a = int(input("Digite o valor do a: "))
b = int(input("Digite o valor do b: "))
c = int(input("Digite o valor do c: "))

delta = b * b - 4 * a * c

if delta <= 0:
    print("O delta deu negativo ou zero")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("=" * 20)
    print("O resultado do x1 é:", x1)
    print("O resultado do x2 é:", x2)
