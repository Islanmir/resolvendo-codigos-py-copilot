# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.
# Dica: Utilize condicionais para realizar a verificação

# Recebendo o número do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se é par ou ímpar (otimizado com operador ternário)
resultado = "par" if numero % 2 == 0 else "ímpar"

# Exibindo o resultado
print(f"O número {numero} é {resultado}.")
