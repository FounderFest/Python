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

a = Item("a")
b = Item("b")
c = Item("c")

a.next = b
b.next = c
c.next = None

c.printList(a)