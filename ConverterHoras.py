def Converte(Horas24): 
    H12 = int(Horas24[:2])
    M12 = Horas24[3:5]

    if H12 == 0:              
        return f"12:{M12} A.M."
    elif H12 < 12:            
        return f"{H12}:{M12} A.M."
    elif H12 == 12:           
        return f"12:{M12} P.M."
    else:                     
        return f"{H12 - 12}:{M12} P.M."

Horas24 = input("Digite as horas HH:MM: ")
Horas12 = Converte(Horas24)
print("Horas em 12h =", Horas12)
