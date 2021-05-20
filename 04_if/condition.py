#키보드로 입력받은 정수가 짝수인지 홀수인지?

# number = int(input('정수를 입력해 주세요 : '))
# if(number % 2 == 0):
#     print('짝수')
# else:
#     print('홀수')
#
# password="1234"
# if password == "1234":
#     print('correct password')
# else:
#     pass

# auth_id = 'flower'
# auth_password = '1234'
#
# input_id = input('아이디 입력 : ')
# input_password = input('비밀번호 입력 : ')
#
# if(input_id == auth_id and input_password == auth_password):
#     print('로그인 성공!')
# else:
#     print('로그인 실패!')
#
# elif
# number = int(input('정수 입력 : '))
# if number > 0:
#     print('양수')
# elif number < 0 :
#     print('음수')
# else:
#     print('0')

a = int(input('정수1 입력 : '))
b = int(input('정수2 입력 : '))
c = int(input('정수3 입력 : '))

if(a>b and a>c):
    max_num = a
elif(b>c):
    max_num = b
else:
    max_num = c

print('max_num : %d' % max_num)

# max_num = a
# if b > max_num:
#     b = max_num
# if c > max_num:
#     c = max_num
