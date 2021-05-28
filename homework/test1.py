# 1.lambda x,y:x**y
# 2.list(map(lambda value:value**2, ex))
# 3.3   패키지는 개별 .py파일의 집합이다
# 4.3   패키지에는 __init__.py파일이 필수이다
# 5.2   as 뒤에는 모듈 이름을 대신할 별명이 들어가야한다
# 6.import fah_converter as fah
# 7.from game.graphic.render import render_test
# 8.가)a나)write
# 9.가)w나)a다)r
# 10.from calculator import *
# 11.
# 7
# 3
# 2
# 1
# 1
# 1
# 종료되었습니다
print('7번')
try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")
# 12.5
print('12번')
sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break
# 13.4
# 14.2
# 15.4
# 16.숫자가 아닙니다
print('16번')
import random
answer = random.randint(1,10)
def guess_number(answer):
    try:
        guess = int(input("숫자를 넣어 주세요: "))
        if answer == guess:
            print("정답!")
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자가 아닙니다.")
guess_number(answer)
# 17.1)NameError2)IOError3)RuntimeError4)KeyError
# 18.Not divided by 0
# 1 3
# 2 1
print('18번')
for i in range(3):
    try:
        print(i, 3// i)
    except ZeroDivisionError:
        print("Not divided by 0")
# 19.
# with open('i_have_a_dream.txt','r') as f:
# 	contents = f.read()
# 	print(contents)
