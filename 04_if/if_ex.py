# 도형을 선택해서 면적 구하기
# 1 : 사각형, 2 : 삼각형, 3 : 원

shape_num = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))

if(shape_num == 1):
    width = int(input('너비 : '))
    height = int(input('높이 : '))
    area = width*height
    print('넓이 : %d' % area)
elif(shape_num == 2):
    width = int(input('밑변 : '))
    height = int(input('높이 : '))
    area = width*height/2
    print('넓이 : %.2f' % area)
else:
    radius = int(input('반지름 : '))
    area = radius*radius*3.14
    print('넓이 : %.2f' % area)
