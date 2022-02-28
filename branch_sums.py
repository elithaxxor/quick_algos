## sum of all values of branch (root to leaf)
## every horizontal node (new level) is a multiple of 2 (2^2)
##

var = {
    "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": "10", "right": null, "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "7", "left": null, "right": null, "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "9", "left": null, "right": null, "value": 9},
        {"id": "10", "left": null, "right": null, "value": 10}
    ],
    "root": "1"
}


class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(node, runningSum, sums):
    sums = []
    calculateBranchSums(root, 0, sums)


def calculateBranchSums(node, runningSum, sums):

    newRunningSum = runningSum + node.value
    if node.left == None and node.right == None:  # indicates leaf node
        sums.append(newRunningSum)
        return

    ## start recursive call,
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


# This is the class of the input root. Do not edit it.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def branchSums(root):
  sums = []
  calculateBranchSums(root, 0, sums)
  return sums


def calculateBranchSums(node, runningSum, sums):
  if node is None:
    return
  newRunningSum = runningSum + node.value

  if node.left is None and node.right is None:  # indicates leaf node
    sums.append(newRunningSum)
    return
  ## start recursive call,
  calculateBranchSums(node.left, newRunningSum, sums)
  calculateBranchSums(node.right, newRunningSum, sums)


