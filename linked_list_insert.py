class linkedListNode():
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head=head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode=self.head
        while True:
            if currentNode.nextNode is None:
                currentnode.nextNode=node
                break
            currentNode = currentNode.nextNode
            #return currentNode

    def printLinkedList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.value, '->')
            currentNode = currentNode.nextNode
        print('none')


node1 = linkedListNode("3")
node2=linkedListNode("4")
node1.nextNode = node2
currentNode = node1


ll=linkedList()
ll.printLinkedList()
ll.insert('55')
ll.printLinkedList()



print(node1.value)
print(node2.value)



