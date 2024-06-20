def code(source, end, data):

    codData = ''
    for char in data:
        codData += end[source.index(char)]
    return codData

key1 = input()
key2 = input()
decode = input()
encode = input()

print(code(key1, key2, decode))
print(code(key2, key1, encode))