media = 7
nota1 = int(input("Portugues:  "))
nota2 = int(input("geografia:  "))
nota3 = int(input("frances:  "))
nota4= int(input("etica:  "))
nota5= int(input("matematica:  "))

print(" aprovados: ")
for i in range (7):
    if i % 2 != 0:
        print(f"{i} reprovados")