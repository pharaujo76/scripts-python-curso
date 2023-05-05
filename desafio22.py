nome = str(input('Qual seu nome completo? ')).strip(); ## Tirando os espaços inuteis

nome_maiusculas = nome.upper(); 
nome_minusculas = nome.lower();
nome_tamanho = nome.replace(' ', ''); ## Tirando os espaços
numero_letras = len(nome_tamanho); ## Tamanho sem os espaços
palavra1 = nome.split()[0]; ## Separando em palavras e pegando a palavra 1
letraspalavra1 = len(palavra1); ## Tamanho palavra 1

print(f'Seu nome em letras maiúsculas é: {nome_maiusculas} \n Em minúsculas é: {nome_minusculas} \n Seu nome tem {numero_letras} letras \n Seu primeiro nome é {palavra1} e tem {letraspalavra1} de letras ');
