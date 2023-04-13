import json
import customer as CUS

# read in the JSON text file
# dataIn = r'C:\Users\Henry\Desktop\git\python\MySQL Connector Python\customerIn.json'
dataIn = 'customerIn.json'

# read in the data from the data file (customerIn.txt) and return them in customers


def ReadCustomerData(dataIn):
    with open(dataIn, 'r') as df:
        customers = json.loads(df.read())

    # return the customers read in from the data file
    return customers


# print each customer

def PrintCustomer(customers):
    for customer in customers:
        print(customer)


# print the fields in a customer

def PrintFields(customers):
    for customer in customers:   # customer is a row in the customers table
        for column in customer:  # column is a column in the customers table
            print(customer[column])


# insert all the customers read in from the data file into the customers table (customer database in MySQL)

def InsertCustomers(customers):
    # INSERT statement
    insertSQL = 'INSERT INTO customer(customer_id, first_name, last_name, house_no, street, city, state, zip_code, phone_no, email)\
                 VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    for customer in customers:
        valStr = []  # make this a list of customer values

        # create the value string
        for column in customer:
            valStr.append(customer[column])

        # convert valStr to a tuple
        valStr = tuple(valStr)

        print(insertSQL, valStr)

        ##############################################################
        # Uncomment the following lines if demoing batch processing. #
        ##############################################################

        '''
        CUS.ConnectDB()                          # connect to the database
        CUS.myCursor.execute(insertSQL, valStr)  # execute insert statement
        CUS.mydb.commit()                        # commit the transaction
        CUS.DisconnectDB()
        '''


###########################################################################
# Main
#
# Status:   Completed
# Date:     4/8/2023
###########################################################################


if __name__ == '__main__':
    customers = ReadCustomerData(dataIn)

    # batch process the new customers into the database
    InsertCustomers(customers)
