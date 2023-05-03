salAtual = float(input('Qual é o salário do funcionário? R$'));
salNovo = salAtual + (salAtual * 15 / 100);

print(f'Um funcionário que ganhava R${salAtual:.2f}, com 15% de aumento, passa a receber R${salNovo:.2f}');