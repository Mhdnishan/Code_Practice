def reve(sentence):
    rev = ''
    for i in sentence:
        rev = i + rev
    return rev

print(reve("learn python code"))
