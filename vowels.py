n = input()
vowels = ['a', 'e', 'i', 'o', 'u']

for i in n:
    if i.lower() in vowels:
        print(i+i, end='')
    else:
        print(i, end='')