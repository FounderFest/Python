# ListasEnlazadas.py
# Carlos Linares
# 18/12/2015

class Item:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    # Override __str__ function
    def __str__(self):
        return str(self.value)

    def printList(self, item):
        while item:
            print(item.value)
            item = item.next
        print("\n")

class LinkedList:
    def __init__(self):
        self.items = []
        self.count = 0
        self.first = None
        self.last = None

    def add(self, item):
        self.items.append(item)
        self.count += 1

        if self.count == 0:
            self.first = item

    def get_count(self):
        return self.count

    def printList(self):
        if self.count > 0:
            for i in self.items:
                print(i.value)

            print("\n")

lista = LinkedList()
lista.add(Item("1"))
lista.add(Item("2"))
lista.add(Item("3"))
lista.add(Item("4"))
lista.add(Item("5"))

print("lista.count: " + str(lista.get_count()))
lista.printList()

a = Item("a")
b = Item("b")
c = Item("c")

a.next = b
b.next = c
c.next = None

c.printList(a)