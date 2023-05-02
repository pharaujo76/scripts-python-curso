x = input('Digite qualquer coisa: ');

print(f'{x} é do tipo primitivo', type(x), '!');
print(f'{x} é um número? ', x.isnumeric(), '!');
print(f'{x} são letras? ', x.isalpha(), '!');
print(f'{x} é decimal', x.isdecimal(), '!');
print(f'{x} está em maiusculo?', x.isupper(), '!');
print(f'{x} é um alfanumerico?', x.isalnum(),'!');

print(3*(5+4)**2)