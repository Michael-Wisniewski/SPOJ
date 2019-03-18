# Zadanie
# https://pl.spoj.com/problems/RNR_01_09/
# Opis rozwiązania
# http://aroundpython.com/index.php/2019/03/18/git/
import sys


class Branch:
    def __init__(self, name, length, branches):
        self.name = name
        self.length = length
        self.children_found = 0
        self.branches = branches
        self.next = None

answer = 'TAK\n'
root = Branch(None, 0, '')
root.next = Branch(None, 0, '')
filled_branches = 0
branches_quantity = int(sys.stdin.readline())

i = 0
while i < branches_quantity:
    i += 1
    params = sys.stdin.readline().split(' ', 2)
    params[1] = int(params[1])

    if params[1] == 0:
        continue

    params[2] = set((params[2][:-1]).split())
    filled_branches += 1
    branch = Branch(*params)
    previous = root
    pointer = root.next

    while branch.length < pointer.length:
        previous = pointer
        pointer = pointer.next

    previous.next = branch
    branch.next = pointer

pointer = root.next.next
i = 1
while i < filled_branches:
    i += 1
    compared_prev = root
    compared = root.next

    while pointer.name not in compared.branches:
        compared_prev = compared
        compared = compared.next

        if compared is pointer:
            sys.stdout.write('NIE\n')
            sys.exit(0)

    compared.branches -= pointer.branches
    compared.children_found += 1
    new_length = len(compared.branches)

    if compared.length != pointer.length + new_length:
        sys.stdout.write('NIE\n')
        sys.exit(0)
    elif new_length == compared.children_found:
        for branch in compared.branches:
            answer += ('{} {}\n').format(compared.name, branch)
        compared_prev.next = compared.next
    else:
        compared.length = new_length

    pointer = pointer.next

pointer = root.next
while pointer.name is not None:
    for branch in pointer.branches:
        answer += ('{} {}\n').format(pointer.name, branch)
    pointer = pointer.next

sys.stdout.write(answer)
