class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def get_root(self):
        return self.root

    def __str__(self):
        return str(self.root)
