import itertools
import json
import sys


def read_file(name_file):
    with open(name_file, encoding='utf-8') as file:
        return file.read()


users = [el.replace(',', ' ') for el in read_file('users.csv').splitlines()]
hobby = read_file('hobby.csv').split(',')
content = dict(itertools.zip_longest(users, hobby))
if len(hobby) > len(users):
    sys.exit(1)
else:
    content = json.dumps(content, ensure_ascii=False, indent=2)
    with open('users_hobby.txt', 'w', encoding='utf-8') as f:
        f.write(content)
