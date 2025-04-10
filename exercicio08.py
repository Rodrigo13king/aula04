a = int(input("Digite um número: "))
print(" impares são: ")
for i in range (1, a+1):
    if i % 2 != 0:
        print(f"{i} é ímpar")