"""
Aumento de Salário

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a
tabela abaixo:


        Salário	            Percentual de Reajuste
0 - 400.00                          15%
400.01 - 800.00                     12%
800.01 - 1200.00                    10%
1200.01 - 2000.00                    7%
Acima de 2000.00                     4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de
reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de
reajuste ganho, conforme exemplo abaixo.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

>>> resp(400.00)
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

>>> resp(500.00)
Novo salario: 560.00
Reajuste ganho: 60.00
Em percentual: 12 %

>>> resp(800.01)
Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

>>> resp(2000.00)
Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %

>>> resp(3000.00)
Novo salario: 3120.00
Reajuste ganho: 120.00
Em percentual: 4 %

"""


def calc_percent(salario):
    if 0 < salario <= 400:
        return 15
    elif 400.01 < salario <= 800.00:
        return 12
    elif 800.01 <= salario <= 1200:
        return 10
    elif 1200.01 <= salario <= 2000:
        return 7
    return 4


def calc_reajuste(salario, percentual):
    return salario * percentual / 100


def resolve(salario):
    percentual = calc_percent(salario)
    reajuste = calc_reajuste(salario, percentual)
    retorno = 'Novo salario: %.2f\n' % (salario + reajuste)
    retorno += 'Reajuste ganho: %.2f\n' % reajuste
    retorno += 'Em percentual: %i %%' % percentual
    return retorno


# print(resolve(float(input())))

def resp(salario):
    print(resolve(salario))

