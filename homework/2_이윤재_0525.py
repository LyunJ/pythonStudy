# 1
def print_coin():
    print('비트코인')


# 2
print_coin()
# 3
for _ in range(100):
    print_coin()


# 4
def print_coins():
    for _ in range(100):
        print_coin()


# 5
# 함수를 정의하기 전에 호출했기 때문

# 6
print('--------------------------')
print('6번')
print('--------------내 예측---------------\n'
      'A\nB\nC\nA\nB')
print('--------------결과--------------')


def message():
    print("A")
    print("B")


message()
print("C")
message()

# 7
print('--------------------------')
print('7번')
print('--------------내 예측---------------\n'
      'A\nA\nC\nB')

print('--------------결과--------------')
print("A")


def message():
    print("B")


print("A")
print("C")
message()

# 8
print('--------------------------')
print('8번')
print('--------------내 예측---------------\n'
      'A\nC\nB\nE\nD')

print('--------------결과--------------')
print("A")


def messages1():
    print("B")


print("C")


def messages2():
    print("D")


# message1() 정의되지 않은 함수 이름 사용
messages1()
print("E")
# message2() 정의되지 않은 함수 이름 사용
messages2()

# 9
print('--------------------------')
print('9번')
print('--------------내 예측---------------\n'
      'B\nA')

print('--------------결과--------------')


# def message1() 함수 선언시 마지막에 붙는 개괄 문자인 : 를 사용하지 않음
def message1():
    print("A")


# def message2() 함수 선언시 마지막에 붙는 개괄 문자인 : 를 사용하지 않음
def message2():
    print("B")
    message1()


message2()

# 10번
print('--------------------------')
print('10번')
print('--------------내 예측---------------\n'
      'B\nC\nB\nC\nB\nC\nA')

print('--------------결과--------------')


# def message1() 함수 선언시 마지막에 붙는 개괄 문자인 : 를 사용하지 않음
def message1():
    print("A")


# def message2() 함수 선언시 마지막에 붙는 개괄 문자인 : 를 사용하지 않음
def message2():
    print("B")


# def message3() 함수 선언시 마지막에 붙는 개괄 문자인 : 를 사용하지 않음
def message3():
    for i in range(3):
        message2()
        print("C")
    message1()


message3()

# 11
print('--------------------------')
print('11번')


def question_11():
    a, b = int(input('a : ')), int(input('b : '))
    return a * b


print(question_11())

# 12
print('--------------------------')
print('12번')


def question_12(ticker):
    return ticker.upper()


print(question_12('ticker'))

# 13
print('--------------------------')
print('13번')


def pickup_even(input_list):
    return [x for x in input_list if x % 2 == 0]


print(pickup_even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


def sootja():
    e = []
    while 1:
        n = input('숫자를 입력하세요.(엔터키 누르면 종료) : ')
        if n == '':  # 엔터키 누르면 종료하게 하는것
            break
        else:
            e.append(int(n))
    return e


def pickup_even():
    e = sootja()
    f = []
    for i in e:
        if i % 2 == 0:
            f.append(i)
        else:
            continue
    return f


print(pickup_even())
