import messages
import functions
import book_borrow
import book_return

def selection_message():
    """Displays the number of actions that can be performed in the program"""
    continueLoop = True
    while continueLoop == True:
        try:
            book_borrow.display()
            print()
            print("Enter '1' to borrow a book")
            print("Enter '2' to return a book")
            print("Enter '3' to exit")
            value = int(input("Please enter a value: "))
            print()

            if value == 1:
                book_borrow.borrow_book()

            elif value == 2:
                book_return.return_book()

            elif value == 3:
                continueLoop = False
                messages.exit_library()

            else:
                messages.invalid_input()

        except:
            messages.invalid_input()

messages.title()
selection_message()
