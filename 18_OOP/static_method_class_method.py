# 정적 메소드
class Calc:
    @staticmethod
    def add(a, b):
        return a + b


print(Calc().add(1, 2))

# 클래스 메소드
# self를 통하지 않고 바로 클래스가 메소드 호출
# 클래스 변수를 이용하는 메소드를 정의
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def show_count(cls):
        print('%d명 태어났습니다' % cls.count)


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
Person.show_count()