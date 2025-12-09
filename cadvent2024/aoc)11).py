stones = """4610211 4 0 59 3907 201586 929 33750""".replace("\n"," ")

class noed:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class solver:
    def __init__(self):
        self.stones = [int(x) for x in stones.split(" ")]
        self.head = None
        self.initlink()
        self.solves = {}
        print("start")
        for i in range(0,75):
            pointer = self.head
            while pointer:
                if pointer.data in self.solves:
                    before = self.insert_before_node(pointer,self.solves[pointer.data][0])
                    after = self.insert_after_node(pointer,self.solves[pointer.data][1])
                    before.next = after
                    after.prev = before
                    pointer = after
                elif pointer.data == 0: # rule 1
                    pointer.data = 1
                elif len(str(pointer.data)) % 2 == 0: # rule 2
                    # split into 2
                    stringdata = str(pointer.data)
                    firstpart, secondpart = stringdata[:len(stringdata)//2], stringdata[len(stringdata)//2:]
                    before = self.insert_before_node(pointer,int(firstpart))
                    after = self.insert_after_node(pointer,int(secondpart))
                    #dereference current pointer as its split into 2 now
                    before.next = after
                    after.prev = before
                    pointer = after
                    self.solves[pointer.data] = [firstpart,secondpart]
                else: # rule 3
                    pointer.data *= 2024
                    self.solves[pointer.data] = [pointer.data * 2024]
                pointer = pointer.next #traverse
            
            print("blink",i)
        self.count()
            
    def count(self):
        total = 0
        current = self.head
        while current:
            total += 1
            current = current.next
        print(total)
        
    def initlink(self):
        self.head = noed(self.stones[0])
        del self.stones[0]
        
        for x in self.stones:
            self.insert_after_node(self.head,x)
            
    def insert_after_node(self, node, data):
        if node is None:
            print("Error: The given node is None")
            return
    
        new_node = noed(data)
        new_node.prev = node
        new_node.next = node.next
    
        if node.next:
            node.next.prev = new_node
    
        node.next = new_node
        return new_node
        
    def insert_before_node(self, node, data):
        if node is None:
            print("Error: The given node is None")
            return
    
        new_node = noed(data)
        new_node.next = node
        new_node.prev = node.prev
    
        if node.prev:
            node.prev.next = new_node
        else:
            # Node is the head, so update the head pointer
            self.head = new_node
    
        node.prev = new_node
        return new_node

    def display(self, head):
        current = head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
            

solver()
        
        
        
        
        
        