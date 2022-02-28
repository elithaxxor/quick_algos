class linkedListNode():
    def __init__(self, value, nextNode=None):
        self.value=value
        self.nextNode = nextNode

class linkedList():
    def __init__(self, head=None):
        self.head=head
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = value
            return
        currentNode=self.head

        while True:
            if currentNode is not None:
                currentNode.nextNode = node
                break
            currentNode=currentNode.nextNode

    def printLinkedList (self):
        currentNode = self.head
        print('NEXT NODE TEST ', currentNode.nextNode.value)
        while True:
            if currentNode is not None:
                if currentNode.value == currentNode.nextNode.value:
                    print('[DUPLICATES-FOUND]: ', currentNode.value, currentNode.nextNode.value)
                    return currentNode.nextNode.value
                    #duplicates.append(currentNode.value)
                print('[NODE TRAVERSAL]', currentNode.value, '->')
                currentNode = currentNode.nextNode


            # if currentNode.value == currentNode.nextNode:
            #     print('duplicate found: ', currentNode.value, currentNode.nextNode)
            # currentNode = currentNode.nextNode
            #

node1=linkedListNode('3')
node2=linkedListNode('6')
node3=linkedListNode('9')
node4=linkedListNode('9')

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4


currentNode=node1
ll = linkedList(currentNode)
ll.printLinkedList()


''' ANOTHER CORRECT ANSWER (ALGOEXPERT'''


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return linkedList




