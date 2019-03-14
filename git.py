class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(name)

    def delete_child(self, name):
        self.children.remove(name)


class Repository:

    def __init__(self):
        self.branches = []

    def get_parent(self, name):
        for branch in self.branches:
            for child in branch.children:
                if child == name:
                    return branch
        return None

    def add_branch(self, name):
        branch = Branch(name)
        self.branches.append(branch)
        return branch

    def print_connections(self):
        for branch in self.branches:
            for child in branch.children:
                print(branch.name + ' ' + child)         


repository = Repository()
valid_repository = True
i = 0

branches_quantity = int(input())

while i < branches_quantity and valid_repository:
    i += 1
    params = input().split()
    children_quantity = int(params[1])

    if children_quantity == 0:
        continue

    name = params[0]
    parent = repository.get_parent(name)
    branch = repository.add_branch(name) 
    
    for j in range(2, children_quantity + 2):
        ck_name = params[j]

        if parent and parent.name == ck_name:
            valid_repository = False
            break

        ck_parent = repository.get_parent(ck_name)

        if ck_parent:
            if parent is ck_parent:
                ck_parent.delete_child(ck_name)
                branch.add_child(ck_name)
        else:
            branch.add_child(ck_name)

if valid_repository:
    print('TAK')
    repository.print_connections()
else:
    print('NIE')