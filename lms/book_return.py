import messages
import functions
import book_borrow
import glob

def return_book():
    """Takes the borrower's name as input from user and returns the total amount to be paid as well as updates the stock of books"""
    returnLoop = True
    while returnLoop == True:
        try:
            name = input("Enter the name of customer: ")
            
            #Searches for the file names that start with the given parameters
            customer = (glob.glob("Borrow-" + name + "-*"))
            if len(customer) == 1:
                returner = customer[0]
            elif len(customer) > 1:
                idLoop = True
                while idLoop == True:
                    try:
                        print()
                        messages.minus()
                        print("Customer ID\t\t" + "Filename")
                        messages.minus()
                        print()
                        
                        #Displays all the files having same customer name
                        for i in range (len(customer)):
                            n = i + 1
                            print("    " + str(n) + "\t\t" + customer[i])
                            print()
                        messages.minus()
                        print()
                        c = int(input("Select the ID of the customer who wants to return: "))
                        
                        if c > len(customer) or c < 1:
                            messages.provide_valid_id()
                        else:
                            r = c - 1 #Subtracts the input by 1 to match the index number
                            returner = customer[r]
                            idLoop = False
                    except:
                        messages.provide_valid_id()
                        
            #Displays the previously borrowed information of the customer
            books = [] #Stores all the borrow informaiton from text file of the customer
            file = open(returner,"r")
            print()
            print("Borrow Details: ")
            print()
            lines = file.readlines()
            for line in lines:
                line = line.replace("\n","")
                books.append(line)
                print(line)
            print()
            file.close()
                
            returned = "Return-" + name + "-" + str(functions.unique) + ".txt"

            #Creates a text file with the customer's information of the returned books
            file = open(returned,"w")
            file.write("Date: " + functions.date + "\n")
            file.write("Time: " + functions.time + "\n\n")
            file.write("Returned By: " + name + "\n\n")
            file.write("Books returned: " + "\n")
            for i in range(6, len(books)):
                file.write(books[i] + "\n")
            from datetime import datetime
            from datetime import timedelta
            borrowDate = []
            borrowDate.append(books[0].replace("Date: ",""))#Extracts time from borrow file
                
            #Converts the date & time from string format to date & time fromat
            startDate = datetime.strptime(borrowDate[0], "%d-%m-%Y")
            dateToday = datetime.strptime(functions.date, "%d-%m-%Y")
            
            endDate = startDate + timedelta(days=10)#Adds 10 days to borrow date
            if dateToday > endDate:
                days = (dateToday - endDate).days
                fine = 0.25 * days
                total = float(books[9].replace("Total price: $",""))
                grand = fine + total
                file.write("Fine:\t     "+ "$" + str(fine) + "\n")
                file.write("Grand Total: " + "$" + str(grand) + "\n\n")
                print("The book is returned " + str(days) + " days late")
                print()
            file.close()
            
            #Displays the customer information about the returned books
            file = open(returned,"r")
            messages.plus()
            print("\t\t\t\tThe book has been returned")
            messages.plus()
            print()
            for line in file:
                line = line.replace("\n","")
                print(line)
            messages.plus()
            file.close()
            print()
                                    
            #Updates the stock after books are returned
            for i in range(6,len(books)-2):
                file = open("books.txt","w")
                for values in book_borrow.booksDictionary.values():
                    if books[i] == values[0]:
                        values[2] = int(values[2]) + 1
                        values[2] = str(values[2])
                    file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "\n")
                file.close()
            returnLoop = False

        except:
            print()
            messages.plus()
            print("\t\t\t    The borrower's name is incorrect")
            messages.plus()
            print()
