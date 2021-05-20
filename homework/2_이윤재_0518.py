# 1. 16진수 구분 코드 작성
hex_num = input('16진수 한 글자 입력 : ')
if hex_num < '0' or hex_num > 'F':
    print('16진수가 아닙니다')
else:
    print('10진수 ==> %d' % int('0x'+hex_num,16))

print('============================')
# 2. 잔돈 교환 프로그래밍
cash = int(input('교환할 돈은 얼마? '))
ohman = cash // 50000
cash %= 50000
man = cash // 10000
cash %= 10000
ohchun = cash // 5000
cash %= 5000
chun = cash // 1000
cash %= 1000
ohback = cash // 500
cash %= 500
back = cash // 100
cash %= 100
ohship = cash // 50
cash %= 50
ship = cash // 10
cash %= 10
print(' 50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장\n 500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개'
      % (ohman,man,ohchun,chun,ohback,back,ohship,ship))
print(' 바꾸지 못한 돈 ==> %d' % cash)

print('============================')
#3. 주사위 게임
import random as rd
anum = rd.randint(1,6)
bnum = rd.randint(1,6)

print('A의 주사위 숫자는 %d입니다'%anum)
print('B의 주사위 숫자는 %d입니다'%bnum)

if anum == bnum:
    print('비겼습니다')
elif anum > bnum :
    print('A가 이겼다')
else:
    print('B가 이겼다')


print('============================')