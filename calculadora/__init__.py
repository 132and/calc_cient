#eram 60 linhas de código
try:
    sub = lambda numbers: numbers[0]-numbers[1]

    times = lambda numbers: numbers[0]*numbers[1]

    div = lambda numbers: numbers[0]/numbers[1]

    exp = lambda numbers: numbers[0]**numbers[1]

    pi = lambda n1 : n1*3.14

    pi_area = lambda n1 : 3.14*(n1**2)

    def fac(n1):

        if n1 == 0:
            return 0
        if n1 == 1:
            return 1
        if n1 > 1:
            return fac(n1 - 1) * n1

    def log(n1, n2):
        x = n1
        mod = 2
        cont = 0
        while(mod > 1):
            x /= n2
            mod = x % n1
            cont=cont + 1
        return cont


except ZeroDivisionError:
    print('Não e possivel dividir o valor por zero')
except ValueError:
    print('Não e possivel inserir letras nem caracteres especiais')
except EOFError:
    print('Valor não permitido nessa funçao')
