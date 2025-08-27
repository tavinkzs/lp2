p1 = str(input("Digite uma frase: "))
p2 = str(input("Digite outra frase: "))

print("="*40)


if p1 == p2:
    print("A primeira frase é igual à segunda")
else:
    print("As frases são diferentes")


if len(p1) < len(p2):
    print("A primeira frase é menor do que a segunda")
elif len(p1) > len(p2):
    print("A segunda frase é menor do que a primeira")
else:
    print("As duas frases têm o mesmo tamanho")


print("\nA primeira frase é: {}\nA segunda frase é: {}".format(p1, p2))
