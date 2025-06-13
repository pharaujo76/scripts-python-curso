tarefas = [];

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa);
    print('Tarefa adicionada com sucesso!');

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa);
        print('Tarefa removida com sucesso!');
    else:
        print('Essa tarefa não pertence a essa lista');

def visualizar_tarefas():
    if len(tarefas) == 0:
        print('Não existe tarefa nessa lista');
    else:
        print('Lista de tarefas:');
    for tarefa in tarefas:
        print('Tarefa - ', tarefa);

while True:
    print('Menu:');
    print('1. Adicionar tarefa');
    print('2. Remover tarefa');
    print('3. Visualizar todas as tarefas');
    print('4. Sair');

    opcao = input('Escolha uma opção: ');

    if opcao == '1':
        tarefa = input('Digite o nome da tarefa:');
        adicionar_tarefa(tarefa);
    elif opcao == '2':
        tarefa = input('Digite o nome da tarefa:');
        remover_tarefa(tarefa);
    elif opcao == '3':
        visualizar_tarefas();
    elif opcao == '4':
        break;
    else:
        print('Opção inválida!');
