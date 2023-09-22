from threading import Thread
from threading import current_thread

class Consumer(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.setName("Consumer thread")
        self.buffer = buffer

    def run(self):
        total = 0

        for i in range(50):
            d = self.buffer.remove()
            total += d
            print("{0} consumed {1} items\n".format(current_thread().name, total), flush=True)