def Testar(X):
    if X > 0:
        return "P"   
    elif X < 0:
        return "N"  
    else:
        return "Z"   

X = int(input("Digite um numero: "))
Tipo = Testar(X)
print("Tipo =", Tipo)
