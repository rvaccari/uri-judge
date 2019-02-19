"""
Lanche

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade
deste item. A seguir, calcule e mostre o valor da conta a pagar.

CODIGO  | ESPECIFICAÇÃO    |  PREÇO
   1    | Cachorro Quente  | R$ 4,00
   2    | X-Salada         | R$ 4,50
   3    | X-Bacon          | R$ 5,00
   4    | Torrada Simples  | R$ 2,00
   5    | Refrigerante     | R$ 1,50


Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade
de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com
2 casas após o ponto decimal.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

--
cod, qtd = map(int, input().strip().split())
itens = [4, 4.5, 5, 2, 1.5]
print('Total: R$ %.2f' % (itens[cod-1] * qtd))
--

>>> resolve(3, 2)
Total: R$ 10.00

>>> resolve(4, 3)
Total: R$ 6.00

>>> resolve(2, 3)
Total: R$ 13.50

"""


def resolve(cod, qtd):
    itens = [4, 4.5, 5, 2, 1.5]
    print('Total: R$ %.2f' % (itens[cod-1] * qtd))
