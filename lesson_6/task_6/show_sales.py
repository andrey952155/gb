import sys


def print_result(line, count):
    if len(sys.argv) == 1:
        print(line)
    elif len(sys.argv) == 2 and count >= int(sys.argv[1]):
        print(line)
    elif len(sys.argv) == 3 and int(sys.argv[1]) <= count <= int(sys.argv[2]):
        print(line)
        if count == int(sys.argv[2]):   # вернем True чтобы остановить чтение строк
            return True


def read_file():
    count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line:
                count += 1
                if print_result(line[:-1], count):  # убрал перенос строки
                    break
            else:
                break


read_file()
