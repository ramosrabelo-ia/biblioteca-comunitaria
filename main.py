# Alunos:
# RM 571546 Giovanni Pascon Corrêa
# RM 570351 Luana Ramos Rabelo
# RM 572886 Mariana Ishikawa Mota
# RM 571619 Nicolas Fois Lima
# RM Vitor Matias de Nascimento

# 1. Cadastro do usuário
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
print(f"\033[31mBoas vindas, {nome}! Você tem {idade} anos.\033[m")

# 2 e 3.Empréstimo de livros
romance = 0
aventura = 0
historia = 0
 
while True:
    total = romance + aventura + historia
 
    if total >= 5:
        print("Máximo de 5 livros atingido!")
        break
 
    print("\n=== MENU DE LIVROS ===")
    print("1 - Romance")
    print("2 - Aventura")
    print("3 - História")
    print("4 - Encerrar empréstimos")
 
    opcao = input("Escolha uma opção: ")
 
    match opcao:
        case "1":
            romance += 1
            print("Livro de Romance emprestado!")
 
        case "2":
            aventura += 1
            print("Livro de Aventura emprestado!")
 
        case "3":
            historia += 1
            print("Livro de História emprestado!")
 
        case "4":
            print("Encerrando empréstimos...")
            break
 
        case _:
            print("Opção inválida!")
 
print("\n=== RESUMO DOS EMPRÉSTIMOS ===")

print(f"Usuário  : {nome}") 
print(f"Romance  : {romance}")
print(f"Aventura : {aventura}")
print(f"História : {historia}")
print(f"Total    : {romance + aventura + historia}")

# 4. Cadastro de Entrega 
for i in range(1, total + 1):
    data_valida = False
 
    while data_valida == False:
        print("Digite a data de entrega do livro", i, "(formato DD/MM/AAAA):")
        data = input()
 
        partes = data.split("/")
 
        if len(partes) == 3 and len(partes[0]) == 2 and len(partes[1]) == 2 and len(partes[2]) == 4:
            print("Data do livro", i, "registrada:", data)
            data_valida = True
        else:
            print("Data inválida! Use o formato DD/MM/AAAA.")