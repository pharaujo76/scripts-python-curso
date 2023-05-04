from math import sqrt,hypot;

catoposto = float(input('Comprimento do cateto oposto: '));
catadjacente = float(input('Comprimento do cateto adjaceste: '));

## hipotenusa = sqrt(catoposto ** 2 + catadjacente ** 2);

hi = hypot(catoposto, catadjacente); ## Importação com math

print(f'A hipotenusa vai medir {hi:.2f}');
