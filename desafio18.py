from math import sin,cos,tan,radians;

ang = float(input('Digite o ângulo que você deseja: '));

print(f'O ângulo de {ang} tem o SENO de {sin(radians(ang)):.2f} '); # Utilizando o  sin(Seno) e Radiante com apenas 2 casas após o "." no ponto flutuante
print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang)):.2f} ');
print(f'O ângulo de {ang} tem o TANGENTE de {tan(radians(ang)):.2f} ');
