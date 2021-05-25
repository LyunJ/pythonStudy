# def get_triangle_area():
#     width, height = int(input('밑변 : ')), int(input('높이 : '))
#     return width * height / 2
#
#
# print(get_triangle_area())

# def order():
#     price, num = int(input('상품 가격 입력 : ')), int(input('주문 수량 입력 : '))
#     return price,num
#
# price,num = order()
# print('------------------')
# print(f'상품가격 : {price}원\n'
#       f'주문수량 : {num}개\n'
#       f'주문액 : {price*num}원')

# def getName():
#     dic = dict()
#     name, age = input('이름 : '), int(input('나이 : '))
#     dic['name'] = name
#     dic['age'] = age
#     return dic
#
#
# print(getName())

# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# def mul(x, y):
#     return x * y
#
#
# def div(x, y):
#     return x / y
#
#
# x, y = int(input('x : ')), int(input('y : '))
# print(f'{x} + {y} = {add(x, y)}\n'
#       f'{x} - {y} = {sub(x, y)}\n'
#       f'{x} * {y} = {mul(x, y)}\n'
#       f'{x} / {y} = {div(x, y):.1f}')


def order():
    price, num = int(input('상품 가격 입력 : ')), int(input('주문 수량 입력 : '))
    result = {
        'total': price * num,
        'pay': price * num - cal_discount(price * num),
        'discount': cal_discount(price * num)
    }
    return result


def cal_discount(total_price):
    if total_price >= get_discount_base_amount(0):
        result = get_discount(total_price, get_discount_ratio(0))
    elif total_price >= get_discount_base_amount(1):
        result = get_discount(total_price, get_discount_ratio(1))
    else:
        result = get_discount(total_price, 0)

    return result


discountStandard = [
    {
        'discount_base_amount': 100000,
        'discount_ratio': 0.1
    },
    {
        'discount_base_amount': 50000,
        'discount_ratio': 0.05
    }
]


def get_discount_base_amount(index):
    return discountStandard[index]['discount_base_amount']


def get_discount_ratio(index):
    return discountStandard[index]['discount_ratio']


def get_discount(total_price, discount_ratio):
    result = total_price * discount_ratio
    return result


price_info = order()
print('------------------')
print(f'주문액 : {price_info["total"]}원\n'
      f'할인액 : {price_info["discount"]}원\n'
      f'지불액 : {price_info["pay"]}원')
