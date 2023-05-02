largura = float(input("Digite a largura da parede em metros: "));
altura = float(input("Digite a altura da parede em metros: "));

area = largura * altura;
litros_tinta = area / 2;

print(f'A área da parede é de {area} metros quadrados. \n Será necessário, {litros_tinta} litro(s) para pintar a parede.');