students = [
    {'name': '홍길동', 'korean': 87, 'math': 98, 'english': 88, 'science': 95},
    {'name': '이몽룡', 'korean': 92, 'math': 98, 'english': 96, 'science': 98},
    {'name': '성춘향', 'korean': 76, 'math': 96, 'english': 94, 'science': 90},
    {'name': '변학도', 'korean': 98, 'math': 92, 'english': 96, 'science': 92},
    {'name': '박지성', 'korean': 95, 'math': 98, 'english': 98, 'science': 98},
    {'name': '류현진', 'korean': 64, 'math': 88, 'english': 92, 'science': 92},
]

print('이름\t\t총점\t평균')
for student in students:
    total = sum(list(student.values())[1:5])
    print(f'{student["name"]}\t{total}\t{total/4:.2f}')

# 2
words = dict()

while True:
    word = input('영어 단어 등록(종료는 quit) : ')
    if word == 'quit':
        break
    if word in words.keys():
        print(f'{word}는 이미 등록된 단어 입니다')
        print()
        continue
    mean = input(f'{word}의 뜻 입력(종료는 quit) : ')
    if mean == 'quit':
        break

    words[word] = mean
    print()

print()

while True:
    search_word = input('검색할 단어 입력(종료는 quit) : ')
    if search_word.strip() == 'quit':
        print('종료합니다')
        break
    if search_word in words.keys():
        print(f'{search_word}의 뜻은 {words.get(search_word)}입니다')
    else:
        print(f'{search_word}는 사전에 없는 단어 입니다')

    print()