
class BinaryTree:
    def __intit__(self):
        self.root = 0
        self.tree = [
            Node("A" , 1, 2),              #0
            Node("B" , 3, 4),        #1
            Node("C" ,8, 9),        #2
            Node("D" , 5, None),         #3
            Node("E" , 6, 7),         #4
            Node("F" , None, None),         #5
            Node("G" , None, None),         #6
            Node("H" , None, None),         #7
            Node("I" , None, None),         #8
            Node("J" , 10, 11),         #9
            Node("K" , None, None),         #10
            Node("L" , None, None)       #11
        ]


    def dft(self, root):
        
        current_node = self.tree[root]
        left = current_node.left
        right = current_node.right

        if left != None:
            self.dft(left)

        if right != None:
            self.dft(right)

        print(current_node.data)


        #left
        #right
        #root



class Node:
    def __init__(self, data, left, right):

        self.data = data
        self.left = left
        self.right = right


my_tree = BinaryTree()
my_tree.dft(0)