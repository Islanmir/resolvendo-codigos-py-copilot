# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Recebendo os números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizando operações matemáticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 if numero2 != 0 else "Indefinido (divisão por zero)"

# Exibindo os resultados
print(f"\nResultados:")
print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} × {numero2} = {multiplicacao}")
print(f"{numero1} ÷ {numero2} = {divisao}")