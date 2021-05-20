# 1~20까지의 정수 중 3의 배수 출력

total = 0
for i in range(1,21):
    if i % 3 == 0:
        total += i
        print(i,end=' ')
print()
print('total:',total)