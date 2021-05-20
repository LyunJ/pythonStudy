# len()
string = 'Python Programming'
n = len(string)
print(n)

# count()
print(string.count('m'))

# find() : 특정 문자열이 존재여부에 따라 위치 인덱스 출력 없으면 -1 출력
print(string.find('ing'))
print(string.find('ong'))

# index() : find와 같지만 못찾으면 오류가 발생함
print(string.index('ing'))
print(string.index('ong'))
