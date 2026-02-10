import numpy as np
from time import perf_counter

class SampleAverages:

    @staticmethod
    def use_for_loop(values, stride):
        count = 0
        total = 0
        
        for i in range(int(len(values)/stride)):
            count += 1
            total += values[i*stride]
            
        return total/count
    
    @staticmethod
    def use_stride(values, stride):
        selection = values[::stride]
        count = len(selection)
        
        return sum(selection)/count
    
    @staticmethod
    def use_numpy(values, stride):
        selection = values[::stride]    
        
        return np.mean(selection)
    
    @staticmethod
    def do_calculations(sequence, strides, avgs_function, label, 
                        other_label=None, other_et=None):
        avgs = []
        
        start_time = perf_counter()
        for stride in strides:
            avgs.append(avgs_function(sequence, stride))
            
        et = perf_counter() - start_time
    
        print(f'{label} elapsed time = {et:6.4f} seconds')
        print(f'{avgs = }')
        print()
        
        if other_et is not None:
            improvement = (other_et - et)/other_et
            print(f'Improvement of {label} over {other_label}: '
                  f'{improvement:4.1%}')
            print()
            
        return et
