"""
teste


>>> res('vertebrado', 'ave', 'carnivoro')
aguia


>>> res('vertebrado', 'ave', 'onivoro')
pomba


>>> res('vertebrado', 'mamifero', 'onivoro')
homem


>>> res('vertebrado', 'mamifero', 'herbivoro')
vaca

>>> res('invertebrado', 'inseto', 'hematofago')
pulga


>>> res('invertebrado', 'inseto', 'herbivoro')
lagarta


>>> res('invertebrado', 'anelideo', 'hematofago')
sanguessuga


>>> res('invertebrado', 'anelideo', 'onivoro')
minhoca

"""


def resolve(tipo_a, tipo_b, tipo_c):
    if tipo_a == 'vertebrado':
        if tipo_b == 'ave':
            if tipo_c == 'carnivoro':
                return 'aguia'
            if tipo_c == 'onivoro':
                return 'pomba'
        if tipo_b == 'mamifero':
            if tipo_c == 'onivoro':
                return 'homem'
            if tipo_c == 'herbivoro':
                return 'vaca'
    if tipo_a == 'invertebrado':
        if tipo_b == 'inseto':
            if tipo_c == 'hematofago':
                return 'pulga'
            if tipo_c == 'herbivoro':
                return 'lagarta'
        if tipo_b == 'anelideo':
            if tipo_c == 'hematofago':
                return 'sanguessuga'
            if tipo_c == 'onivoro':
                return 'minhoca'

    return ''


"""
Comente as 2 linhas abaixo para submer o desafio
"""


def res(tipo_a, tipo_b, tipo_c):
    print(resolve(tipo_a, tipo_b, tipo_c))


"""
Descomente as linhas abaixo para submer o desafio
"""
# tipo_a = input()
# tipo_b = input()
# tipo_c = input()
#
# print(resolve(tipo_a, tipo_b, tipo_c))
