aluno = input('Olá! Digite seu nome para saber a suas notas da prova e a sua média: ');
n1 = float(input('Qual a primeira nota?? '));
n2 = float(input('Qual a segunda nota? '));
media = (n1 + n2) / 2;

print(f'Então {aluno}, sua primeira nota foi {n1}, a segunda {n2}, sendo assim, você obteve a média de {media:.1f} nesse semestre.');