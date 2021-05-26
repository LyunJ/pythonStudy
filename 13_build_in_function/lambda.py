list1 = [1, 2, 3, 4]
list2 = [100, 20, 30, 40]

print(list(zip(*[iter(list2)] * 4)))
print(zip(list1, list2))
it = zip(list1, list2).__iter__()
print(next(it))
print(next(it))
print(next(it))


def hap(a, b):
    return [x + y for x, y in zip(a, b)]


print(hap(list1, list2))

print(list(map(lambda x, y: x + y, list1, list2)))
