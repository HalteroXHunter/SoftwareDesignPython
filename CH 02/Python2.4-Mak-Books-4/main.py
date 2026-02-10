from key import Key
from kind import Kind
from genre import Genre
from region import Region
from subject import Subject
from attributes import  Attributes
from catalogue import Catalogue

def fill(catalogue):
    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "Life of Pi",
        Key.LAST:  "Martel",
        Key.FIRST: "Yann",
        Key.YEAR:  2003,
        Key.GENRE: Genre.ADVENTURE
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "The Call of the Wild",
        Key.LAST:  "London",
        Key.FIRST: "Jack",
        Key.YEAR:  1903,
        Key.GENRE: Genre.ADVENTURE
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "To Kill a Mockingbird",
        Key.LAST:  "Lee",
        Key.FIRST: "Harper",
        Key.YEAR:  1960,
        Key.GENRE: Genre.CLASSICS
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "Little Women",
        Key.LAST:  "Alcott",
        Key.FIRST: "Louisa",
        Key.YEAR:  1868,
        Key.GENRE: Genre.CLASSICS
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "The Adventures of Sherlock Holmes",
        Key.LAST:  "Doyle",
        Key.FIRST: "Conan",
        Key.YEAR:  1892,
        Key.GENRE: Genre.DETECTIVE
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "And Then There Were None",
        Key.LAST:  "Christie",
        Key.FIRST: "Agatha",
        Key.YEAR:  1939,
        Key.GENRE: Genre.DETECTIVE
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "Carrie",
        Key.LAST:  "King",
        Key.FIRST: "Stephen",
        Key.YEAR:  1974,
        Key.GENRE: Genre.HORROR
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "It: A Novel",
        Key.LAST:  "King",
        Key.FIRST: "Stephen",
        Key.YEAR:  1986,
        Key.GENRE: Genre.HORROR
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "Frankenstein",
        Key.LAST:  "Shelley",
        Key.FIRST: "Mary",
        Key.YEAR:  1818,
        Key.GENRE: Genre.HORROR
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "2001: A Space Odyssey",
        Key.LAST:  "Clarke",
        Key.FIRST: "Arthur",
        Key.YEAR:  1968,
        Key.GENRE: Genre.SCIFI
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "Ender's Game",
        Key.LAST:  "Card",
        Key.FIRST: "Orson",
        Key.YEAR:  1985,
        Key.GENRE: Genre.SCIFI
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "The Wok of Life",
        Key.LAST:  "Leung",
        Key.FIRST: "Bill",
        Key.REGION: Region.China
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Chinese Cooking for Dummies",
        Key.LAST:  "Yan",
        Key.FIRST: "Martin",
        Key.REGION: Region.China
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Mastering the Art of French Cooking",
        Key.LAST:  "Child",
        Key.FIRST: "Julia",
        Key.REGION: Region.France
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Vegetarian India",
        Key.LAST:  "Jaffrey",
        Key.FIRST: "Madhur",
        Key.REGION: Region.India
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Made in India",
        Key.LAST:  "Sodha",
        Key.FIRST: "Meera",
        Key.REGION: Region.India
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Essentials of Classic Italian Cooking",
        Key.LAST:  "Hazan",
        Key.FIRST: "Marcella",
        Key.REGION: Region.Italy
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "The Complete Italian Cookbook",
        Key.LAST:  "Mazzocco",
        Key.FIRST: "Manuela",
        Key.REGION: Region.Italy
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Food for Life",
        Key.LAST:  "Batmanglij",
        Key.FIRST: "Najmieh",
        Key.REGION: Region.Persia
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "The New Orleans Kitchen",
        Key.LAST:  "Devillier",
        Key.FIRST: "Justin",
        Key.REGION: Region.US
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.TITLE: "Rodney Scott's World of BBQ",
        Key.LAST:  "Scott",
        Key.FIRST: "Rodney",
        Key.REGION: Region.US
    }
    catalogue.add(Attributes(attrs))

    attrs = {
        Key.KIND:  Kind.HOWTO,
        Key.TITLE: "On Writing: A Memoir of the Craft",
        Key.LAST:  "King",
        Key.FIRST: "Stephen",
        Key.SUBJECT: Subject.WRITING
    }
    catalogue.add(Attributes(attrs))

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
    target_attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "Life of Pi",
        Key.LAST:  "Martel",
        Key.FIRST: "Yann",
        Key.YEAR:  2003,
        Key.GENRE: Genre.ADVENTURE
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.FICTION,
        Key.LAST:  "KING",
        Key.GENRE: Genre.HORROR
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.FICTION,
        Key.TITLE: "1984",
        Key.LAST:  "Orwell",
        Key.FIRST: "George",
        Key.GENRE: Genre.CLASSICS
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.FICTION,
        Key.YEAR:  1960,
        Key.GENRE: Genre.ROMANCE
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.FICTION,
        Key.YEAR:  1960
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.FICTION,
        Key.GENRE: Genre.SCIFI
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.FICTION
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:   Kind.COOKBOOK,
        Key.TITLE:  "Mastering the Art of French Cooking",
        Key.LAST:   "Child",
        Key.FIRST:  "Julia",
        Key.REGION: Region.France
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.REGION: Region.China
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:   Kind.COOKBOOK,
        Key.LAST:   "Leung",
        Key.REGION: Region.Mexico
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.KIND:  Kind.COOKBOOK,
        Key.LAST:  "Scott",
        Key.FIRST: "Rodney"
    }
    search(catalogue, Attributes(target_attrs))

    target_attrs = {
        Key.LAST: "King"
    }
    search(catalogue, Attributes(target_attrs))

if __name__ == '__main__':
    catalogue = Catalogue()
    fill(catalogue)
    test(catalogue)
