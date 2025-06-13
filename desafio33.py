numero = float(input('Digite um número:  '));
numero2 = float(input('Digite outro número '));
numero3 = float(input('Digite mais um número '));
maior = numero;

if (numero2 > maior):
    maior = numero2;
if (numero3 > maior):
    maior = numero3;

menor = numero;

if (numero2 < menor):
    menor = numero2;
if (numero3 < menor):
    menor = numero3;

print(f'O maior número é {maior} e o menor é {menor}');
