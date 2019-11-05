from calculadora.__init__ import *

try:
    
    print('\n CALCULADORA CIENTIFICA \n')
    print('\n 1-Soma\n 2-Subtracao\n 3-Multiplicacao\n 4-Divisao\n 5-Exponencial\n 6-Multiplicacao por "PI"\n 7-Area do circulo\n 8-Fatorial\n 9-Logaritimo\n 0-Para sair do programa')
    option = int(input("\nEscolha uma opção: "))


    while(option != 0):
        if option == 1:
            a = float(input("\nEntre com um numero a ser somado:"))
            b = float(input("Entre com outro numero:"))
            valor = sum(a, b)
            print("\nA soma de {} com {} é {}\n".format(b, a, valor))
            break
            
        elif option == 2:
            a = float(input("\nEntre com um numero:"))
            b = float(input("Entre com o outro numero:"))
            valor = sub(a, b)
            print("\nA subtracao de {} por {} é: {}\n".format(a, b, valor))
            break
        
        elif option == 3:
            a = float(input("\nEntre com um numero:"))
            b = float(input("Entre com o outro numero:"))
            valor = times(a, b)
            print("\nA multiplicacao de {} por {} é: {}\n".format(a, b, valor))
            break

        elif option == 4:
            a = float(input("\nEntre com um numero:"))
            b = float(input("Entre com o outro numero:"))
            valor = div(a, b)
            print("\nA divisao de {} por {} é: {}\n".format(a, b, valor))
            break

        elif option == 5:
            a = float(input("\nEntre com um numero:"))
            b = float(input("Entre com o exponecial:"))
            valor = exp(a, b)
            print("\nO resultado de {} elevado por {} é: {}\n".format(a, b, valor))
            break

        elif option == 6:
            a = float(input("\nEntre com um numero:"))
            valor = pi(a)
            print("\nO resultado de {} multiplicado por PI(3,14) é: {}\n".format(a, valor))
            break

        elif option == 7:
            a = float(input("\nEntre com o valor do raio do circulo:"))
            valor = pi_area(a)
            print("\nA area do circulo é: {}\n".format(valor))
            break

        elif option == 8:
            a = float(input("\nEntre com o valor a ser fatorado:"))
            valor = fac(a)
            print("\nO valor da fatoração é: {}\n".format(valor))
            break

        elif option == 9:
            a = float(input("\nEntre com o numero da base:"))
            b = float(input("Entre com o numero de log:"))
            valor = log(b, a)
            print("\nO logaritimo de {} na base {} é {}\n".format(b, a, valor))
            break

        else:
            print('Escolha uma opção valida!!!')
            

except ZeroDivisionError:
    print('Não e possivel dividir o valor por zero')
except ValueError:
    print('Não e possivel inserir letras nem caracteres especiais')
except EOFError:
    print('Valor não permitido nessa funçao')
