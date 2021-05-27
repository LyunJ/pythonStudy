
# 여러줄의 데이터 쓰기
f = open('file4.csv','w',encoding='utf-8')

for i in range(1,11):
    data = '%d행' % i
    f.write(data)

f.close()