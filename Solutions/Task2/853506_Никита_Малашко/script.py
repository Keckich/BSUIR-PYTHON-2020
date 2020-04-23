import random


def sort_file(filename):
    with open(filename, 'w') as file:
        file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(100))


def new_file(filename, n='', param='a'):
    with open(filename, param) as file:
        if type(n) is list:
            for i in range(len(n)):
                file.writelines('{}\n'.format(n[i]))



