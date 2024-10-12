class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if self.__is_checked_out == True:
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_book(self):
        if self.__is_checked_out == False:
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} is not checked out.")

    def is_checked_out(self):
        return self


class Library:
    def __init__(self):
        self._books = []
    def add_book(self, title):
        self._books.append(title)
    def check_out_book(self, title, author):
        self.title = title
        self.author = author
        if title in self._books:
            self._books.remove(title)
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")
    def return_book(self, title, author):
        self.title = title
        self.author = author
        if title not in self._books:
            self._books.append(title)
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} is not checked out.")
    def list_available_books(self):
        return self._books

