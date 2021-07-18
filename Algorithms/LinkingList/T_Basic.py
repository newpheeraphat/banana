class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

class linkingList:
    def __init__(self) -> None:
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
    
    def display(self):
        element = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            element.append(cur_node.data)
        print(element)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' is out of range")
            return None
        cur_node = self.head
        count_index = 0
        while True:
            cur_node = cur_node.next
            if count_index == index: 
                return cur_node.data
            count_index += 1

    def remove(self, index):
        if index >= self.length():
            print("ERROR: 'Remove' is out of range")
            return None
        count_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if count_index == index:
                last_node.next = cur_node.next
                return 
            count_index += 1
