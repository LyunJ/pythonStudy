name = ''


def inputName():
    global name
    name = input('이름입력 : ')


def getName():
    if name == '':
        return '무명씨'
    else:
        return name


def main():
    inputName()
    print(getName())


if __name__ == '__main__':
    main()
