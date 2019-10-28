from anytree import Node

class MyNode(Node):
    
    def __lt__(self, other):
        return self.height > other.height