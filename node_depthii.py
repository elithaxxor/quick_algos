def nodeDepth(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepth(root.left, depth+1) + nodeDepth(root.right, depth+1)


class BinaryTree:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        # self.root=0
        # self.depth=0



data = {
    "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": null, "right": null, "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "7", "left": null, "right": null, "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "9", "left": null, "right": null, "value": 9}
    ],
    "root": "1"
}

root=3
depth = nodeDepth(data)
