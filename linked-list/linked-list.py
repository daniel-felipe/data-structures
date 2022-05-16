""" A simple implementation of an Linked List """

""" Creating a Node class for linked list """
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
            if current_node is None:
                return
        return current_node.data

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        while current_node:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1
        return None

    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
        
        current_node = self.first_node
        current_index = 0
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1     
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
        current_node = self.first_node
        current_index = 0
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
        after_deleted = current_node.next_node.next_node
        current_node.next_node = after_deleted 

# Testing
node_1 = Node('orange')
node_2 = Node('strawberry')
node_3 = Node('banana')
node_4 = Node('blueberry')

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

# Creating list
list = LinkedList(node_1)
list.insert_at_index(3, 'hahahaha')
# print(list.read(3))
arr = []