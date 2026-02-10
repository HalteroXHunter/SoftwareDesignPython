from attributes import Genre
from attributes import Attributes
from catalogue import Catalogue

def fill(catalogue):
    catalogue.add(Attributes("Life of Pi", 
                             "Martel", "Yann",
                             2003, Genre.ADVENTURE))
    catalogue.add(Attributes("The Call of the Wild",
                             "London", "Jack",
                             1903, Genre.ADVENTURE))

    catalogue.add(Attributes("To Kill a Mockingbird", 
                             "Lee", "Harper",
                             1960, Genre.CLASSICS))
    catalogue.add(Attributes("Little Women", 
                             "Alcott", "Louisa",
                             1868, Genre.CLASSICS))

    catalogue.add(Attributes("The Adventures of Sherlock Holmes", 
                             "Doyle", "Conan",
                             1892, Genre.DETECTIVE))
    catalogue.add(Attributes("And Then There Were None", 
                             "Christie", "Agatha",
                             1939, Genre.DETECTIVE))

    catalogue.add(Attributes("Carrie", 
                             "King", "Stephen",
                             1974, Genre.HORROR))
    catalogue.add(Attributes("It: A Novel", 
                             "King", "Stephen",
                             1986, Genre.HORROR))
    catalogue.add(Attributes("Frankenstein",
                             "Shelley", "Mary",
                             1818, Genre.HORROR))

    catalogue.add(Attributes("2001: A Space Odyssey", 
                             "Clarke", "Arthur",
                             1968, Genre.SCIFI))
    catalogue.add(Attributes("Ender's Game", 
                             "Card", "Orson",
                             1985, Genre.SCIFI))

def search(catalogue, target_attrs):
    print()
    print("Find ", end="")
    print(target_attrs)
    
    matches = catalogue.find(target_attrs)
    
    if len(matches) == 0:
        print("No matches.")
    else:
        print("Matches:")
        
        for book in matches:
            print("  ", end="")
            print(book.attributes)

def test(catalogue):
    target_attrs = Attributes("Life of Pi", "Martel", "Yann", 
                              2003, Genre.ADVENTURE)
    search(catalogue, target_attrs)

    target_attrs = Attributes("", "King", "", 0, Genre.HORROR)
    search(catalogue, target_attrs)

    target_attrs = Attributes("1984", "Orwell", "George", 
                              0, Genre.CLASSICS)
    search(catalogue, target_attrs)

    target_attrs = Attributes("", "", "", 1960, Genre.ROMANCE)
    search(catalogue, target_attrs)

    target_attrs = Attributes("", "", "", 1960, Genre.UNSPECIFIED)
    search(catalogue, target_attrs)

    target_attrs = Attributes("", "", "", 0, Genre.SCIFI)
    search(catalogue, target_attrs)

    target_attrs = Attributes("", "", "", 0, Genre.UNSPECIFIED)
    search(catalogue, target_attrs)

if __name__ == '__main__':
    catalogue = Catalogue()
    fill(catalogue)
    test(catalogue)
