from TreeFactory import TreeFactory
class Tree:
    def __init__(self, x, y, treeType):
        self.x = x
        self.y = y
        self.treeType = treeType

    def draw(self):
        self.treeType.draw(self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_trees(self, name, texture, color, x, y):
        treeType = TreeFactory.getTreeType(name, texture, color)
        tree = Tree(x, y, treeType)
        self.trees.append(tree)

    def draw(self):
        for t in self.trees:
            t.draw()