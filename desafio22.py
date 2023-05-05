nome = str(input('Qual seu nome completo? '));

nome_maiusculas = nome.upper(); 
nome_minusculas = nome.lower();
nome_tamanho = nome.replace(' ', ''); ## Tirando os espaços
numero_letras = len(nome_tamanho); ## Tamanho sem os espaços
palavra1 = nome.split()[0]; ## Separando em palavras e pegando a palavra 1
letraspalavra1 = len(palavra1); ## Tamanho palavra 1

print(f'{nome_maiusculas} \n {nome_minusculas} \n {numero_letras} \n {letraspalavra1}');
