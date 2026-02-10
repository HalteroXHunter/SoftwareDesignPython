import random
import numpy as np
from averages import SampleAverages

SIZE = 10_000_000
STRIDES = (1, 50, 100, 1000, 10_000)

if __name__ == '__main__':
    random.seed(0)
    lst = [random.randint(1, 5) for _ in range(SIZE)]
    
    for_loop_label     = 'for loop'
    list_stride_label  = 'list stride'
    tuple_stride_label = 'tuple stride'
    array_stride_label = 'ndarray stride'
    
    elapsed_time_for_loop = \
        SampleAverages.do_calculations(
            lst, STRIDES,
            SampleAverages.use_for_loop, 
            for_loop_label)
        
    elapsed_time_list_stride = \
        SampleAverages.do_calculations(
            lst, STRIDES,
            SampleAverages.use_stride, 
            list_stride_label,
            other_label=for_loop_label,
            other_et=elapsed_time_for_loop)
    
    tpl = tuple(lst)
    
    elapsed_time_tuple_stride = \
        SampleAverages.do_calculations(
            tpl, STRIDES,
            SampleAverages.use_stride, 
            tuple_stride_label,
            other_label=list_stride_label,
            other_et=elapsed_time_list_stride)
    
    arr = np.array(lst)
    
    elapsed_time_array_stride = \
        SampleAverages.do_calculations(
            arr, STRIDES,
            SampleAverages.use_numpy, 
            array_stride_label,
            other_label=tuple_stride_label,
            other_et=elapsed_time_tuple_stride)
        
    overall = ( (elapsed_time_for_loop - elapsed_time_array_stride)
                /elapsed_time_for_loop
              )
    print(f'Overall improvement: {overall:4.1%}')
