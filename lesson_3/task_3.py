def thesaurus(*args):
    names = {}
    for arg in sorted(args):    # результат получится отсортированным
        if arg[0] not in names:
            names[arg[0]] = [arg]
        else:
            names[arg[0]].append(arg)
    return names


print(thesaurus('Ярослав', 'Пётр', 'Андрей', 'Антон', 'Александр', 'Иван', 'Илья'))
