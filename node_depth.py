

class BinarySearch_TreeNode(): #to create a node
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        print(self.value)

    # def nodeDepths(root, depth=0):
    #     # print(self.depth)
    #     # print(self.data)
    #     print('root', root)
    #     if root is None:
    #         print('nothing here')
    #         return 0
    #     #print('depth', depth + 1)
    #     # print(depth + BinarySearch_TreeNode.nodeDepths(self.left) + BinarySearch_TreeNode.nodeDepths(self.right))
    #     return depth + BinarySearch_TreeNode.nodeDepths(root.left, depth + 1) + BinarySearch_TreeNode.nodeDepths(root.right, depth + 1)
    #     pass
    #


def nodeDepths(root, depth=0):
    # print(self.depth)
    # print(self.data)
    print('root', root)
    if root is None:
        print('nothing here')
        return 0
    #print('depth', depth + 1)
    # print(depth + BinarySearch_TreeNode.nodeDepths(self.left) + BinarySearch_TreeNode.nodeDepths(self.right))
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    pass



root = {
    "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": None, "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9}
    ],
    "root": "1"
}
bs = BinarySearch_TreeNode(root)
# bs.nodeDepths(root)

result = nodeDepths(root)
print(result)



