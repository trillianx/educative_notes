class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value " + str(value) + " already in BST")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
        return ''

    def show(self):
        if self.root:
            self.inorder(self.root)

    def height(self):
        if self.root:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node:
            left = self._height(cur_node.left, cur_height+1)
            right = self._height(cur_node.right, cur_height+1)
            return max(left, right)
        else:
            return cur_height
    
    def search(self, value):
        if self.root:
            return self._search(self.root, value) == True
        else:
            return None

    def _search(self, cur_node, value):
        if value == cur_node.data:
            return True
        if value < cur_node.data:
            if cur_node.left is not None:
                return self._search(cur_node.left, value)
            else:
                return False
        elif value > cur_node.data:
            if cur_node.right is not None:
                return self._search(cur_node.right, value)
            else:
                return False
        

if __name__ == "__main__":
    arr = [10, 8, 11, 5, 5]
    b = BST()
    for a in arr:
        b.insert(a)
    b.show()
    print(b.search(5))
    print(b.search(10))
    print(b.search(100))