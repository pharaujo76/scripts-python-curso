import random;

aluno1 = str(input('Primeiro aluno: '));
aluno2 = str(input('Segundo aluno: '));
aluno3 = str(input('Terceiro aluno: '));
aluno4 = str(input('Quarto aluno:  '));

nomes = [aluno1, aluno2, aluno3, aluno4];

print(f'O aluno escolhido foi {random.choice(nomes)}');
