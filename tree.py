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
            if parent.left == node:
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
            if parent.right == node:
                return parent
            else:
                node = parent
                parent = parent.parent
        return None

    def __del_leafless(self, node):
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

        node.del_connections()

    def __del_with_one_leaf(self, node):
        if node.left is not None:
            child = node.left
        else:
            child = node.right

        child.parent = node.parent

        if node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child

        node.del_connections()

    def __nodes_at_deph(self, node, deph, actual_deph=0):
        result = ''

        if (deph == actual_deph + 1) and (node.left or node.right is not None):
            result += 'P({}) '.format(node.value)
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
                result += self.__nodes_at_deph(node.left, deph, actual_deph + 1)
            if node.right is not None:
                result += self.__nodes_at_deph(node.right, deph, actual_deph + 1)

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
            successor = self.__successor(node)
            node.value = successor.value
            self.__del_with_one_leaf(successor)
        elif node.left or node.right is not None:
            self.__del_with_one_leaf(node)
        else:
            self.__del_leafless(node)
            
    def search_value(self, value):
        node = self.__search(value)
        if node is None:
            print('-')
        else:
            print(node.value)

    def search_successor(self, value):
        node = self.__search(value)
        if node is None:
            print('-')
        else:
            successor = self.__successor(node)
            if successor is None:
                print('-')
            else:
                print(successor.value)

    def search_predecessor(self, value):
        node = self.__search(value)
        if node is None:
            print('-')
        else:
            predecessor = self.__predecessor(node)
            if predecessor is None:
                print('-')
            else:
                print(predecessor.value)

    def print(self):
        result = self.root_node.value
        deph = 1
        
        while result:
            print(result)
            result = self.__nodes_at_deph(self.root_node, deph)
            deph += 1


import fileinput
data_file = fileinput.input("./data.txt")          
        
tree = Tree(5)

for line in data_file:
    line = line.rstrip('\n')
    line_arr = line.split(" ", 1)

    tree.insert(int(line_arr[1]))

tree.print()