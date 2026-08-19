class Node :
    def __init__ (self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree :
    def __init__(self, root=None):
        self.root = root

    def insert (self, data, current=None):
        if self.root is None:
            self.root = Node(data)
            return

        if current == None:
            current = self.root

        if data < current.data:
            if current.left_child is None:
                current.left_child = Node(data)
            else:
                current = current.left_child
                self.insert(data, current)
        else:
            if current.right_child is None:
                current.right_child = Node(data)
            else:
                current = current.right_child
                self.insert(data, current)


    def search(self, data, current=None):
        if self.root is None:
            return None
        
        if current is None:
            current = self.root
        
        if current.data == data:
            return current
        
        if data < current.data:
            if current.left_child is None:
                return None
            return self.search(data, current.left_child)
        elif data >= current.data:
            if current.right_child is None:
                return None
            return self.search(data, current.right_child)

    def find_max(self):
        current = self.root
        while current.right_child is not None:
            current = current.right_child
        return current

    def find_min(self, current=None):
        if current is None:
            current = self.root

        while current.left_child is not None:
            current = current.left_child
        return current

    def remove(self, data):
        removing = self.search(data)
        if removing is None:
            return
        father = self.search_father(data)
        if removing.left_child is None and removing.right_child is None:
            if father is None:
                self.root = None
            elif father.left_child == removing:
                father.left_child = None
            else:
                father.right_child = None

        elif removing.right_child is None:
            if father is None:
                self.root = removing.left_child
            elif father.left_child == removing:
                father.left_child = removing.left_child
            else:
                father.right_child = removing.left_child

        elif removing.left_child is None:
            if father is None:
                self.root = removing.right_child
            elif father.left_child == removing:
                father.left_child = removing.right_child
            else:
                father.right_child = removing.right_child

        else:
            replacement = self.find_min(removing.right_child)
            replacement_father = self.search_father(replacement.data)
            removing.data = replacement.data
            if replacement_father.left_child == replacement:
                replacement_father.left_child = replacement.right_child
            else:
                replacement_father.right_child = replacement.right_child
        

    def in_order_deleter(self, node):
        if node is None:
            return
        self.in_order(node.left_child)
        return node

    def search_father(self, data, current=None, father=None):
        if self.root is None:
            return None
        
        if current is None:
            current = self.root
        
        if current.data == data:
            return father
        
        if data < current.data:
            if current.left_child is None:
                return None
            return self.search_father(data, current.left_child, current)
        elif data >= current.data:
            if current.right_child is None:
                return None
            return self.search_father(data, current.right_child, current)