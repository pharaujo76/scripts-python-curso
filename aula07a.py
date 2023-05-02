nome = str(input('Qual é o seu nome? '));

print(f'Prazer em te conhecer, {nome}', '!');

n1 = int(input('Qual o primeiro valor? '));
n2 = int(input('Qual o segundo valor? '));
s = n1 + n2;
m = n1 * n2;
d = n1 / n2;
di = n1 // n2;
e = n1 ** n2;

print(f'A soma é {s}, o produto é {m} e a divisão é {d:3} \n Divisão inteira é {di} e potência é {e:4}');
