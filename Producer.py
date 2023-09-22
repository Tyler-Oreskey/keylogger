from threading import Thread
from threading import current_thread

class Producer(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.setName("Producer thread")
        self.buffer = buffer

    def run(self):
        total = 0

        for i in range(50):
            self.buffer.add(1)
            total += 1
            print("{0} produced {1} items\n".format(current_thread().name, total), flush=True)