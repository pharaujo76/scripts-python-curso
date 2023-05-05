salario = float(input('Digite salário do funcionário: R$ '));

if (salario > 1250):
    aumento = salario * 1.1;
    print(f'O novo salário do funcionário será de R$ {aumento:.2f}');
else:
    aumento = salario * 1.15;
    print(f'O novo salário do funcionário será de R$ {aumento:.2f}');