string = str(input('insira a palavra: '))
string_reversa = ''

i = len(string) - 1
while i >= 0:
    string_reversa += string[i]
    i -= 1

print(string_reversa)