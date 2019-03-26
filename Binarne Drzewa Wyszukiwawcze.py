# Zadanie
# https://pl.spoj.com/problems/TBDW/
# Opis rozwiązania
# http://aroundpython.com/index.php/2019/03/11/binarne-drzewa-wyszukiwawcze/


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def del_connections(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None


class Tree:
    root_node = None

    def __init__(self, value):
        self.root_node = Node(value)

    def __search(self, value):
        node = self.root_node
        while True:
            if value == node.value:
                return node
            elif (value < node.value) and (node.left is not None):
                node = node.left
            elif node.right is not None:
                node = node.right
            else:
                return None

    def __min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def __max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def __successor(self, node):
        if node.right is not None:
            return self.__min(node.right)

        parent = node.parent
        while parent is not None:
            if parent.left is node:
                return parent
            else:
                node = parent
                parent = parent.parent
        return None

    def __predecessor(self, node):
        if node.left is not None:
            return self.__max(node.left)
        
        parent = node.parent
        while parent is not None:
            if parent.right is node:
                return parent
            else:
                node = parent
                parent = parent.parent
        return None

    def __del_leafless(self, node):
        if node.parent is not None:
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None

        node.del_connections()

    def __del_with_one_leaf(self, node):
        if node.left is not None:
            child = node.left
        else:
            child = node.right

        if node.parent is None:
            child.parent = None
            self.root_node = child
        else:
            child.parent = node.parent
            if node.parent.left is node:
                node.parent.left = child
            else:
                node.parent.right = child

        node.del_connections()

    def __pre_order(self, node):
        result = str(node.value) + ' '
        if node.left is not None:
            result += self.__pre_order(node.left)
        if node.right is not None:
            result += self.__pre_order(node.right)
        return result

    def __in_order(self, node):
        result = ''
        if node.left is not None:
            result += self.__in_order(node.left)
        result += str(node.value) + ' '
        if node.right is not None:
            result += self.__in_order(node.right)
        return result

    def __post_order(self, node):
        result = ''
        if node.left is not None:
            result += self.__post_order(node.left)
        if node.right is not None:
            result += self.__post_order(node.right)
        result += str(node.value) + ' '
        return result

    def __nodes_at_deph(self, node, deph, actual_deph=0):
        result = ''

        if (deph == actual_deph + 1) and (node.left or node.right is not None):
            result += 'P(' + str(node.value) + ') '
            if node.left is None:
                result += '- '
            else:
                result += str(node.left.value) + ' '

            if node.right is None:
                result += '- '
            else:
                result += str(node.right.value) + ' '
        else:
            if node.left is not None:
                result += self.__nodes_at_deph(node.left, deph, actual_deph+1)
            if node.right is not None:
                result += self.__nodes_at_deph(node.right, deph, actual_deph+1)

        return result

    def insert(self, value):
        node = self.root_node
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value, node)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(value, node)
                    break
                else:
                    node = node.right

    def delete(self, value):
        node = self.__search(value)

        if node is None:
            return

        if node.left and node.right is not None:
            predecessor = self.__predecessor(node)
            node.value = predecessor.value
            if predecessor.left is not None:
                self.__del_with_one_leaf(predecessor)
            else:
                self.__del_leafless(predecessor)
        elif node.left or node.right is not None:
            self.__del_with_one_leaf(node)
        else:
            self.__del_leafless(node)
            
    def search(self, value):
        node = self.__search(value)
        if node is None:
            return '-'
        else:
            return node.value

    def min(self):
        node = self.__min(self.root_node)
        return node.value

    def max(self):
        node = self.__max(self.root_node)
        return node.value

    def successor(self, value):
        node = self.__search(value)
        if node is None:
            return '-'
        else:
            successor = self.__successor(node)
            if successor is None:
                return '-'
            else:
                return successor.value

    def predecessor(self, value):
        node = self.__search(value)
        if node is None:
            return '-'
        else:
            predecessor = self.__predecessor(node)
            if predecessor is None:
                return '-'
            else:
                return predecessor.value

    def print_tree(self):
        result = self.root_node.value
        deph = 1

        while result:
            print(result)
            result = self.__nodes_at_deph(self.root_node, deph)
            deph += 1

    def pre_order(self):
        result = self.__pre_order(self.root_node)
        return result

    def in_order(self):
        result = self.__in_order(self.root_node)
        return result

    def post_order(self):
        result = self.__post_order(self.root_node)
        return result

output = []
tests = int(input())

for i in range(1, tests+1):
    output.append('test ' + str(i))
    iterations = int(input())
    root_val = int(input()[2:])
    tree = Tree(root_val)
    
    while iterations > 1:
        operation = input().split()
        command = operation[0]
        value = int(operation[1])
        iterations -= 1

        if command == 'I':
            tree.insert(value)
            continue
        if command == 'D':
            tree.delete(value)
            continue

        result = ''
        if command == 'S':
            result = tree.search(value)
        elif command == 'N':
            result = tree.successor(value)
        elif command == 'P':
            result = tree.predecessor(value)
        elif command == 'X':
            if value == 0:
                result = tree.min()
            else:
                result = tree.max()
        elif command == 'R':
            if value == 0:
                result = tree.in_order()
            elif value == 1:
                result = tree.pre_order()
            else:
                result = tree.post_order()
        
        output.append(result)

for line in output:
    print(line)