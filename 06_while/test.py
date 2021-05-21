# 1-1
for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()
# 1-2
for i in range(0,5):
    for j in range(5-i):
        print(' ',end='')
    for k in range((i*2)+1):
        print('*',end='')
    print()
# 2
num = int(input('숫자 입력 : '))
while num != 7:
    num = int(input('다시 입력 : '))

# 3
cash = 10000
oneCoin = 2000
i = 0
while True:
    i += 1
    cash -= oneCoin
    if cash > 0:
        print(f'노래를 {i}곡 불렀습니다')
        print(f'현재 {cash}원 남았습니다')
    else:
        print('잔액이 없습니다. 종료합니다')
        break
