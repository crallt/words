z = input()

x = 'fkkfg'

w = '_' * len(x)




def found(text, char):
    w = '_' * len(x)
    start = 0
    indexes = []
    while True:
        index = text.find(char, start)
        if index == -1:
            break
        indexes.append(index)
        start = index + 1
    for i in indexes:
        f = x[i]
        w = w[:i] + f + w[i+1:] 
    return w



indexes = found(x, z)


print(indexes)
print(w)