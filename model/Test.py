from model.Puzzle8 import Puzzle8
from model.Search import Search
from anytree import Node
from anytree.dotexport import DotExporter



test = [1, 2, 3, 4, 5, 6, 0, 7, 8]
tree = Node(test)
test2 = [2, 3, 1, 4, 5, 6, 0, 7, 8]
tree2 = Node(test2, parent=tree)
test3 = [2, 1, 4, 3, 5, 6, 0, 7, 8]
tree3 = Node(test3, parent=tree)
test4 = [2, 1, 3, 5, 6, 4, 0, 7, 8]
tree4 = Node(test4, parent=tree2)
test5 = [2, 1, 3, 4, 5, 6, 7, 0, 8]
tree5 = Node(test5, parent=tree3)
# print(test.__cmp__(test2))
p = Puzzle8(test)
p1 = Puzzle8(test2)

# print(p.__cmp__(p1))
search = Search()
# print( p < p1)
# search.bfs(p)

#
# tree = Node(p.__str__())
# tree1 = Node(p1.__str__(), tree)
# print(tree1)
#
# for pre, fill, node in RenderTree(tree):
#     print("%s%s" % (pre, node.name))
#
DotExporter(tree).to_picture("tree.png")
