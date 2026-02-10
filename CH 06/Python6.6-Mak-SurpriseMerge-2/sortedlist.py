class SortedList:

    @staticmethod
    def merge_and_deduplicate(list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        
        merged = []
        i1 = i2 = 0
                
        while (i1 < len1) or (i2 < len2):
            if (     (i1 < len1)
                 and ((i2 == len2) or (list1[i1] <= list2[i2]))):
                
                if (len(merged) == 0) or (list1[i1] != merged[-1]):
                    merged.append(list1[i1])
                i1 += 1
            else:
                if (len(merged) == 0) or (list2[i2] != merged[-1]):
                    merged.append(list2[i2])
                i2 += 1

        return merged 
