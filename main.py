user = str(input('Olá usuário! Apenas professores têm acesso ao painel! Caso você seja um professor, digite: "professor" ou "p": ')) # Pergunta o cargo do usuário.
student = []
numero_matricula = 1
# Função que registra o estudante.
def register(student):
    global numero_matricula
    name = str(input('Nome do aluno: '))
    course = str(input('Digite o curso do aluno: '))
    date = str(input('Digite a data de nascimento do aluno: '))
    email = str(input('Digite o email do aluno: '))
    matricula = int(numero_matricula)
    numero_matricula += 1
    aluno = {
        'nome': name,
        'matricula': matricula,
        'curso': course,
        'nascimento': date,
        'contato': email
    }
    student.append(aluno) # Adiciona o novo aluno à lista.
    print('----------------------------------------------------- \n')
    print(f"\nO estudante {name} foi cadastrado com matrícula de n°{matricula}\n")
    options()
# Função que mostra todos os estudantes.
def students(student):
    print("\n-----> ESTUDANTES <-----\n")
    if student:
        for lista in student:
            print(f"Nome: {lista['nome']}, N° da matrícula: {lista['matricula']}, Curso: {lista['curso']}, "
                  f"Nascimento: {lista['nascimento']}, Contato: {lista['contato']} \n")
            print('--------------------------------------------------')
        options()
    else:
        print("Nenhum aluno está cadastrado.\n ")
        options()

# Função que remove o registro do estudante.
def remove(student):
    print('\n-----> REMOÇÃO DE ESTUDANTES <-----\n')
    print('\nDigite o número da matrícula do estudante que deseja remover!')
    numero = int(input('N°: '))
    
    aluno_encontrado = False
    
    for i in student:
        if numero == i["matricula"]:
            student.remove(i)
            print(f'O aluno {i["nome"]} com matrícula {i["matricula"]} foi removido.')
            aluno_encontrado = True
            break
    
    if not aluno_encontrado:
        print(f"O aluno com matrícula {numero} não foi encontrado!")

    options()
# Função que atualiza o cadastro do estudante.
def update(student):
    print('\n-----> ATUALIZAÇÃ DE ESTUDANTES <-----\n')
    print('\nDigite o número da matrícula do estudante que deseja atualizar!')
    numero = int(input('N°: '))
    aluno_encontrado = False
    for i in student:
        if numero == i["matricula"]:
            i["curso"] = input("Novo curso: ")
            i["nascimento"] = input("Nova data de nascimento: ")
            i["contato"] = input("Novo email: ")
            print(f"Os dados do aluno {i['nome']} foram atualizados com sucesso!")
            aluno_encontrado = True
            break
    
    if not aluno_encontrado:
        print(f"O aluno com matrícula {numero} não foi encontrado!")

    options()

def leave(student):
    print('\n-----> PAINEL ENCERRADO <-----')
# Função que mostra as opções ao professor.
def options():
    print("\n-----> OPÇÕES <-----\n 1 -> Cadastrar alunos \n 2 -> Ver alunos \n 3 -> Remover alunos \n 4 -> Atualizar alunos \n 5 -> Sair")
    option = int(input('Escolha um número: '))
    escolha(option)
# Função que serve pra verificar qual foi a escolha do usuário.
def escolha(option):
    if option == 1:
        register(student)
    elif option == 2:
        students(student)
    elif option == 3:
        remove(student)
    elif option == 4:
        update(student)
    elif option == 5:
        leave(student)
    else: 
        print('Opção não encontrada, painel fechado!')
if user.lower() == 'p' or user.lower() == 'professor' or user.lower() == 'professora': # Verifica se é professor.
    options()
else:
    print(f'Você não tem permissão para acessar o painel!')