f = open("txtfile.txt",'w')

f.close()

# 디렉토리 경로 설정 시 오류 \ 사용 => \\ 또는 /
# f = open ('C:\Users\tedle\work\study\python\16_fileIO\txtfile.txt','w') # 에러발생
# f.close()
f = open ('C:\\Users\\tedle\\work\\study\\python\\16_fileIO\\txtfile.txt','w')
f.close()
f = open ('C:/Users/tedle/work/study/python/16_fileIO/txtfile.txt','w')
f.close()

# 상대경로
f = open("./txtfile.txt",'w')
f.close()