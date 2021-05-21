#4
student_num = int(input('학생 수 입력 : '))
student_score_list = list()
more_than_80 = 0
for i in range(student_num):
    score = int(input(f'학생{i} 점수 입력 : '))
    if score >= 80:
        more_than_80 += 1
    student_score_list.append(score)

print(f'총첨 : {sum(student_score_list)}')
print(f'평균 : {sum(student_score_list)/len(student_score_list):.2f}')
print(f'80점 이상 학생 : {more_than_80}명')
print(f'점수 내림차순 정렬 : {sorted(student_score_list,reverse=True)}')

#5
proverb = ['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
proverb_mean = ['잘못을 고치고 옮은 길에 들어섬',
                '죽일 고비를 여러번 겪으며 살아나다',
                '평범한 사람 가운데 뛰어난 사람',
                '아무짝에나 쓸모 없는 것',
                '고통과 즐거움을 함께 한다',
                '미리 준비해두면 근심 걱정이 없다',
                '사회적으로 인정받고 출세하여 이름을 세상에 드날림',
                '다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
                '생사를 같이 할 수 있는 친밀한 벗',
                '상대 없이 혼자서는 어떤 일을 이룰 수 없다']

print("사자성어 맞추기 게임을 시작합니다\n"
      "----------------------------")

import random as rd

while True:
    proverb_num = rd.randint(0,len(proverb))

    print(proverb_mean[proverb_num])
    answer = input('이 말의 사자성어는? : ')

    if answer in proverb:
        print('맞습니다.. 게임을 종료합니다')
        break
    else:
        print('틀렸습니다... 다시 도전!')
