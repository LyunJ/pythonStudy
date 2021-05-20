# 타입 변환

# print('나는 현재 나이가 ' + str(23) + '살입니다')
#
# num = input('숫자를 입력하세요 : ')
# print(type(num))
# print(int(num) + 100)

# print(int('123',8)) # 8진수0o123
# print(int('123',16)) # 16진수 0x123
# print(int('1011',2)) # 2진수 0b1011

#float(문자열) : 문자열을 실수로 변환
# 0x 0b 0o 는 문자열로 넣을 수 없다
# 즉 10진수 문자열만 넣을 수 있다
# print(float(num) + 100)
# print(float('123'))

# 키보드로부터 두 개의 숫자를 입력을 받고 두 수의 합과 평균을 구한 후 출력하시오
num1 , num2 = input('num1 : '), input('num2 : ')

total = int(num1) + int(num2)
avg = total/2

print('total : %d, avg : %.2f' % (total,avg))
print('total : {0}, avg : {1}'.format(total,avg)) # {순서}

# print(format(total,'10.2f'))
print('total : {0:d}, avg : {1:5.2f}'.format(total,avg)) # 서식 지정
print('total :',format(total,'d'),', avg :',format(avg,',.2f'))
