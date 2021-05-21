# x.join(str) str사이사이에  x를 삽입한 결과를 반환 str이 한글자면 str 그대로 반환
a = 'aa'
a = a.join('bbb')
print(a)

b = '-'
print(b.join('1'))

numbers = ['10','20','30','40','50']
print(''.join(numbers))