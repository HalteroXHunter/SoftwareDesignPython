from threading import Thread
from threading import Lock

COUNT = 5

printing_mutex = Lock()

def print_message(msg):    
    for _ in range(COUNT):
        printing_mutex.acquire()
        
        for ch in msg:
            print(ch, end='')
            
        printing_mutex.release()

def test_mt():
    hello_thread = Thread(target=print_message,
                          args=('Hello, world!\n',))
    use_thread = Thread(target=print_message,
                        args=('Use good design!\n',))
    go_thread = Thread(target=print_message,
                       args=('Go multithreaded\n',))
    
    hello_thread.start()
    use_thread.start()
    go_thread.start()
    
    hello_thread.join()
    use_thread.join()
    go_thread.join()

if __name__ == '__main__':
    test_mt()
    
    print()
    print('Done!')
