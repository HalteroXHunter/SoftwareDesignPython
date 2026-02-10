from key import Key
from kind import Kind
from genre import Genre
from region import Region
from subject import Subject

class Attributes:

    @staticmethod
    def _equal_ignore_case(target_str, other_str):
        if len(target_str) == 0: 
            return True
        else:
            return target_str.casefold() == other_str.casefold()

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if key == Key.YEAR:
                assert(isinstance(value, int))
            elif key in [Key.TITLE, Key.LAST, Key.FIRST]:
                assert(isinstance(value, str))
            elif key == Key.KIND:
                assert(isinstance(value, Kind))
            elif key == Key.GENRE:
                assert(isinstance(value, Genre))
            elif key == Key.REGION:
                assert(isinstance(value, Region))
            elif key == Key.SUBJECT:
                assert(isinstance(value, Subject))

        self._dictionary = dictionary
    
    def _is_matching_key_value(self, target_key, target_value):
        if target_key not in self._dictionary.keys(): return False
        if self._dictionary[target_key] == target_value: return True

        if isinstance(target_value, str):
            return Attributes._equal_ignore_case(
                self._dictionary[target_key], target_value)
            
        return False
                       
    def is_match(self, target_attrs):
        for target_key, target_value \
                            in target_attrs._dictionary.items():
            if not self._is_matching_key_value(target_key, 
                                               target_value):
                return False
            
        return True
            
    def __str__(self):
        last_key = list(self._dictionary.keys())[-1]
        ostr = '{'
        
        for key, value in self._dictionary.items():
            ostr += str(key.name) + ': '
            
            if isinstance(value, str):
                ostr += "'" + value + "'"
            else:
                ostr += str(value)
                
            if key != last_key: ostr += ', '
                
        ostr += '}'
        return ostr
    