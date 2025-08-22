def Somar(X, Y, Z): 
    S = X + Y + Z 
    return S 

print("Digite X Y Z : ")
X, Y, Z = input().split()
X, Y, Z = int(X), int(Y), int(Z)
Soma = Somar(X, Y, Z)
print("Soma:", Soma)
