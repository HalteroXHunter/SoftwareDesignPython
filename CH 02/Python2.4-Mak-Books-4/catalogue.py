from book import Book

class Catalogue:
    def __init__(self):
        self._booklist = []
    
    def add(self, attrs):
        book = Book(attrs)
        self._booklist.append(book)
        
    def find(self, target_attrs):
        return [book for book in self._booklist
                    if book.attributes.is_match(target_attrs)
               ]
