class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
            
        new_node = ListNode(value)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.find_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node
            
        self.size += 1
        return 0

    def remove_node(self, index):
        if index < 0 or index >= self.size:
            return -1
            
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.find_node(index - 1)
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
                
        self.size -= 1
        return 0

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.insert_node(0, item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.item

    def is_empty(self):
        return self.ll.size == 0

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        self.ll.insert_node(self.ll.size, item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def is_empty(self):
        return self.ll.size == 0
    


# Q1
def reverse_stack(stack):
    q = Queue()

    while stack.peek() != None:
        q.enqueue(stack.pop())

    while q.ll.head != None:
        stack.push(q.dequeue())

    return True


# Q2
def reverse_first_k_items(queue, k):
    s = Stack()

    for _ in range(k):
        s.push(queue.dequeue())

    while not s.is_empty():
        queue.enqueue(s.pop())

    for _ in range(queue.ll.size - k):
        queue.enqueue(queue.dequeue())   

    return True

# Q3
def sort_stack(stack):
    s2 = Stack()

    while not stack.is_empty():
        s2.push(stack.pop())
        
    s2.ll.print_list()

    temp = s2.pop()

    while not s2.is_empty():
        if temp < s2.peek():
            stack.push(temp)
            temp = s2.pop()
        
    

    return True



s = Stack()
l = [1,2,3,4,5]
for i in l:
    s.push(i)

# print("Before:")
# s.ll.print_list()
# print("After:")
# reverse_stack(s)
# s.ll.print_list()


q = Queue()
l = [1,2,3,4,5]
for i in l:
    q.enqueue(i)

# print("Before:")
# q.ll.print_list()
# print("After:")
# reverse_first_k_items(q, 3)
# q.ll.print_list()



s2 = Stack()
l = [2,3,1,5,4]
for i in l:
    s2.push(i)

print("Before:")
s2.ll.print_list()
print("After:")
sort_stack(s2)
s2.ll.print_list()



# Q4

#a) x=a+b*c%d>>e (infix) to xabc*d%+e>>= (postfix)
#b) =y&&<<ab>>c+de (prefix) to 

