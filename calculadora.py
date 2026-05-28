def somar(numero1, numero2):
    return numero1 + numero2 # Função para realizar a soma de dois números

def subtrair(numero1, numero2):
    return numero1 - numero2 # Função para realizar a subtração de dois números

def multiplicar(numero1, numero2):
    return numero1 * numero2 # Função para realizar a multiplicação de dois números

def dividir(numero1, numero2):
    return numero1 / numero2 # Função para realizar a divisão de dois números


print("=" * 30)
print("CALCULADORA PYTHON")
print("=" * 30)

while True: # Loop infinito para permitir que o usuário faça várias operações até decidir encerrar
    numero1 = float(input("Digite o primeiro número: ")) # Solicita ao usuário que digite o primeiro número e converte a entrada para float
    numero2 = float(input("Digite o segundo número: ")) # Solicita ao usuário que digite o segundo número e converte a entrada para float
    operacao = input("Digite a operação desejada (+, -, *, /): ") # Solicita ao usuário que escolha a operação desejada

    if operacao == "+":
        resultado = somar(numero1, numero2) # Chama a função de soma e armazena o resultado
        print(f"O resultado da soma é: {resultado}") # Verifica se a operação escolhida é a soma e imprime o resultado correspondente
    elif operacao == "-":
        resultado = subtrair(numero1, numero2) # Chama a função de subtração e armazena o resultado
        print(f"o resultado da subtração é: {resultado}") # Verifica se a operação escolhida é a subtração e imprime o resultado correspondente
    elif operacao == "*":
        resultado = multiplicar(numero1, numero2) # Chama a função de multiplicação e armazena o resultado
        print(f"O resultado da multiplicação é: {resultado}") # Verifica se a operação escolhida é a multiplicação e imprime o resultado correspondente
    elif operacao == "/":
        if numero2 != 0: # Verifica se o segundo número é diferente de zero para evitar divisão por zero
            resultado = dividir(numero1, numero2)
            print(f"O resultado da divisão é: {resultado}") # Verifica se a operação escolhida é a divisão e imprime o resultado correspondente, caso a divisão seja válida
        else:
            print("Erro: Divisão por zero não é permitida.") # Caso o usuário tente dividir por zero, uma mensagem de erro é exibida
    else:
        print("Operação inválida. Escolha entre +, -, * ou /.") # Caso o usuário escolha uma operação inválida, uma mensagem de erro é exibida

    continuar = input("Deseja continuar? (s/n): ") # Pergunta ao usuário se deseja continuar usando a calculadora
    if continuar.lower() == "n": # Se o usuário escolher "n" ou "N", o loop é encerrado e a calculadora é finalizada
        print("Calculadora encerrada.")
        break # Encerra o loop infinito, finalizando a calculadora