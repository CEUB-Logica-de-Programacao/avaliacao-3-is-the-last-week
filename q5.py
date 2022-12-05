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
                if c[x] - c[b[a]] == 1:
                    valido = True
                    break
                valido = False
                break
            a += 1
    return valido


if __name__ == '__main__':
    print(q5('abcc'))
