"""
TO DO List application  (template version)
(c) Alexandr K
"""

# VARIABLES DEFINE
HELP = """
    help - напечатать справку
    add - добавить задачу
    print - распечатать все задачи
    exit - выход из программы
    """
tasks = []

# WELCOME HEADER
print('=' * 38)
print('Добро пожаловать в программу TODO List ! ')
print('Справка по комманде: help')
print('=' * 38 + '\n')

# MAIN CODE:
while True:
    command = input('Введите команду: ')
    if command == 'exit':
        print('Благодарим за использование! До свидания !')
        break;
    elif command == 'help':
        print('список доступных комманд: '  + HELP)
    elif command == 'add':
        task = input('Введите задачу: ')
        tasks.append(task)
    elif command == 'print':
        print('\n')
        print(tasks)
    else:
        print('Введенная команда неизвестна...')

# по уму нужно еще добавить сюда возможность записи\вывода задач на\из файл(а)...
# или запись в DataBase