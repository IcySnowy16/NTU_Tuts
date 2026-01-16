class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data, index):
        if index < 0 or index > self.size:
            return ValueError("Invalid Position")

        elif index == 0: 
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        
        #! don't need put self.head one, need exclude index == 0 one

        else:
            curr = self.head
            prev = curr


            while index > 0 or curr != None:
            #! cant use and
            #! cant remove curr != None
                prev = curr
                curr = curr.next
                index -= 1

            
            new_node = Node(data)
            new_node.next = curr
            prev.next = new_node

            
        self.size += 1

        return True
    
    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            return False
        

        curr = self.head
        
        if index == 0:
            self.head = curr.next
            self.size -= 1
            return True
            
        prev = curr
        while index > 0:
            prev = curr
            curr = curr.next
            index -= 1

        prev.next = curr.next
        self.size -= 1

        return True

        
    
    def printList(self):
        if self.size == 0:
            return ValueError("No Nodes in LinkedList")
        
        curr = self.head
        while curr != None:
            print(f"{curr.data}", end=" ")
            curr = curr.next
        print("")


# Q1
def move_even_items_to_back(ll):
    if ll.size == 0:
        return ValueError("No Nodes in LinkedList")
    
    curr = ll.head
    insert_pt = ll.size - 1
    counter = ll.size
    index = 0


    while counter > 0:
        if curr.data % 2 == 0:
            ll.removeNode(index) #! had problems with remove node
            ll.insert(curr.data, insert_pt)
        else:
            index += 1 #! forgot to add index

        curr = curr.next
        counter -= 1

    return True

def q1():
    linked_list = LinkedList()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    LL = input()
    LL_lst = LL.strip().split()

    index = 0

    for values in LL_lst:
        if values.isdigit() is True:
            linked_list.insert(int(values), index)
            index += 1
        else:
            break

    print("Original LinkedList:")
    linked_list.printList()

    print("The resulting Linked List after moving even integers to the back of the Linked List is: ", end="")
    move_even_items_to_back(linked_list)
    linked_list.printList()

# Q2
def move_max_to_front(ll):
    passes = ll.size
    temp = ll.head.data
    temp_index = 0
    curr = ll.head.next

    for index in range(1, passes):
        if temp < curr.data: #! Comparison wrong
            temp = curr.data
            temp_index = index
            
        curr = curr.next

    ll.removeNode(temp_index)
    ll.insert(temp, 0) #insert has some problem

    return True

def q2():
    linked_list = LinkedList()

    print('''1. Insert an integer to the linked list:  
2: Move the node with the largest stored value to the front of the 
list:  
0: Quit)\n''')
    
    choice = -1

    while choice != 0:
        choice = int(input("Please input your choice(1/2/0): "))
        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            linked_list.insert(int(value), linked_list.size)
            print(f"The Linked List is: ", end="")
            linked_list.printList()
        elif choice == 2:
            move_max_to_front(linked_list)
            print(f"The resulting Linked List is: ", end="")
            linked_list.printList()

# Q3
def remove_duplicates_sorted_ll(ll):
    curr = ll.head
    index = 0

    while curr.next != None:
        if curr.data == curr.next.data:
            ll.removeNode(index+1)
        else:
            index += 1

        curr = curr.next

    return True

def q3():
    linked_list = LinkedList()

    print('''1. Insert an integer to the linked list:  
2: Remove duplicates from a sorted linked list:  
0: Quit\n''')
    
    choice = -1

    while choice != 0:
        choice = int(input("Please input your choice(1/2/0): "))
        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            linked_list.insert(int(value), linked_list.size)
            print(f"The Linked List is: ", end="")
            linked_list.printList()
        elif choice == 2:
            remove_duplicates_sorted_ll(linked_list)
            print(f"The resulting Linked List is: ", end="")
            linked_list.printList()



# Q4
def T2Q1(s,q):
    temp = s
    while temp.next != q:
        temp = temp.next
    temp.next = s

#T2Q1(Apter, Bpter) #
#T2Q1(Bpter, Apter) #

# Separate into 2 circular linkedlist

if __name__ == "__main__":
    choices = -1
    while choices != 0:
        choices = int(input("Qn No(1/2/3/0): "))
        if choices < 0 or choices > 3:
            raise ValueError("Invalid Choice")
        elif choices == 1:
            q1()
        elif choices == 2:
            q2()
        elif choices == 3:
            q3()
        else:
            pass