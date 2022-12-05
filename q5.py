# ## Questão 5
#
# Sherlock considera uma string válida se todos os caracteres dela aparecerem o mesmo número de vezes.
# Também é válida se ele puder remover apenas um caractere, e os caracteres restantes aparecerem o
# mesmo número de vezes. Dada uma cadeia de caracteres, determine se ela é válida. Se for o caso, retorne `True`, caso
# contrário retorne `False`.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# aabbcd
# ```
#
# A saída deve ser:
#
# ```
# False
# ```
#
# Isso porque não é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abcc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q5(s):
    senha = list(s)
    a = 1
    b = []
    c = {}
    valores = []
    maior = 0
    posicao = 0
    aa = 0
    valido = True
    for x in senha:
        if x not in b:
            b.append(x)
            c[x] = 0
    for x in senha:
        if x in b:
            c[x] += 1
    for x in c:
        while a < len(b):
            if c[x] != c[b[a]]:

                if len(valores) != len(b):
                    for v in c.values():
                        valores.append(v)
                        if len(valores) == len(b):
                            break
                if aa == 0:
                    for i, m in enumerate(valores):
                        if m > maior:
                            maior = m
                            posicao = i
                    if maior != valores[0] and maior != valores[1] and maior != valores[2]:
                        valido = True
                        aa = 1
                        break
                    else:
                        print(maior)
                        print(valores)
                        valores.pop(posicao)
                        print(valores)
                        maior -= 1
                        valores.append(maior)
                        print(valores)
                        aa = 1
                for ab in valores:
                    valido = True
                    break
                valido = False
                break
            a += 1
    print(b)
    print(c)
    return valido


if __name__ == '__main__':
    print(q5('abcc'))
