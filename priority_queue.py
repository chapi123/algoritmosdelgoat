class Element:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue (self, element):
        if len(self.queue) == 0:
            self.queue.append(element)
            return
        
        index = 0

        while index < len(self.queue):
            current = self.queue[index]

            if element.priority < current.priority:
                self.queue.insert(index, element)
                return
            
            if element.priority == current.priority:
                self.queue.insert(index + 1, element)
                return
            
            index += 1

        self.queue.append(element)

    def peek (self) :
        return self.queue[0].value

    def isEmpty (self) :
        return len(self.queue) == 0

    def size (self) :
        return len(self.queue)

    def dequeue(self) :
        dequeued = self.queue.pop(0)
        return dequeued

    def show_values(self):
        for i in self.queue:
            print(i.value)

    def show_priorities(self):
        for i in self.queue:
            print(i.priority)

instance = PriorityQueue()
element1 = Element("hola", 1)
element2 = Element("hola2", 0)
element3 = Element("hola3", 300)
instance.enqueue(element1)
instance.enqueue(element2)
instance.enqueue(element3)
instance.show_values()
instance.show_priorities()