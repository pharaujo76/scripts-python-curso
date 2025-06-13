numero = int(input('Digite um número:  '));

unidade = numero % 10;
dezena = (numero // 10) % 10;
centena = (numero // 100) % 10;
milhar = (numero // 1000) % 10;

print(f'unidade: {unidade} \n dezena: {dezena} \n centena: {centena} \n milhar: {milhar}');