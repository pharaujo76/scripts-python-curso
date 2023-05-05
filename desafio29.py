velocidade = float(input('Qual a velocidade em que o carro estava? '));

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print(f'Você estava acima da velocidade ({velocidade}Km), e foi multado em: R$ {multa:.2f}' );
else:
    print(f'Sua velocidade nessa via era de {velocidade}Km, então, você não foi multado esse dia, favor, conferir outras datas.');