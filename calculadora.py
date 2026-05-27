print("Calculadora Python")

while True: # Loop infinito para permitir que o usuário faça várias operações até decidir encerrar
    numero1 = float(input("Digite o primeiro número: ")) # Solicita ao usuário que digite o primeiro número e converte a entrada para float
    numero2 = float(input("Digite o segundo número: ")) # Solicita ao usuário que digite o segundo número e converte a entrada para float
    operacao = input("Digite a operação desejada (+, -, *, /): ") # Solicita ao usuário que escolha a operação desejada

    soma = numero1 + numero2 # Realiza a soma dos dois números
    subtracao = numero1 - numero2 # Realiza a subtração dos dois números
    multiplicacao = numero1 * numero2 # Realiza a multiplicação dos dois números

    if operacao == "+":
        print(f"O resultado da soma é: {soma}") # Verifica se a operação escolhida é a soma e imprime o resultado correspondente
    elif operacao == "-":
        print(f"o resultado da subtração é: {subtracao}") # Verifica se a operação escolhida é a subtração e imprime o resultado correspondente
    elif operacao == "*":
        print(f"O resultado da multiplicação é: {multiplicacao}") # Verifica se a operação escolhida é a multiplicação e imprime o resultado correspondente
    elif operacao == "/":
        if numero2 != 0: # Verifica se o segundo número é diferente de zero para evitar divisão por zero
            divisao = numero1 / numero2 # Realiza a divisão dos dois números
            print(f"O resultado da divisão é: {divisao}")
        else: # Se o segundo número for zero, exibe uma mensagem de erro
            print("Erro: Divisão por zero não é permitida.")
    else: # Se a operação escolhida não for válida, exibe uma mensagem de erro
        print("Operação inválida. Escolha entre +, -, * ou /.")

    continuar = input("Deseja continuar? (s/n): ") # Pergunta ao usuário se deseja continuar usando a calculadora
    if continuar == "n": # Se o usuário escolher "n", o loop é encerrado e a calculadora é finalizada
        print("Calculadora encerrada.")
        break # Encerra o loop infinito, finalizando a calculadora