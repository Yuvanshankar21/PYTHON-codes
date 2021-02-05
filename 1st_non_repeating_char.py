def character(str1):
    for i in range(0, len(str1)):
        a = []
        a[:] = str1
        a.remove(a[i])
        if str1[i] not in a:
            return str1[i]


print(character(input()))
