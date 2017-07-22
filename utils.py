"""Utility functions"""

import getpass


def ask_input(prompt = '', is_password = False):
    while True:
        answer = getpass.getpass() if is_password == True else input(prompt)
        if answer is not '':
            return answer


def ask_multiple_option(options, prefix = 'Choose between', prompt = ': '):
    def exists(index):
        return 0 <= index < len(options)

    # while answer == None or not exists(answer):
    while True:
        print(prefix)
        for index, option in enumerate(options):
            print('  {} - {}'.format(index + 1, option))
        answer = input(prompt).strip()
        if answer is not '':
            index = int(answer) - 1
            if exists(index):
                return options[index]
