
# remove(x) : 가장 첫번째 만나는 값을 삭제

n = [1,2,3,4,5,6,7,1]
n.remove(1)
print(n)
cnt = n.count(1)
print(cnt)

# pop() : 마지막 값을 꺼내서 반환함 pop(index) : index 위치의 값을 꺼내서 반환
data = n.pop()
print(n)
print(data)

data = n.pop(0)
print(data)