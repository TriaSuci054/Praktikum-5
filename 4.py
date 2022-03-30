'''
Nama  : Tria Suci Cahyani
NIM   : 20051397054
Kelas : 2020B
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, element):
        new_item = Node(element)

        if self.rear == None:
            self.front = self.rear = new_item
            return
        self.rear.next = new_item
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            print("You cannot dequeue from an empty queue.")
        else:
            removed_item = self.front
            self.front = removed_item.next

            if (self.front == None):
                self.rear = None
            return removed_item.data


    def print_queue(self):
        item = self.front
        if self.is_empty():
            print("The queue is empty.")
        else:
            queue = []
            while (item != None):
                queue.append(item.data)
                item = item.next
            print (queue)



class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.is_empty():
            print ('You cannot pop from an empty stack.')
            return None
        else:
            popped_item = self.head
            self.head = self.head.next
            popped_item.next = None
            return popped_item.data

    def print_stack(self):
        item = self.head
        if self.is_empty():
            print("The stack is empty.")
        else:
            stack = []
            while (item != None):
                stack.append(item.data)
                item = item.next
            print(stack)

class PalindromeCheck:

    def __init__(self, word):
        self.word = word
        self.queue = Queue()
        self.stack = Stack()

    def check_palindrome(self):
        i = 0
        mid = len(self.word)//2
        for letter in self.word:
            if (i<mid):                                  
                self.stack.push(letter)                 
            else:                                        
                self.queue.enqueue(letter)
            i+=1

        if (len(self.word)%2 != 0):
            self.queue.dequeue()
        for i in range(len(self.word) // 2):
            if self.queue.dequeue() != self.stack.pop():
                return False

        return True


if __name__ == '__main__':
    given_str = input("Masukkan Kata/Kalimat: ").lower()

    test = PalindromeCheck(given_str)
    if (test.check_palindrome()):
        print("Kalimat tersebut adalah palindrome!")
    else:
        print("Kalimat tersebut bukan palindrome.")
