# 파일 내에서 검색
# seek(offset, whence)
print('--------파일 내에서 검색 seek()----------')
f = open('file5.txt','r',encoding='utf-8')
f.seek(3,0)
lines = f.readlines()
print(lines)
f.close()