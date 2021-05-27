
# utf-8저장된 파일 읽어오기
f = open('file5.txt','r',encoding='utf-8')

line = f.readline()
print(line)

f.close()


#여러줄 읽기
f = open('file5.txt','r',encoding='utf-8')

while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')

f.close()

#파일 전체 읽기
f = open('file5.txt','r',encoding='utf-8')
lines = f.readlines()
print(''.join(lines))
f.close()