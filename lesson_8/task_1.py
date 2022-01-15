import re


def email_parse(email_address):
    pattern = r'^([^@|\.]+)@(\w+\.\w+)$'
    result = re.findall(pattern, email_address)
    if not result:
        raise ValueError
    else:
        return {'username': result[0][0], 'domain': result[0][1]}


print(email_parse('-text123_@mail.ru'))
