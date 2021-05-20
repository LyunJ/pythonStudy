# 첫번째 프로그램

# print('Lee YunJae')
'''
# 변수에 값을 저장
x = 10
y = 20
z = 30
print(x,y,z)

# 여러개의 변수에 여러개의 값을 저장
x, y, z = 10, 20, 30
print(x,y,z)

# 여러개의 변수에 동일한 값을 할당
a = b = c = 100
print(a,b,c)



# 두 변수의 값을 교환
a, b = 10, 20
print('a=',a)
print('b=',b)
a,b = b,a
print('a=',a)
print('b=',b)


# 변수를 삭제
x = 100
print(x)
print(id(x))
print(type(x))
del x


# 문자열에 큰 따옴표 사용
name = "이윤재"
age = 24

print(name,age)
address = "서울시"
print(name+'는 '+address+'에 삽니다')
# str() : 숫자형을 문자열로 변환
print(name+'는 '+str(age)+'살입니다')
print(name+'은 ',age,'살입니다')


# 사각형의 면적을 구하는 프로그램
width = 100
height = 50
area = width * height
print(area)

name = "홍길동"
no = "2016001"
year = 4
grade = 'A'
average = 93.5

# print('성명 : ' + name)
# print('학번 : ' + no)
# print('학년 :',year)
# print('학점 : ' + grade)
# print('평균 :',average)

# print('성명 : %s' % name)
# print('학번 : %s' % no)
# print('학년 : %d' % year)
# print('학점 : %c' % grade)
# print('평균 : %0.2f' % average)
#
# print('성명 : %s, 학번 : %s' %(name,no))
#
# rate = 80
# print('이름 : %s, 출석률: %d%%' %(name,rate))

print(format(average,'10.2f'))


INT_Rate = 0.03
deposit = 10000
interest = deposit * INT_Rate
balance = deposit + interest

print(balance)
print(int(balance))

print(format(int(balance),','))


a = 0b1010
b = 300
c = 0o123
d = 0x12fc
print(a,b,c,d)

f1 = 3.14

str = """여러줄로
나누어
출력가능"""

print(str)

# 특수 리터럴
# None
address = None
print(address)

a = 1+2+3+\
    4+5+6
print(a)

print("c:\python\name")
print(r"c:\python\name")
'''

print("first")
print("second")

print("first",end="@")
print("second")

print("%f" % (10/4))
print("%d / %d = %5.1f"  % (10, 4, 10 / 4))
print("%d / %d = %5.0f"  % (10, 4, 10 / 4))
print("%1.1f" % 123.45)