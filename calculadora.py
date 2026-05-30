def somar(numero1, numero2): # Função DEF para definir a função de soma, que recebe dois parâmetros (numero1 e numero2)
    return numero1 + numero2 # Função para realizar a soma de dois números. return é usado para retornar o resultado da soma para onde a função foi chamada.

def subtrair(numero1, numero2): # Função DEF para definir a função de subtração, que recebe dois parâmetros (numero1 e numero2)
    return numero1 - numero2 # Função para realizar a subtração de dois números. return é usado para retornar o resultado da subtração para onde a função foi chamada.

def multiplicar(numero1, numero2): # Função DEF para definir a função de multiplicação, que recebe dois parâmetros (numero1 e numero2)
    return numero1 * numero2 # Função para realizar a multiplicação de dois números. return é usado para retornar o resultado da multiplicação para onde a função foi chamada.

def dividir(numero1, numero2): # Função DEF para definir a função de divisão, que recebe dois parâmetros (numero1 e numero2)
    return numero1 / numero2 # Função para realizar a divisão de dois números. return é usado para retornar o resultado da divisão para onde a função foi chamada.


print("=" * 30)
print("CALCULADORA PYTHON")
print("=" * 30)

while True: # Loop infinito para permitir que o usuário faça várias operações até decidir encerrar
    
    # 29/05/26 - Terceiro dia trabalhando na calculadora python, dessa vez irei utilizar a função try e except ao digitar um número, para evitar que o programa quebre caso o usuário digite algo que não seja um número

    # 29/05/26 - No terceiro dia estou criando também um Menu de opções para o usuário escolher a operação desejada, utilizando um loop while para exibir o menu repetidamente até que o usuário escolha sair.
    print("\n===== MENU DE OPERAÇÕES =====")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Escolha uma opção: ") # Solicita ao usuário que escolha uma opção desejada

    if opcao == "5": # Verifica se a opção escolhida é "5", que é a opção para sair da calculadora
        print("Calculadora encerrada.") # Imprime uma mensagem indicando que a calculadora foi encerrada
        break # Encerra o loop infinito, finalizando a calculadora
    
    # 29/05/26 - Verifica se a opção escolhida é válida (entre 1 e 5). Se a opção for inválida, uma mensagem de erro é exibida e o loop reinicia, permitindo que o usuário tente novamente.
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Operação inválida. Escolha uma opção entre 1 e 5.") # not in é usado para verificar se a opção escolhida pelo usuário não está na lista de opções válidas. Se a opção for inválida, uma mensagem de erro é exibida.
        continue # Se o usuário escolher uma opção inválida, o loop reinicia, permitindo que o usuário tente novamente

    # 29/05/26 - Inverti a ordem do código para solicitar os números após o usuário escolher a operação, para evitar que o usuário digite números desnecessariamente caso queira apenas sair ou escolher uma operação inválida. Dessa forma, os números só serão solicitados se o usuário escolher uma operação válida (1 a 4).

    try: # O bloco try tenta executar o código que pode gerar uma exceção, neste caso, a conversão de entrada para float. Se o usuário digitar algo que não seja um número, a exceção ValueError será capturada e tratada no bloco except.
        numero1 = float(input("Digite o primeiro número: ")) # Solicita ao usuário que digite o primeiro número e converte a entrada para float
        numero2 = float(input("Digite o segundo número: ")) # Solicita ao usuário que digite o segundo número e converte a entrada para float
    except ValueError: # Se o usuário digitar algo que não seja um número, uma mensagem de erro será exibida e o loop continuará, permitindo que o usuário tente novamente.
        print("Erro: Por favor, digite apenas números.")
        continue # O comando continue faz com que o loop reinicie imediatamente, permitindo que o usuário tente novamente sem encerrar o programa

    if opcao == "1": # 29/05/26 - Verifica se a opção escolhida é "1". Também alterei a variável de operacao para opcao para facilitar a leitura do código, já que o usuário escolhe a operação através do menu de opções.
        resultado = somar(numero1, numero2) # Chama a função de soma e armazena o resultado
        print(f"O resultado da soma é: {resultado}") # Verifica se a operação escolhida é a soma e imprime o resultado correspondente
    elif opcao == "2": # Verifica se a opção escolhida é "2"
        resultado = subtrair(numero1, numero2) # Chama a função de subtração e armazena o resultado
        print(f"o resultado da subtração é: {resultado}") # Verifica se a operação escolhida é a subtração e imprime o resultado correspondente
    elif opcao == "3": # Verifica se a opção escolhida é "3"
        resultado = multiplicar(numero1, numero2) # Chama a função de multiplicação e armazena o resultado
        print(f"O resultado da multiplicação é: {resultado}") # Verifica se a operação escolhida é a multiplicação e imprime o resultado correspondente
    elif opcao == "4": # Verifica se a opção escolhida é "4"
        if numero2 != 0: # Verifica se o segundo número é diferente de zero para evitar divisão por zero
            resultado = dividir(numero1, numero2)
            print(f"O resultado da divisão é: {resultado}") # Verifica se a operação escolhida é a divisão e imprime o resultado correspondente, caso a divisão seja válida
        else:
            print("Erro: Divisão por zero não é permitida.") # Caso o usuário tente dividir por zero, uma mensagem de erro é exibida

    continuar = input("Deseja continuar? (s/n): ") # Pergunta ao usuário se deseja continuar usando a calculadora
    if continuar.lower() == "n": # Se o usuário escolher "n" ou "N", o loop é encerrado e a calculadora é finalizada
        print("Calculadora encerrada.")
        break # Encerra o loop infinito, finalizando a calculadora