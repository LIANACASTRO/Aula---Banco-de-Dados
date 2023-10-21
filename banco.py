import aula21

while True:
    print('-- Bem vindo ao menu --')
    print('1 - Adicionar aluno')
    print('2 - Editar aluno')
    print('3 - Deletar aluno')
    print('4 - Listar todos os alunos')
    print('5- Sair')
    opcao = input('Selecione uma opção:')
    if opcao == '1':
        nome = input(' Digite o nome do aluno: ')
        idade = int(input(' Digite a idade do aluno: '))
        nota = float(input(' Digite a nota do aluno: '))
        aula21.insert(nome, idade, nota)
    elif opcao == '2':
        nome = input(' Digite o nome do aluno: ')
        idade = int(input(' Digite a idade do aluno: '))
        nota = float(input(' Digite a nota do aluno: '))
        matricula = int(input(' Digite a matricula do aluno: '))
        aula21.update(nome, idade, nota, matricula)
    elif opcao == '3':
        matricula = int(input(' Digite a matricula do aluno: '))
        aula21.delete(matricula)
    elif opcao == '4':
        aula21.select()
    elif opcao == '5':
        break





