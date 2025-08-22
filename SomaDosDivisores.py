def soma_divisores(n):
    soma_pares = 0
    soma_impares = 0
    for i in range(1, n + 1):
        if n % i == 0:  
            if i % 2 == 0:
                soma_pares += i
            else:
                soma_impares += i
    return soma_pares, soma_impares   



numero = int(input("Digite um número inteiro: "))

pares, impares = soma_divisores(numero)  

print(f"Soma dos divisores pares de {numero}: {pares}")
print(f"Soma dos divisores ímpares de {numero}: {impares}")
