from fictionattrs  import FictionAttrs, Genre
from cookbookattrs import CookbookAttrs, Region
from catalogue     import Catalogue

def fill(catalogue):
    catalogue.add(FictionAttrs("Life of Pi", 
                               "Martel", "Yann",
                               2003, Genre.ADVENTURE))
    catalogue.add(FictionAttrs("The Call of the Wild", 
                               "London", "Jack",
                               1903, Genre.ADVENTURE))

    catalogue.add(FictionAttrs("To Kill a Mockingbird", 
                               "Lee", "Harper",
                               1960, Genre.CLASSICS))
    catalogue.add(FictionAttrs("Little Women", 
                               "Alcott", "Louisa",
                               1868, Genre.CLASSICS))

    catalogue.add(FictionAttrs("The Adventures of Sherlock Holmes", 
                               "Doyle", "Conan",
                               1892, Genre.DETECTIVE))
    catalogue.add(FictionAttrs("And Then There Were None", 
                               "Christie", "Agatha",
                               1939, Genre.DETECTIVE))

    catalogue.add(FictionAttrs("Carrie",
                               "King", "Stephen",
                               1974, Genre.HORROR))
    catalogue.add(FictionAttrs("It: A Novel", 
                               "King", "Stephen",
                               1986, Genre.HORROR))
    catalogue.add(FictionAttrs("Frankenstein", 
                               "Shelley", "Mary",
                               1818, Genre.HORROR))

    catalogue.add(FictionAttrs("2001: A Space Odyssey", 
                               "Clarke", "Arthur",
                               1968, Genre.SCIFI))
    catalogue.add(FictionAttrs("Ender's Game", 
                               "Card", "Orson",
                               1985, Genre.SCIFI))

    catalogue.add(CookbookAttrs("The Woks of Life",
                                "Leung", "Bill", 
                                Region.China))
    catalogue.add(CookbookAttrs("Chinese Cooking for Dummies",
                                "Yan", "Martin", 
                                Region.China))

    catalogue.add(CookbookAttrs("Mastering the Art of French Cooking",
                                "Child", "Julia", 
                                Region.France))

    catalogue.add(CookbookAttrs("Vegetarian India",
                                "Jaffrey", "Madhur", 
                                Region.India))
    catalogue.add(CookbookAttrs("Made in India",
                                "Sodha", "Meera", 
                                Region.India))

    catalogue.add(CookbookAttrs("Essentials of Classic Italian Cooking",
                                "Hazan", "Marcella", 
                                Region.Italy))
    catalogue.add(CookbookAttrs("The Complete Italian Cookbook",
                                "Mazzocco", "Manuela", 
                                Region.Italy))

    catalogue.add(CookbookAttrs("The Mexican Home Kitchen",
                                "Martinez", "Mely",
                                Region.Mexico))

    catalogue.add(CookbookAttrs("The New Orleans Kitchen",
                                "Devillier", "Justin", 
                                Region.US))
    catalogue.add(CookbookAttrs("Rodney Scott's World of BBQ",
                                "Scott", "Rodney", Region.US))

def search_fiction(catalogue, target_attrs):
    print()
    print("Find ", end="")
    print(target_attrs)

    matches = catalogue.find_fiction(target_attrs)

    if len(matches) == 0:
        print("No matches.")
    else:
        print("Matches:")

        for book in matches:
            print("  ", end="")
            print(book.attributes)

def search_cookbook(catalogue, target_attrs):
    print()
    print("Find ", end="")
    print(target_attrs)

    matches = catalogue.find_cookbook(target_attrs)

    if len(matches) == 0:
        print("No matches.")
    else:
        print("Matches:")

        for book in matches:
            print("  ", end="")
            print(book.attributes)

def test(catalogue):
    target_attrs = FictionAttrs("Life of Pi", "Martel", "Yann", 
                                2003, Genre.ADVENTURE)
    search_fiction(catalogue, target_attrs)

    target_attrs = FictionAttrs("", "King", "", 
                                0, Genre.HORROR)
    search_fiction(catalogue, target_attrs)

    target_attrs = FictionAttrs("1984", "Orwell", "George", 
                                0, Genre.CLASSICS)
    search_fiction(catalogue, target_attrs)

    target_attrs = FictionAttrs("", "", "", 
                                1960, Genre.ROMANCE)
    search_fiction(catalogue, target_attrs)

    target_attrs = FictionAttrs("", "", "", 
                                1960, Genre.UNSPECIFIED)
    search_fiction(catalogue, target_attrs)

    target_attrs = FictionAttrs("", "", "", 
                                0, Genre.SCIFI)
    search_fiction(catalogue, target_attrs)

    target_attrs = FictionAttrs("", "", "", 
                                0, Genre.UNSPECIFIED)
    search_fiction(catalogue, target_attrs)

    target_attrs = CookbookAttrs(
                        "Mastering the Art of French Cooking",
                        "Child", "Julia", Region.France)
    search_cookbook(catalogue, target_attrs)

    target_attrs = CookbookAttrs("", "", "", Region.China)
    search_cookbook(catalogue, target_attrs)

    target_attrs = CookbookAttrs("", "Hom", "", Region.Mexico)
    search_cookbook(catalogue, target_attrs)

    target_attrs = CookbookAttrs("", "Scott", "Rodney", 
                                 Region.UNSPECIFIED)
    search_cookbook(catalogue, target_attrs)


if __name__ == '__main__':
    catalogue = Catalogue()
    fill(catalogue)
    test(catalogue)
