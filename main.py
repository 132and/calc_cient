from calculadora.__init__ import *

try:
    print('\n CALCULADORA CIENTIFICA \n')
    print('\n1-Digitar uma Expressão matematica \n2-Operar com valores salvos \n0-Para sair do programa')
    option = int(input("\nEscolha uma opção: "))
    while(option != 0):

        if option == 1:
            expression = str(input("\nEntre com a expressao matematica:"))

            n1 = {}
            numbers = []
            operators = []
            operators_aux = []
            valor_sum = 0
            valor_sub = 0
            valor_times = 0
            valor_div = 0
            valor_exp = 0

            # identificar os operadores e numerais
            for element in expression:
                if (element == '+') or (element == '-') or (element == '*') or (element == '/') or (element == 'n1'):
                    operators.append((element))
                else:
                    numbers.append(float(element))

            def prioridade(operators_aux):
            for element in operators:
                if element == '+':
                    return 0
                elif element == '-':
                    return 0
                elif element == '*':
                    return 1
                elif element == '/':
                    return 1
            print(operators_aux)

            for element in operators_aux:
                if element == 0:
                    valor_sum = sum(numbers)

            # Calcular e operar entre as listas
            for element in operators_aux:
                if element == '+' or element == '-'
                for element in numbers:
                        valor_sum = sum(numbers)
                        return 0
                elif element == '-':
                    for element in numbers:
                        valor_sub = sub(numbers)
                        return 0
                elif element == '*':
                    for element in numbers:
                        valor_times = times(numbers)
                        return 1
                elif element == '/':
                    for element in numbers:
                        valor_div = div(numbers)
                        return 1
                elif element == '**':
                    for element in numbers:
                        valor_exp = exp(numbers)

                else:
                    print("Nao existe operação na entrada.")

        valor = valor_sum + valor_sub + valor_div + valor_times

        print("Resposta da expressao: {} ".format(valor))

        expression = str(
            input("\nDigite 'n1' para salvar o valor da expressão: "))
        for element in expression:

            if expression == 'n1':
                n = expression
                n = {n: valor}
                print(n)
            else:
                print("volta programa")


except ZeroDivisionError:
    print('Não e possivel dividir o valor por zero')
except ValueError:
    print('Não e possivel inserir letras nem caracteres especiais')
except EOFError:
    print('Valor não permitido nessa funçao')
