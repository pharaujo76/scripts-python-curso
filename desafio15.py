aluguel = int(input('Quantos dias alugados? '));
rodados = float(input('Quantos Km rodados?' ));
resultado = (aluguel * 60) + (rodados * 0.15);

print(f'O total a pagar é de R$ {resultado:.2f}');