def calcular(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação invalida!"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Soma =", calcular(num1, num2, '+'))
print("Diferença =", calcular(num1, num2, '-'))
print("Produto =", calcular(num1, num2, '*'))
print("Quociente =", calcular(num1, num2, '/'))
