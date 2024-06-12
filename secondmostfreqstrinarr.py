def method1(array):
    dicti = {}
    for name in array:
        if name in dicti:
            dicti[name] += 1
        else:
            dicti[name] = 1
    max = 0
    smax = 0
    s1 = ""
    s2 = ""
    for key, value in dicti.items():
        if value > max:
            smax = max
            s2 = s1
            max = value
            s1 = key
        elif value > smax:
            smax = value
            s2 = key
    return s2


arr = ['kavi', 'amr', 'amr','amr','amr', 'kav', 'kav', 'kav']
print(method1(arr))
