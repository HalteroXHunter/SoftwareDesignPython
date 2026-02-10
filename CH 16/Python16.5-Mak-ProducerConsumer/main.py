from bounded_queue import BoundedQueue
from producer import Producer
from consumer import Consumer

QUEUE_CAPACITY = 8;

PRODUCER_COUNT = 2;
PRODUCER_TURNS = 5;
MIN_PRODUCER_SLEEP_TIME = 2;
MAX_PRODUCER_SLEEP_TIME = 4;

CONSUMER_COUNT = 3;
MIN_CONSUMER_SLEEP_TIME = 3;
MAX_CONSUMER_SLEEP_TIME = 5;

if __name__ == '__main__':
    for i in range(PRODUCER_COUNT):
        print(f'Producer#{i + 1} ', end='')
    for i in range(CONSUMER_COUNT):
        print(f'Consumer#{i + 1} ', end='')
    print()
    
    queue = BoundedQueue(QUEUE_CAPACITY)
    
    producer = Producer(PRODUCER_COUNT,
                        PRODUCER_TURNS,
                        MIN_PRODUCER_SLEEP_TIME,
                        MIN_PRODUCER_SLEEP_TIME,
                        queue)
    
    consumer = Consumer(PRODUCER_COUNT,
                        CONSUMER_COUNT, 
                        MIN_CONSUMER_SLEEP_TIME,
                        MAX_CONSUMER_SLEEP_TIME,
                        queue)
    
    producer.start()
    consumer.start()
    
    producer.finish()
    consumer.finish()
    
    print()
    print('Program done!')
