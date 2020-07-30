
def Add(a):
    sum = 0
    for z in a:
        sum += z
    return sum

a = [120, 55, 55, 8, 4, 65, 9, 4, 65]
print Add(a)
b = [120, 55, 55, 8, 4, 65, 9, 4, 65, 55, 8, 4, 65]
print Add(b)