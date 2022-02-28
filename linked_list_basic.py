class linkedList():
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode


node1 = linkedList("3")
node2 = linkedList("4")
node3 = linkedList("6")
node4 = linkedList("37")

node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4

print(node1.value)
print(node2.value)

currentNode = node1
node_count = 0
while True:
    print(currentNode.value, '->')
    if currentNode.nextNode is None:
        print('None')
        break
    node_count += 1
    currentNode = currentNode.nextNode
print('total iterations',node_count)
