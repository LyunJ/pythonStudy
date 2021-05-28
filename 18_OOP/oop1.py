# class Car:
#     def __init__(self, speed=0, color='white'):
#         self.speed = speed
#         self.__color = color  # private field
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self,color):
#         self.__color = color
#
#     def show_info(self):
#         self.__show_color()
#         print('car color : %s\n speed : %d' % (self.__color,self.speed))
#
#     def __show_color(self): # private method
#         print('car color: %s'%self.__color)
#
#
#
# car1 = Car()
# print(car1.get_color())
# car1.show_info()

# class Dog:
#     def __init__(self, breed, size, age, color):
#         self.__breed = breed
#         self.__size = size
#         self.__age = age
#         self.__color = color
#
#     def eat(self, food):
#         print(f'{self.__breed}가 {food}를 먹는다')
#
#     def sleep(self):
#         print(f'{self.__breed}가 잠들었다')
#
#     def play(self):
#         print(f'{self.__breed}가 놀고있다다')
#
#
# dog1 = Dog('Neapolitan Mastiff','Large',5,'Black')
# dog2 = Dog('Maltese','Small',2,'White')
# dog3 = Dog('Chow Chow','Medium',3,'Brown')
# dog1.eat('개밥')
# dog2.sleep()
# dog3.play()

# class Line:
#     def __init__(self, length=0):
#         self.length = length
#         print('%s 길이의 선이 생성' % self.length)
#
#     def __del__(self):
#         print('%s 길이의 선이 소멸' % self.length)
#
#     def __repr__(self):
#         return '선의 길이 : ' + str(self.length)
#
#     def __add__(self, other):
#         return self.length + other.length
#
#     def __eq__(self, other):
#         return self.length == other.length
#
#     def __ne__(self, other):
#         return self.length != other.length
#
#     def __lt__(self, other):
#         return self.length < other.length
#
#
#
#
# line1 = Line()
# line2 = Line()
# print(line1)
# print('두 선의 길이의 합:', line1 + line2)
# if line1 < line2:
#     print('선 2가 더 크네요')
# elif line1 == line2:
#     print('길이가 같아요')
# else:
#     print('몰라요')

# class Car:
#     def __init__(self, speed=0, color='white'):
#         self.speed = speed
#         self.__color = color  # private field
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, color):
#         self.__color = color
#
#     def show_info(self):
#         self.__show_color()
#         print('car color : %s\n speed : %d' % (self.__color, self.speed))
#
#     def __show_color(self):  # private method
#         print('car color: %s' % self.__color)
#
#
# class Truck(Car):
#     def __init__(self, speed, color, load):
#         super().__init__(speed, color)
#         self.load = load
#
#     def show_load(self):
#         print(self.load)
#
# car1 = Car()
# car2 = Truck(0,'Blue',1000)
#
# car1.show_info()
# car2.show_info()

# class Dog:
#     def __init__(self, breed, size, age, color):
#         self.__breed = breed
#         self.__size = size
#         self.__age = age
#         self.__color = color
#
#     def __str__(self):
#         return f'Breed : {self.__breed}\n' \
#                f'Size : {self.__size}\n' \
#                f'Age : {self.__age}\n' \
#                f'Color : {self.__color}'
#
#     def __lt__(self, other):
#         return self.__age < other.__age
#
#     def __eq__(self, other):
#         return self.__age == other.__age
#
#     def eat(self, food):
#         print(f'{self.__breed}가 {food}를 먹는다')
#
#     def sleep(self):
#         print(f'{self.__breed}가 잠들었다')
#
#     def play(self):
#         print(f'{self.__breed}가 놀고있다다')
#
# dog1 = Dog('Neapolitan Mastiff','Large',5,'Black')
# dog2 = Dog('Maltese','Small',2,'White')
# print(dog1)
# if dog1 > dog2:
#     print('1번 개가 나이가 더 많음')
# elif dog1 == dog2:
#     print('나이가 같음')
# else:
#     print('2번개가 나이가 더 많음')

# class Person:
#     def __init__(self, age, sex, name):
#         self.__age = age
#         self.__name = name
#         self.__sex = sex
#
#     def greeting(self):
#         print('안녕하세요')
#
#     def get_name(self):
#         return self.__name
#
#
# class Student(Person):
#     def __init__(self, age, sex, name, school, department, student_num):
#         super().__init__(age, sex, name)
#         self.__school = school
#         self.__department = department
#         self.__student_num = student_num
#
#     def study(self):
#         print('studying')
#
#     def test(self):
#         print('시험 보는 중')
#
#     def greeting(self):
#         super().greeting()
#         print(f'{self.__school}에 다니는 {super().get_name()}입니다')
#
#
# student1 = Student(20, '남', '홍길동', '하버드', '컴퓨터공학과', '20200022')
# student1.greeting()

