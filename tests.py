v = [{'nome': 'julio', 'telefone': 929921035522}, {'nome': 'gabe', 'telefone': 11112321313}]

p = {'nome': 'julio', 'telefone': 929921035522}
n = {'nome': 'julio new', 'telefone': 929213213}

i = v.index(p)
print(type(i))

v[i] = n
for i in v:
    print(i)

print(n in v)