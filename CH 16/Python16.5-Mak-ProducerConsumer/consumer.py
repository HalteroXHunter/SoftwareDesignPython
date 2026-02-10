import time
from threading import Thread
from random import randint

class Consumer:
    def __init__(self, producer_count, consumer_count,
                 min_sleep_time, max_sleep_time, 
                 queue):
        self._producer_count = producer_count
        self._min_sleep_time = min_sleep_time
        self._max_sleep_time = max_sleep_time
        self._queue = queue
        
        self._threads = []
        
        for i in range(consumer_count):
            self._threads.append(
                Thread(target=self._consume,
                       args=(i + 1,))
            )
    
    def start(self):
        for th in self._threads:
            th.start()
    
    def finish(self):
        for th in self._threads:
            th.join()
    
    def _print_spaces(self, thread_id):
        k = self._producer_count + thread_id
        for _ in range(1, k):
            print('           ', end='')

    def _consume(self, thread_id):
        keep_consuming = True
        
        while keep_consuming:
            time.sleep(
                randint(self._min_sleep_time,
                        self._max_sleep_time))
        
            with self._queue.condition:
                while self._queue.is_empty():
                    self._queue.condition.wait()
                
                value = self._queue.peek()
                if value > 0:
                    self._queue.remove()
                
                self._print_spaces(thread_id)
                print(f'{-value:4d} {self._queue.data} ')

                if self._queue.just_became_not_full():
                    self._queue.condition.notify()
                    
                if value == 0:
                    keep_consuming = False
                    self._print_spaces(thread_id)
                    print('   Done!')
