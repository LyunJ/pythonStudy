value = input('검색 값 입력:')
f = open('file5.txt','r',encoding='utf-8')
data = f.read()
print(data)
for ch in data:
    print(ch,end='')
f.close()