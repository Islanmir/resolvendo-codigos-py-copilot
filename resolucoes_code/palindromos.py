# Descrição: Vamos testar se uma palavra é um palíndromo?!
# Dica: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Recebendo a palavra do usuário
palavra = input("Digite uma palavra: ")

# Removendo espaços e convertendo para minúsculas para comparação mais precisa
palavra_limpa = palavra.replace(" ", "").lower()

# Invertendo a palavra usando slicing
palavra_invertida = palavra_limpa[::-1]

# Verificando se é um palíndromo
if palavra_limpa == palavra_invertida:
    print(f"'{palavra}' é um palíndromo! ✓")
else:
    print(f"'{palavra}' não é um palíndromo.")

# Mostrando a palavra invertida para referência
print(f"Palavra original: {palavra_limpa}")
print(f"Palavra invertida: {palavra_invertida}")
