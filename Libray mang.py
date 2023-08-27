class Library:

    @staticmethod
    def menu():
        print("**_ WELCOME TO THE LIBRARY _**")
        print("1. Print book list.")
        print("2. Borrow a book.")
        print("3. Add a book.")
        print("4. Return the no. of books in library.")
        print("5. Exit library.")
        print("Enter your choice using (1, 2, 3, 4, 5) :")

    booklist = ["Quran","Rich Dad Poor Dad", "The Alchemist", "Atomic Habits",
                "Abye hyat", "peery kamil", "namal",  "namal"]

    def printBookList(self):
        for counter, book in enumerate(self.booklist):
            print(counter, book)

    def borrowBook(self, index: int):
        self.index = index
        print(f"You have borrowed {self.booklist[index]}.")
        for book in self.booklist:
            print(book)

    def addBook(self, addedBook: str):
        self.addedBook = addedBook
        self.booklist.append(addedBook)
        print("The updated booklist contains these books: ")
        for book in self.booklist:
            print(book)

    @property
    def no_of_books(self):
        print(f"There are {len(self.booklist)} books in this library.")

    def getChoice(self, choice: int):
        self.choice = choice
        if choice == 1:
            self.printBookList()
            print()
            self.menu()
            self.getChoice(int(input()))
        elif choice == 2:
            self.borrowBook(
                int(input("Enter the index of the book you want to borrow: ")))
            print()
            self.menu()
            self.getChoice(int(input()))
        elif choice == 3:
            self.addBook(input("Enter the name of the book you want to add: "))
            print()
            self.menu()
            self.getChoice(int(input()))
        elif choice == 4:
            self.no_of_books
            print()
            self.menu()
            self.getChoice(int(input()))
        elif choice == 5:
            quit()
        else:
            raise Exception("Something went wrong!")


library = Library()

if __name__ == "__main__":
    library.menu()
    library.getChoice(int(input()))
