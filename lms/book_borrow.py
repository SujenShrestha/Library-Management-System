import functions
import messages

def books_dictionary():
    """Reads text file contents and puts each line in a list as values of a dictionary
    and assigns auto increasing numbers as keys for each list"""
    file = open("books.txt","r")
    booksInDictionary = {}
    bookID = 0
    for line in file:
        line = line.replace("\n","")
        bookID += 1
        booksInDictionary[bookID] = line.split(",")
    file.close()
    return booksInDictionary

booksDictionary = books_dictionary()

def display():
    """Displays book details in a tabular form"""
    print()
    messages.minus()
    print("Book ID" " \t Book Name" "\t\tAuthor" "\t\t\tQuantity" "\tPrice")
    messages.minus()
    print()
    
    for key, value in booksDictionary.items():
        value = "\t\t".join(value) #Separates each list value in dictionary with 2 tab space
        print("  ", key, "\t\t" , value)
        print()
    messages.minus()
    print()

def borrow_book():
    """Takes Book ID as input from user and gives suitable output according to the input provided
    and writes the details of borrowed books in a text file"""
    borrowLoop = True
    total = 0
    books = []
    while borrowLoop == True:
        try:
            if total == 0:
                print("Press '0' to go back.")
                print()
            b = int(input("Enter the ID of the book you want to borrow: "))
            for key,value in booksDictionary.items():
                if b == key:
                    book = booksDictionary[b][0]
                    quantity = int(booksDictionary[b][2])
                    price = float(booksDictionary[b][3].replace("$",""))
                    if quantity > 0:
                        messages.available()
                        books.append(book)
                        if len(books) == 1:
                            borrower = input("Enter the name of Borrower: ")
                            print("The date of borrow is:", functions.date)
                            print("The time of borrow is:", functions.time)  
                        if len(books) >= 1:
                            print("The price of the book is: " + "$" + str(price))
                            total = total + price
                            
                            #Updates the book's quantity after a book is borrowed
                            file = open("books.txt","w")
                            for values in booksDictionary.values():
                                #Matches the quantity of user input Book ID with quantity value in dictionary;
                                #Reduces the quantity in dictionary by 1
                                if quantity == int(values[2]):
                                    values[2] = int(values[2]) - 1
                                    values[2] = str(values[2])
                                file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "\n")
                            file.close()                            
                            display()                     
                            print("Do you want to borrow another book?")
                            answer = input("If 'Yes' enter 'y'. Press any other key to skip: ").lower()
                            print()
                            if answer != "y":
                                borrowLoop = False
                                customer = "Borrow-" + borrower + "-" + str(functions.unique) + ".txt"
                                
                                #Writes customer details in a text file
                                file = open(customer,"w")
                                file.write("Date: " + functions.date + "\n")
                                file.write("Time: " + functions.time + "\n\n")
                                file.write("Customer's Name: " + borrower + "\n\n")
                                file.write("Books borrowed: " + "\n")
                                for i in range(len(books)):
                                    file.write(books[i] + "\n")
                                file.write("\nTotal price: " + "$" + str(total) + "\n")
                                file.close()

                                #Displays customer borrow details in shell
                                file = open(customer,"r")
                                for line in file:
                                    line = line.replace("\n","")
                                    print(line)
                                messages.plus()
                                file.close()
                                print()

                    else:
                        messages.not_available()
                        
                elif b == 0:
                    print()
                    borrowLoop = False
                    break

                elif b > len(booksDictionary) or b < 0:
                    messages.provide_valid_id()
                    display()
                    break

        except:
            messages.provide_valid_id()
            display()
