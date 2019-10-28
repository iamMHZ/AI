from model.Utility import printer
from model.Puzzle8 import Puzzle8
from anytree import Node, RenderTree
from anytree.dotexport import DotExporter



test = [1, 2, 3, 4, 5, 6, 0, 7, 8]
p = Puzzle8(test)
tree = Node(p)

test2 = [2, 3, 1, 4, 5, 6, 0, 7, 8]
p2 = Puzzle8(test2)
tree2 = Node(p, parent=tree)

test3 = [2, 1, 4, 3, 5, 6, 0, 7, 8]
p3 = Puzzle8(test3)
tree3 = Node(p3, parent=tree)

test4 = [2, 1, 3, 5, 6, 4, 0, 7, 8]
p4 = Puzzle8(test4)
tree4 = Node(p4, parent=tree2)

test5 = [2, 1, 3, 4, 5, 6, 7, 0, 8]
p5 = Puzzle8(test5)
tree5 = Node(p5, parent=tree3)

# tree = Node(p.show())
# tree1 = Node(p1.show(), tree)
# print(tree1)

for pre, fill, node in RenderTree(tree):
    print("%s%s" % (pre, printer(str(node.name))))
    # print(str(node.name) + "\n")

DotExporter(tree).to_picture("tree.png")




