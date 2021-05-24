# 딕셔너리 dictionary

d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
print(type(d))
print(d[1])

d2 = {'name': 'Lee', 'tel': '010010010'}
print(d2['name'])

d3 = {
    'name': 'daum',
    'url': 'www.daum.net',
    'userid': 'dm',
    'pw': 1234
}

# keys(), values(), items()
print(type(d3.keys()))
print(d3.keys())
# dict_keys 타입이기 때문에 요소에 접근하려면 먼저 리스트로 변환한다
print(list(d3.keys())[1])

print(type(d3.values()))
print(d3.values())
# dict_values 타입이기 때문에 요소에 접근하려면 먼저 리스트로 변환한다
print(list(d3.values())[0])

print(type(d3.items()))
print(d3.items())
# 튜플의 리스트 형식
print(list(d3.items()))

for key in d3.keys():
    print(key)
print(d3.get('url'))
# 없는 키값일경우 None을 반환함
print(d3.get('add'))
print(d3.get('add', 'not exist'))  # 오류 메시지 지정 가능

k = 'link'

if d3.get(k) is None:
    print(k + '에 대한 데이터가 없음')
# in / not in
print('link' in d3)
print('link' not in d3)
print('name' in d3)

print(d3.popitem())

# zip()
# 튜플로 묶어줌
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
for pair in zip(numbers, letters):
    print(pair)
# zip을 사용한 병렬처리
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
