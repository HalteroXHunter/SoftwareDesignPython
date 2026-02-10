class SortedList:

    @staticmethod
    def merge(list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        
        merged = []
        i1 = i2 = 0
        
        while (i1 < len1) and (i2 < len2):
            if list1[i1] <= list2[i2]:
                merged.append(list1[i1])
                i1 += 1
            else:
                merged.append(list2[i2])
                i2 += 1
                
        if i1 < len1:
            merged += list1[i1:]
        elif i2 < len2:
            merged += list2[i2:]

        i = 0
        while i < len(merged):
            j = i + 1
            
            while j < len(merged):
                if merged[i] == merged[j]:
                    merged.pop(j)
                else:
                    j += 1
                    
            i += 1
            
        return merged 
