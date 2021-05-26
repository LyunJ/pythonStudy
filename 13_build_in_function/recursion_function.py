def count(num):
    print(num)
    if num == 0:
        return 0
    else:
        count(num-1)

count(49)