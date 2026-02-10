class Quicksort:
    def __init__(self, data):
        self._data = data
        
    def _swap_values_at(self, index1, index2):
        self._data[index1], self._data[index2] = \
            self._data[index2], self._data[index1]
        
    def _partition(self, left_index, right_index):
        middle_index = (left_index + right_index)//2
        pivot_element = self._data[middle_index]
        
        self._swap_values_at(middle_index, right_index)
        
        i = left_index - 1
        j = right_index
        
        while i < j:
            i += 1
            while (    (i < right_index)
                   and (self._data[i] <= pivot_element)):
                i += 1
                
            j -= 1
            while (    (j >= left_index)
                   and (self._data[j] > pivot_element)):
                j -= 1
            
            if i < j:   
                self._swap_values_at(i, j)
                
        self._swap_values_at(i, right_index)
        return i
        
    def sort(self):
        self._sort(0, len(self._data) - 1)
        
    def _sort(self, left_index, right_index):
        partition_size = right_index - left_index + 1
        
        if partition_size < 2:
            return
        elif partition_size == 2:
            if (  self._data[left_index] 
                > self._data[right_index]):
                self._swap_values_at(left_index, 
                                     right_index)
        else:
            pivot_index = self._partition(left_index, 
                                          right_index)
            self._sort(left_index, pivot_index - 1)
            self._sort(pivot_index + 1, right_index)

    def verify_sorted(self):
        for i in range(len(self._data) - 1):
            if self._data[i] > self._data[i+1]:
                return False
            
        return True

        