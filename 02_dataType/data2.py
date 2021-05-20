# eval(expression) expression에 해당하는 식을 그대로 실행
num1 = eval(input('num1 : '))
num2 = eval(input('num2 : '))
print(type(num1),type(num2))
total = num1 + num2
print('total : {}'.format(total))

print(eval("abs(20)"))