from fiction import Fiction
from fictionattrs import FictionAttrs
from cookbook import Cookbook

class Catalogue:
    def __init__(self):
        self._booklist = []
    
    def add(self, attrs):
        if isinstance(attrs, FictionAttrs): book = Fiction(attrs)
        else:                               book = Cookbook(attrs)
        
        self._booklist.append(book)

    def find_fiction(self, target_attrs):
        return [book for book in self._booklist
                    if (    isinstance(book, Fiction)
                        and book.attributes.is_match(target_attrs))
        ]
    
    def find_cookbook(self, target_attrs):
        return [book for book in self._booklist
                    if (    isinstance(book, Cookbook)
                        and book.attributes.is_match(target_attrs))
        ]
