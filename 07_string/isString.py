# 문자열의 구성요소 판단
# isalpha() : 문자여부 True False
# isdigit() : 숫자여부
# isspace() : 공백여부
# isalnum() : 문자,숫자여부
text = '1234'
print(text.isdigit())
print(text.isalpha())
print('   '.isspace())
print(' ss'.isspace())
print('hi2'.isalnum())
print('hi'.isalnum())
print('2'.isalnum())
print('hi'.isalpha())
print('abc'.islower())
print('ABC'.isupper())

print('안녕'.isalpha())

# 연습문제. 문장을 입력하여 알파벳, 숫자, 스페이스, 그외문자의 개수를 계산 출력
string = input('문장을 입력해 주세요')

alpha = 0
num = 0
space = 0
other = 0

for s in string:
    if s.isalpha():
        alpha += 1
    elif s.isdigit():
        num += 1
    elif s.isspace():
        space += 1
    else:
        other += 1

print(f'문자 개수 : {alpha} || 숫자 개수 {num} || 공백 개수 {space} || 그 외 문자 개수 : {other}')