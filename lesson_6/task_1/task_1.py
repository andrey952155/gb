def parsed_line(line):
    line = line.split(' ')
    return line[0], line[5][1:], line[6]


def get_line_file():
    result = []
    with open('nginx_logs.txt') as file:
        while True:
            line = file.readline()
            if line:
                result.append(parsed_line(line))
            else:
                break
        return result


print(get_line_file())

