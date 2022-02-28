## log(n) search

import subprocess
'''$ python download_imdb.py'''

def load_names(path):
    def load_csvfile():
        process = subprocess.Popen(['echo', 'More output'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # stdout, stderr

        load_csvfile()

        # names = load_names('names.txt')
        # sorted_names = load_names('sorted_names.txt')

        with open('./names.txt') as f:
            return f.read().splitlines()


class BinarySearch_TreeNode(): #to create a node
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    ''' checks node value, make sure its root, leaf etc..; call when adding new node'''
    def add_child(self, data):
        if data == self.data: # binary cannot have duplicate elements
            return

        if data < self.data:
            ## add to left subtree
            if self.left: # if self.left has a value
                print(self.left.add_child(data))
                return self.left.add_child(data)

            else: # if left node is empty, then create a left tree node data to
                self.left = BinarySearch_TreeNode(data)

        else: # add data to right subtree
            if self.right: # if self.left has a value
                print(self.right.add_child(data))

                return self.right.add_child(data)
            else: # if left node is empty, then create a left tree node data to
                self.right = BinarySearch_TreeNode(data)



    def in_order_traversal(self):
        elements = []
        # traverse left part of the tree
        if self.left:
            elements += self.left.in_order_traversal() # recursive call to add element to master elements

        # visit the base node
        elements.append(self.data)

        # traverse right part of the tree:
        if self.right:
            elements += self.left.in_order_traversal() # recursive call to add element to master elements

        return elements

    def search(self, search_val): ## recursive search, will element is found
        # if self.data in search_val:
        #     print('\n\nfound value, in statement')
        #     pass

        if self.data == search_val: ## recursive stop
            print('\n\nfound the value: == statement', search_val)
            return True

        if search_val < self.data: ## check the left subtree
            print('\n\nsearching left nodes\n', search_val)
            if self.left:
                self.left.search(search_val)
            else:
                print('\n\n Element not found in left stack ')
                return False

        if search_val > self.data: ## check the right  subtree
            print('\n\nsearching right nodes\n', search_val)
            if self.right:
                self.right.search(search_val)
            else:
                print('\n\n Element not found in right stack ')
                return False



def main():
    def build_tree(elements):
        print('Current Elements\n', elements)
        print('Element at index 0 \n', elements[0])
        root = BinarySearch_TreeNode(elements[0])
        len_elements = len(elements)
        for i in range(1, len_elements):
            root.add_child(elements[i])
            return root

    numbers = [5,3,2,2,5,6,3]
    numbers_tree = build_tree(numbers)
    print('X'*50)
    print('\n\t\t after traverse', numbers_tree.in_order_traversal())
    print(numbers_tree.search(5))

if __name__ == '__main__':
    main()

