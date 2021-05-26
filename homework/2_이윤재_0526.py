def answer_format(num, expect, result):
    print(f'----{num}.실행결과로 알맞은 것은-----')
    print('==예측')
    print(expect)
    print('==결과')
    result()


def one():
    mylist = ['apple', 'banana', 'grape']
    result = list(enumerate(mylist))
    print(result)


def two():
    cat_song = "my cat has blue eyes, my cat is cute"
    print({i: j for j, i in enumerate(cat_song.split())})


def three():
    colors = ['orange', 'pink', 'brown', 'black', 'white']
    result = '&'.join(colors)
    print(result)


def four():
    user_dict = {}
    user_list = ["students", "superuser", "professor", "employee"]
    for value_1, value_2 in enumerate(user_list):
        user_dict[value_2] = value_1
    print(user_dict)


def five_one():
    result = [i for i in range(10) if i % 2 == 0]
    print(result)


def five_two():
    result = [i for i in range(10)]
    print(result)


def five_three():
    items = 'zero one two three'.split()
    print(items)


def five_four():
    example = 'cs50.gachon.edu'
    subdomain, domain, tid = example.split('.')
    print(subdomain)


def six():
    animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
    print([ani for ani in animal if 'o' not in ani])


def seven():
    name = "Hanbit University"
    student = ["Hong", "Gil", "Dong"]
    split_name = name.split()
    join_student = ''.join(student)
    print(join_student[-4:] + split_name[1])


def eight():
    kor_score = [49, 79, 20, 100, 80]
    math_score = [43, 59, 85, 30, 90]
    eng_score = [49, 79, 48, 60, 100]
    midterm_score = [kor_score, math_score, eng_score]
    print(midterm_score[0][2])


def nine():
    a = [1, 2, 3]
    b = [4, 5, ]
    c = [7, 8, 9]
    print([[sum(k), len(k)] for k in zip(a, b, c)])


def ten():
    week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    list_data = [week, rainbow]
    print(list_data[1][2])


def eleven():
    kor_score = [30, 79, 20, 100, 80]
    math_score = [43, 59, 0, 30, 90]
    eng_score = [49, 72, 48, 67, 15]
    midterm_score = [kor_score, math_score, eng_score]
    print("score:", midterm_score[2][1])


def twelve():
    alist = ["a", "b", "c"]
    blist = ["1", "2", "3"]
    abcd = []
    for a, b in enumerate(zip(alist, blist)):
        try:
            abcd.append(b[a])
        except IndexError:
            abcd.append("error")
    print(abcd)


def fourteen():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
    nums = [i for i in range(20)]
    answer = [alpha + str(num) for alpha in alphabet for num in nums if num % 2 == 0]
    print(len(answer))


answer_format(1, "[(0, 'apple'), (1, 'banana'), (2, 'grape')]", one)
answer_format(2, "{'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}", two)
answer_format(3, "orange&pink&brown&black&white", three)
answer_format(4, "{'students':0,'superuser':1,'professor':2,'employee':3}", four)
answer_format('5-1', "[0,2,4,6,8]", five_one)
answer_format('5-2', "[0,1,2,3,4,5,6,7,8,9]", five_two)
answer_format("5-3", "['zero','one','two','three]", five_three)
answer_format('5-4', "cs50", five_four)
answer_format(6, "['Cat','Panda','Owl']", six)
answer_format(7, "DongUniversity", seven)
answer_format(8, 20, eight)
answer_format(9, "[[12, 3], [15, 3]]", nine)
answer_format(10, "yellow", ten)
answer_format(11, "score: 72", eleven)
answer_format(12, "['a','2','error']", twelve)

# 13
print(f'----13.들어갈 코드로 알맞은 것은-----')
print('==예측')
print("zip")
print('==결과')
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

answer_format(14, 80, fourteen)

list
