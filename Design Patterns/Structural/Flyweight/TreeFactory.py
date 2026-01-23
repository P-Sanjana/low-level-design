from TreeType import TreeType
class TreeFactory:
    _treeTypes = {}

    @staticmethod
    def getTreeType(name, texture, color):
        key = name+texture+color
        if key not in TreeFactory._treeTypes:
            TreeFactory._treeTypes[key] = TreeType(name, texture, color)
        return TreeFactory._treeTypes[key]

