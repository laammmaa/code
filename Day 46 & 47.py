class library:
    def __init__(self, shelf, book):
        self.shelf = shelf
        self.book = book


class ScienceSection(library):
    def __init__(self, shelf, book, name):
        super().__init__(shelf, book)
        self.name = name

    def book1(self):
        print("Number of shelf:", self.shelf, "\n Number of books:", self.book, "\n Name of book: ", self.name)


x = ScienceSection(45, 300, "Physics books")
x.book1()
print("After changing the number of shelf and book in child class:")
x.book = 20
x.shelf = 4
x.book1()
