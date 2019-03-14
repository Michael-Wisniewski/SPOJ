class Branch:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, branch):
        self.children.append(branch)

    def unplug(self):
        self.parent.children.remove(self)


def search(branch, name):
    for child in branch.children:
        result = search_branch(child, name)
        if result is not None:
            return result
    return None


def search_branch(branch, name):
    if branch.name == name:
        return branch
    for child in branch.children:
        result = search_branch(child, name)
        if result is not None:
            return result
    return None


def search_inside(branch, branch_list):
    for child in branch.children:
        search_inside_branch(child, branch_list)


def search_inside_branch(branch, branch_list):
    if branch.name in branch_list:
        branch_list.remove(branch.name)
    for child in branch.children:
        search_inside_branch(child, branch_list)


def search_outside(branch, branch_list):
    for child in branch.children:
        result = search_outside_branch(child, branch_list)
        if result is True:
            return True
    return False


def search_outside_branch(branch, branch_list):
    if branch.name in branch_list:
        return True
    for child in branch.children:
        result = search_outside_branch(child, branch_list)
        if result is True:
            return True
    return False


def print_connections(branch):
    for child in branch.children:
        print_connections(child)
        print(branch.name + ' ' + child.name)


input_lines = []
valid_repository = True
root = Branch(None, None)

branches_quantity = int(input())

i = 0
while i < branches_quantity:
    line = input()
    input_lines.append(line)
    i += 1

i = 0
while i < branches_quantity and valid_repository:
    params = input_lines[i].split()
    i += 1

    children_quantity = int(params[1])
    if children_quantity == 0:
        continue

    name = params[0]
    del params[:2]
    children_to_remove = []
    branch = search(root, name)

    if branch is None:
        branch = Branch(name, root)
    else:
        branch.parent.children.remove(branch) 

    for parent_child in branch.parent.children:
        
        if parent_child.name in params:
            parent_child.parent = branch
            branch.add_child(parent_child)
            params.remove(parent_child.name)
            children_to_remove.append(parent_child)
        
    for child in children_to_remove:
        branch.parent.children.remove(child)
       
    if params:
        search_inside(branch, params)

    if params:
        if branch.parent.name is not None:
            valid_repository = False
        else:
            if search_outside(root, params):
                valid_repository = False
            else:
                for new_branch_name in params:
                    new_branch = Branch(new_branch_name, branch)
                    branch.add_child(new_branch)
                
    branch.parent.add_child(branch)


if valid_repository and len(root.children) == 1:
    print('TAK')
    print_connections(root.children[0])
else:
    print('NIE')