nome = str(input('Qual seu nome completo? ')).strip();

separador = nome.split(); ## Separando em palavras
primeiro = separador [0]; ## Primeira Palavra
ultimo = separador [-1]; ## Última palavra

print(f'O Primeiro nome da pessoa é {primeiro} e o último é {ultimo}');