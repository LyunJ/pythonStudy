# 산술연산자 : +, -, *, /, //, %, **

# 10000초는 몇 시간 몇 분 몇 초인가
s = 10000
h = s // 3600
m = s % 3600 // 60



# 산술 연산자 우선순위:(),**,(*,/,%,//),(+,-)

# 할당연산자 : =
# 대입연산자 : +=, -=, *=, /=, //=, %=, **=

a = 100
a = a + 10


# # 관계연산자 : >, <, <=, >=, ==, !=
# a=100
# b=1001
# print(a>b)
#
# # 논리연산자 : and, or, not
#
# print(a>b and b==1001)
# print(a>b or b==1001)
# print(not(a>b))
#
# # 비트연산자 : &(논리곱), |(or), ^(xor), ~(not), <<, >>
# print(10&3)
# print(10|3)
# print(10^3)
# print(~3)
# print(~3+1)
#
# print(10<<1)
# print(10<<2)
# print(10<<3)
#
# print(10>>1)
# print(10>>2)
# print(10>>3)

# 현금이 50000원이 있고, 사탕 가격이 120원 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가
cash = 5000
candy_price = 120
candy_amount = cash // candy_price
change = cash % candy_price

print("살 수 있는 사탕 개수 : {0:d}개\n거스름돈 : {1:d}원".format(candy_amount,change))