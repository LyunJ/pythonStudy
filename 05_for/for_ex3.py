# 정수 2개를 입력 받아서 두 수 사이의 합을 구하는 프로그램 작성

# num1, num2 = int(input('숫자1 입력 : ')), int(input('숫자2 입력 : '))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# total = 0
# for i in range(num1,num2+1):
#     total += i
# print('%d과 %d사이의 합은 %d' % (num1,num2,total))

# 단 수를 입력받아서 해당 구구단 출력
# num = int(input('단 수 입력 : '))
# for i in range(1,10):
#     print('%d * %d = %d' % (num,i,num*i))

# 카운트 다운 프로그램 작성
# num = int(input('시작 숫자를 입력하시오 : '))
#
# for i in range(num,-1,-1):
#     if i != 0 :
#         print(i,end=' ')
#     elif i == 0:
#         print('발사')
#     else:
#         pass

#숫자 10개를 입력받아서 양, 음, 0의 개수 출력

plus = 0
minus = 0
zero = 0

for i in range(10):
    num = int(input(f'숫자 {i+1}입력 : '))
    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    else:
        zero += 1
print('--------------------')
print(f'양의 개수 : {plus}')
print(f'음의 개수 : {minus}')
print(f'0의 개수 : {zero}')