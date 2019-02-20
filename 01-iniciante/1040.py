"""
Média 3

Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente
às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para
cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta
média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada
for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um
valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem
"Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo
aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida
por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou
"Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem
"Media final: " seguido da média final para esse aluno.

Entrada
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Saída
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser
impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final
de cada linha, caso contrário obterá "Presentation Error".

--
a, b, c, d = map(float, input().strip().split())
a = a * 2
b = b * 3
c = c * 4

media1 = (a + b + c + d) / 10

print('Media: %.1f' % media1)
if (media1 >= 5) and (media1 <= 6.9):
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: %.1f' % e)
    media2 = (media1 + e) / 2
    if media2 >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % media2)
elif media1 > 7:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')
--

>>> resolve([2.0, 4.0, 7.5, 8.0, 6.4])
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9

>>> resolve([2.0, 6.5, 4.0, 9.0])
Media: 4.8
Aluno reprovado.

>>> resolve([9.0, 4.0, 8.5, 9.0])
Media: 7.3
Aluno aprovado.

"""


def resolve(notas):
    p1 = 2
    p2 = 3
    p3 = 4
    p4 = 1
    media1 = (
            ((notas[0] * p1) + (notas[1] * p2) + (notas[2] * p3) + (notas[3] * p4)) /
            (p1 + p2 + p3 + p4)
    )
    print('Media: %.1f' % media1)
    if (media1 >= 5) and (media1 <= 6.9):
        print('Aluno em exame.')
        print('Nota do exame: %.1f' % notas[4])
        media2 = (media1 + notas[4]) / 2
        if media2 >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: %.1f' % media2)
    elif media1 > 7:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
