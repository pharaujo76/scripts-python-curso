from random import randint;

aleatorio = randint(0,5);
pessoa = int(input('Escolha um número entre 0 e 5:   '));

if (pessoa == aleatorio):
    print(f'Parabéns, o número sorteado foi {aleatorio}, e você acertou!');
else:
    print(f'Infelizmente, você errou, o número sorteado foi {aleatorio}');