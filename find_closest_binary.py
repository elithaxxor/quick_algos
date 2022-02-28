def findClosestValueInBst(tree, target):
    closest = float('inf')
    print(tree)
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:  ## find leaf
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    if target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = Nonei
        self.right = None
        print(self.value)


tree = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "13", "left": None, "right": "14", "value": 13},
        {"id": "14", "left": None, "right": None, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": None, "value": 2},
        {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "10"
}
print(type(tree))
target = 12
findClosestValueInBst(tree, target)
