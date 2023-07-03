import csv
from os import path
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime, timedelta


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    receipt_dic = {}
    fileName = path.join(path.dirname(__file__), filename)

    with open(fileName, "rt") as receipt_list:
        # read the csv file
        reader = csv.reader(receipt_list)

        # skip a line in the file
        next(reader)

        # iterate in the file
        for element in reader:
            if len(element) != 0:
                # define the key of the dic and store it to a variable
                key = element[key_column_index]

                # define the value of the dictionary
                receipt_dic[key] = element

    return receipt_dic


def main():
    """Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
    Prints the products_dict. Opens the request.csv file for reading.
    Skips the first line of the request.csv file because the first line contains column headings.
    Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop,
    your program must do the following for each row
    Print the product name, requested quantity, and product price.
    """
    # define key_column_index  to 0
    key_column_index = 0
    current_date = datetime.now()

    try:
        # call the read_dictionary funtion and store it to a variable
        product_dict = read_dictionary("products.csv", key_column_index)

        # Print all the products in the product dictionary
        # print("All products:\n", product_dict)
        
        print()

        filename = path.join(path.dirname(__file__), "request.csv")
        
        
        #Opens the request.csv file for reading.
        with open(filename, "rt") as request_list:
            print("Inkom Emporium")
            print()

            reader = csv.reader(request_list)
            #Skips the first line of the request.csv
            next(reader)

            num_items = 0
            subtotal = 0
            total_discount = 0
            for each_row in reader:
                # get the product # number in the request file.
                product_num = each_row[0]
                # get the quantity of the product in the request file.
                product_quantity = each_row[1]

                # get the product name in the products file
                product_name = product_dict[product_num][1]

                # get the product price in the products file.
                product_price = float(product_dict[product_num][2])
                if current_date.weekday() == 1 or current_date.weekday() == 2:
                    discount  = product_price * 0.1
                    product_price -= discount
                    total_discount += discount
                if current_date.hour < 11 :
                    discount  = product_price * 0.1
                    product_price -= discount
                    total_discount += discount
                elif current_date.hour <= 11 and current_date.minute == 00 :
                    discount  = product_price * 0.1
                    product_price -= discount
                    total_discount += discount

                
                num_items += int(product_quantity)
                subtotal += float(product_price) * int(product_quantity) 
                
                # print the name, price and quantity of the product requested.
                print(f"{product_name}:{product_quantity} @ {product_price }")

            tax_rate = subtotal * 0.06
            Total = subtotal + tax_rate

            # Call the now() method to get the current
            # date and time as a datetime object from
            # the computer's operating system.
            print()
            print(f"Number of Items: {num_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Total Discount: {total_discount:.2f}")
            print(f"Sales Taxes: {tax_rate:.2f}")
            print(f"Total: {Total:.2f}")

            print()
            print("Thank you for shopping at the Inkom Emporium.")
            
            # Use an f-string to print the current
            # day of the week and the current time.
            print(f"{current_date:%a %b  %d %T %Y }")
    except FileNotFoundError as not_found_err:
        print()
        print("Error: missing file")
        print(not_found_err)
    except PermissionError as not_authorized:
        print()
        print("Access denied")
        print(not_authorized)
    except KeyError as key_err:
        print()
        print("Error: unknown product ID in the request.csv file")
        print(type(key_err).__name__, key_err ) 
    except IndexError as index_err:
        print(index_err)

if __name__ == "__main__":
    main()
