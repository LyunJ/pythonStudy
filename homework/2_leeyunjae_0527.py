# 1
def formatting(string):
    return string.lower().strip('.?,')


with open('static_file/yesterday.txt', 'r') as f:
    lyrics_words = list(map(formatting, f.read().split()))
    word_dict = {key: 0 for key in set(lyrics_words)}
    for word in lyrics_words:
        word_dict[word] += 1
    for key, value in word_dict.items():
        print(key, ':', value)


# 2
def sum(file, path):
    wf = open(path, 'w')
    while True:
        line = file.readline()

        if line == '\n':
            continue
        elif line == '':
            break
        num1, num2 = map(int, line.split())

        wf.write(f'{num1}+{num2}={num1 + num2:.1f}\n')
    wf.close()


f = open('static_file/two_numbers.txt', 'r')
sum(f, 'static_file/two_numbers_result.txt')
f.close()

#3
def input_member(path):
    with open(path,'a',encoding='utf-8') as f:
        while True:
            mem_name = input('멤버를 입력하세요.(종료는 q) : ')
            if mem_name == 'q':
                print('저장이 완료되었습니다')
                break
            f.write(mem_name+'\n')


def output_member(path):
    with open(path,'r',encoding='utf-8') as f:
        print(f.read())


while True:
    select_num = input('저장 1, 출력 2, 종료 q : ')
    if select_num == '1':
        file_name = input('멤버 명단을 저장할 파일명을 입력하세요 : ')
        input_member('static_file/' + file_name)
    elif select_num == '2':
        file_name = input('멤버 명단이 저장된 파일명을 입력하세요 : ')
        output_member('static_file/' + file_name)
    else:
        break