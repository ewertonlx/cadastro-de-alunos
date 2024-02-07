user = str(input('Olá usuário! Você é aluno(a) ou professor(a)? Digite "A" caso seja aluno(a) ou "P" caso seja professor(a): '))
student = []
numero_matricula = 1
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
    student.append(aluno)
    print('----------------------------------------------------- \n')
    print(f"\nO estudante {name} foi cadastrado com matrícula de n°{matricula}\n")
    options()
def students(student):
    print("\n-----> ESTUDANTES <-----\n")
    if student:
        for lista in student:
            print(f"Nome: {lista['nome']}, N° da matrícula: {lista['matricula']}, Curso: {lista['curso']}, "
                  f"Nascimento: {lista['nascimento']}, Contato: {lista['contato']} \n")
            print('--------------------------------------------------')
        options()
    else:
        print("Nenhum aluno cadastrado.\n ")
        options()


def remove():
    print

def update():
    print
def options():
    print("\n-----> OPÇÕES <-----\n 1 -> Cadastrar alunos \n 2 -> Ver alunos \n 3 -> Remover alunos \n 4 -> Atualizar alunos")
    option = int(input('Escolha um número: '))
    escolha(option)

def escolha(option):
    if option == 1:
        register(student)
    elif option == 2:
        students(student)
    elif option == 3:
        remove(student)
    elif option == 4:
        update(student)
if user.lower() == 'p' or user.lower() == 'professor' or user.lower() == 'professora':
    options()
elif user.lower() == 'a' or user.lower() == 'aluno' or user.lower() == 'aluna':
    print('Bem-vindo aluno(a)!')
else:
    print(f'{user.lower()} não foi identificado.')