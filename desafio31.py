cidade = str(input('De qual cidade você quer partir? '));
cidade2 = str(input('Em qual cidade você quer ir? '));
distancia = float(input('Qual a distância de uma cidade para outra? '));

if (distancia <= 200):
    preco = distancia * 0.50;
    print(f'O valor da passagem da viagem partindo de {cidade} e indo para {cidade2} é de R$ {preco:.2f}');
else: 
    preco = distancia * 0.45;
    print(f'O valor da passagem da viagem partindo de {cidade} e indo para {cidade2} é de R$ {preco:.2f}');