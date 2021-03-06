# Zadanie
# https://pl.spoj.com/problems/RNR_01_09/
# Opis rozwiązania
# http://aroundpython.com/index.php/2019/03/18/git/
import sys


class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []

g_branch = None
g_parent = None
g_valid = True
g_result = 'TAK\n'
root = Branch('root')


def search(branch, name):
    for child in branch.children:
        if child.name == name:
            global g_branch
            global g_parent
            g_branch = child
            g_parent = branch
            return
        else:
            search(child, name)


def search_in_new(branch, branch_list):
    for child in branch.children:
        for i in range(0, len(branch_list)):
            if branch_list[i] == child.name:
                branch_list.pop(i)
                break

        search_in_new(child, branch_list)


def search_in_old(branch, branch_list):
    for child in branch.children:
        try:
            branch_list.remove(child.name)
        except ValueError:
            return

        search_in_old(child, branch_list)


def test_names(branch, branch_list):
    if branch.name in branch_list:
        global g_valid
        g_valid = False
        return

    for child in branch.children:
        test_names(child, branch_list)


def generate_connections(branch):
    global g_result
    for child in branch.children:
        generate_connections(child)
        new_pair = ('{} {}\n').format(branch.name, child.name)
        g_result += new_pair


branches_quantity = int(sys.stdin.readline())

i = 0
while i < branches_quantity:
    params = sys.stdin.readline().split()
    i += 1

    children_quantity = int(params[1])
    if children_quantity == 0:
        continue

    name = params[0]
    params.pop(0)
    params.pop(0)

    search(root, name)

    if g_branch is None:
        g_branch = Branch(name)
        children_to_remove = []

        for child in root.children:
            for j in range(0, len(params)):
                if params[j] == child.name:
                    params.pop(j)
                    children_to_remove.append(child)
                    g_branch.children.append(child)
                    break

        for child in children_to_remove:
            root.children.remove(child)
                
        for child in g_branch.children:
            search_in_new(child, params)

        if params:
            for child in root.children:
                test_names(child, params)

            if g_valid:
                for new_branch_name in params:
                    new_branch = Branch(new_branch_name)
                    g_branch.children.append(new_branch)

                root.children.append(g_branch)
                g_branch = None
            else:
                break

    else:
        g_parent.children.remove(g_branch)
        children_to_remove = []

        for child in g_parent.children:
            for j in range(0, len(params)):
                if params[j] == child.name:
                    params.pop(j)
                    children_to_remove.append(child)
                    g_branch.children.append(child)
                    break

        for child in children_to_remove:
            g_parent.children.remove(child)

        for child in g_branch.children:
            search_in_old(child, params)

        if params:
            g_valid = False
            break

        g_parent.children.append(g_branch)
        g_branch = None

if g_valid and len(root.children) == 1:
    generate_connections(root.children[0])
    sys.stdout.write(g_result)
else:
    sys.stdout.write('NIE')