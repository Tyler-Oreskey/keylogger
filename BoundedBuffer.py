from threading import Condition

class BoundedBuffer:
    def __init__(self):
        self.max_size = 10
        self.size = 0
        self.cond = Condition()
        self.buffer = []

    def add(self, item):
        self.cond.acquire()

        while(self.is_full()):
            self.cond.wait()
        
        self.buffer.append(item)
        self.size += 1
        self.cond.notify_all()
        self.cond.release()

    def remove(self):
        self.cond.acquire()

        while(self.is_empty()):
            self.cond.wait()
        
        item = self.buffer.pop(0)
        self.size -= 1
        self.cond.notify_all()
        self.cond.release()
        return item

    def is_full(self):
        return self.size == self.max_size
    
    def is_empty(self):
        return self.size == 0