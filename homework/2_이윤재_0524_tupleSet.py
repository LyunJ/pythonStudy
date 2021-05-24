# 1
my_variable = tuple()
# 2
# 튜플은 요소의 변경이 불가능하다

# 3
my_variable = tuple([1])
print(my_variable)

# 4
# tuple

# 5
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
print(t)

# 6
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)

# 7
interest = tuple(interest)

# 8
partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}

print(partyA.union(partyB))
print(partyA.intersection(partyB))
print(partyA.difference(partyB))
print(partyB.difference(partyA))
