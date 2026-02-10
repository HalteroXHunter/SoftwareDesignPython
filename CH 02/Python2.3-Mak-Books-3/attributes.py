class Attributes:

    @staticmethod
    def _equal_ignore_case(target_str, other_str):
        if len(target_str) == 0: 
            return True
        else:
            return target_str.casefold() == other_str.casefold()

    def __init__(self, title, last, first):
        self.__title = title
        self.__last  = last
        self.__first = first
        
    @property
    def title(self): return self.__title
        
    @property
    def last(self): return self.__last
    
    @property
    def first(self): return self.__first
    
    def is_match(self, target_attrs):
        return (     
                Attributes._equal_ignore_case(target_attrs.title, 
                                              self.__title)
            and Attributes._equal_ignore_case(target_attrs.last,  
                                              self.__last)
            and Attributes._equal_ignore_case(target_attrs.first, 
                                              self.__first)
        )
    
    def __str__(self):
        return (f"TITLE: '{self.__title}'"
                f", LAST: '{self.__last}'" 
                f", FIRST: '{self.__first}'")
