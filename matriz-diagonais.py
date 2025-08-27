matriz = [[10, 21, 54],
          [43, 53, 21],
          [64, 32, 89]]

dp = []  
ds = []  
acima = []  

for i in range(3):
    for j in range(3):
        if i == j:
            dp.append(matriz[i][j])
        if i + j == 2:
            ds.append(matriz[i][j])
        if j > i:
            acima.append(matriz[i][j])

print("Diagonal principal:", dp)
print("Diagonal secundária:", ds)
print("Acima da diagonal principal:", acima)
