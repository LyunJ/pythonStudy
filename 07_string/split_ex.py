#
birthDay = input('생일 입력(연/월/일) : ')

[year,month,day] = birthDay.split('/')

print(f'당신은 {year}년에 태어나셨군요')
print(f'생일은 {month}월 {day}일 이네요')

# 주어진 데이터에서 점수만 추출하여 숫자화 하고 총점과 평균을 구하시오
data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
dataList = data.split(',')

total = 0
for dl in dataList:
    score = int(dl[4:6])
    total += score

avg = total / len(dataList)

print(f'total : {total}, average : {avg}')