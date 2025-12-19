# Descrição: Calcular a média de três notas fornecidas na entrada do usuário.
# Dica: Utilize operadores aritméticos para realizar o cálculo da média.

# Recebendo as três notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média usando operadores aritméticos
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultado
print(f"\nAs notas digitadas foram: {nota1}, {nota2}, {nota3}")
print(f"A média das notas é: {media:.2f}")
