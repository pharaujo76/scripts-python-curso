dinheiro = float(input('Quanto de dinheiro você tem?'));
cotacao_dolar = float(input('Digite o valor do dólar atual: '));

dolar = dinheiro / cotacao_dolar;

print(f'Com o dinheiro que você tem ({dinheiro}) e com base na cotação do dolar atual ({cotacao_dolar}), você pode comprar {dolar} dolares.')
