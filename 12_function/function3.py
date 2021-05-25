# 가변길이 매개변수
# *args : arguments 1개 이상 지정
# **kwargs : keyword arguments key=value

def mySum(*args):
    total = 0
    for x in args:
        total += x
    return total


def myShowInfo(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print()
    for value in kwargs.values():
        print(value, end=' ')
    print()
    for item in kwargs.items():
        print(item)


print(mySum(1, 2, 3, 4))  # 10
# print(mySum([1, 2, 3, 4]))  # error

myShowInfo(id=123,name='kim',add='Seoul')
# myShowInfo({'id':123,'name':'kim','add':'Seoul'}) # error

