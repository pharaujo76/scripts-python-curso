a = int(input('Qual o primeiro valor do triângulo?  '));
b = int(input('Qual o segundo valor do triângulo? '));
c = int(input('Qual o terceiro valor do triângulo? '));

if (a + b > c and b + c > a and a + c > b):
    print('Pode ser um triângulo.');
else:
    print('Não pode ser um triângulo.'); 