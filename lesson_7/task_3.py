import os
from shutil import copytree


def copy_files(route, folder):
    final_path = os.path.join('my_project\\templates\\', folder)
    try:
        copytree(route, final_path)
    except FileExistsError:
        print(f'Шаблон {folder} уже существует')


def search_templates():
    for i in os.walk('my_project'):
        if '.html' in ''.join(i[-1]) and 'my_project\\templates\\' not in i[0]:
            sl = i[0].rfind('\\')
            route = i[0][:sl]
            folder = i[0][sl+1:]
            copy_files(route, folder)


if not os.path.exists('my_project'):
    print('Сначала запустить task_1_2.py, а то ничего работать не будет =)')
else:
    search_templates()
