from model.Puzzle8 import Puzzle8
from model.Search import Search
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from graphviz import render
from graphviz import Source

test = [1, 2, 3, 4, 5, 6, 0, 7, 8]

test2 = [2, 1, 3, 4, 5, 6, 0, 7, 8]

# print(test.__cmp__(test2))
p = Puzzle8(test)
p1 = Puzzle8(test2)

# print(p.__cmp__(p1))
search = Search()
# print( p < p1)
# search.a_star(p)


tree = Node(p.__str__())
tree1 = Node(p1.__str__(), tree)
print(tree1)

for pre, fill, node in RenderTree(tree):
    print("%s%s" % (pre, node.name))

DotExporter(tree).to_picture("tree.png")

#https://bobswift.atlassian.net/wiki/spaces/GVIZ/pages/20971549/How+to+install+Graphviz+software