class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# l_list = LinkedList()

# data = []
# for i in range(1, 10):
#     data.append(i)
#
# l_list.head = Node(data[0])
# for j in data[1:]:
#     l_list.append(j)
#
# l_list.push(78) => ha bir method uchin bularni mashq qilib ko'rdim faqat insert uchin emas chunki ustoz insertni kelasi dars o'rgataman degandila
# print(l_list.printList())

# a = Node(9)
# b = Node(18)
# c = Node(13)
# l_list = LinkedList() = > bularni ham har birini boshqa boshqa holatlarda mashq qilib ko'rdim
# l_list.head = a
# a.next = b
# b.next = c
# print(l_list.printList())

