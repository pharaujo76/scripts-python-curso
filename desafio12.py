produto = float(input('Qual o valor do produto? R$ '));
desconto = produto - (produto * 5 / 100);

print(f'O valor do produto é {produto:.2f} e com o desconto de 5% ficou por {desconto:.2f}');