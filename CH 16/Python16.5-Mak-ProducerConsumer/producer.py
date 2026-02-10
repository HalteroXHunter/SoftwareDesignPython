import time
from threading import Thread
from random import randint

class Producer:
    def __init__(self, producer_count, turns, 
                 min_sleep_time, max_sleep_time, 
                 queue):
        self._turns = turns
        self._min_sleep_time = min_sleep_time
        self._max_sleep_time = max_sleep_time
        self._queue = queue
        
        self._value = 0
        self._threads = []
        
        for i in range(producer_count):
            self._threads.append(
                Thread(target=self._produce,
                       args=(i + 1,))
            )
    
    def start(self):
        for th in self._threads:
            th.start()
                       
    def finish(self):        
        for th in self._threads:
            th.join()

        self._enter(0, 0, 0)
    
    def _print_spaces(self, thread_id):
        for _ in range(1, thread_id):
            print('           ', end='')
            
    def _produce(self, thread_id):
        for turn in range(self._turns):
            time.sleep(
                    randint(self._min_sleep_time,
                            self._max_sleep_time))
            
            self._value += 1
            self._enter(thread_id, turn, self._value)
            
    def _enter(self, thread_id, turn, value):
        with self._queue.condition:
            while self._queue.is_full():
                self._queue.condition.wait()
        
            self._queue.enter(value)
            
            if thread_id > 0:
                self._print_spaces(thread_id)
                print(f'{value:3d} {self._queue.data}   ')
            
            if turn == self._turns - 1:
                self._print_spaces(thread_id)
                print('   Done!')
            
            if self._queue.just_became_not_empty():
                self._queue.condition.notify()
    