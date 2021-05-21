crawling = 'Data crawling is fun'
# print(crawling.find('i'))
# print(crawling.rfind('i'))
# print(crawling.find('i',1,9))
#
# print('------------')
# print(crawling.index('i'))
# print(crawling.rindex('i'))
# print(crawling.index('i',1,9))

# split() : 지정된 문자로 문자열을 분할하여 리스트로 반환

token = crawling.split()
print(token)

names = 'Lee,Kim,Choi,Kang'
nameL = names.split(',')
for n in nameL:
    print(n)