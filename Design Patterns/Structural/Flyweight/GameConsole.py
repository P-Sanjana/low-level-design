from Tree import Forest
class GameConsole:
    forest = Forest()

    forest.plant_trees("Oak", "oak_texture", "green", 10, 20)
    forest.plant_trees("Pine", "pine texture", "dark green", 25, 40)
    forest.plant_trees("Oak", "oak texture", "green", 45, 76)

    forest.draw()
