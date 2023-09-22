from BoundedBuffer import BoundedBuffer
from Consumer import Consumer
from Producer import Producer

def main():
    buffer = BoundedBuffer()
    consumer_thread = Consumer(buffer)
    producer_thread = Producer(buffer)

    consumer_thread.start()
    producer_thread.start()

    producer_thread.join()
    consumer_thread.join()
    

if __name__ == "__main__":
    main()