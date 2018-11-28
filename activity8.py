# Activity 8
# Erase the current code in the file and create the code to complete the requirements as stated in the assignment.
import csv

with open('customers.csv', 'r') as f:
    reader = csv.reader(f)
    list1 = list(reader)

print("Customer Viewer")
print()


class Customer:
    def __init__(self, c_id=0, first_name="", last_name="", company_name="", address="", city="", state="", zip=""):
        self.c_id = c_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def getCustomer(cust_id):

        if 601 > cust_id > 100:
            for i in range(len(list1)):
                new_cust_id = str(cust_id)
                if new_cust_id in list1[i][0]:
                    first1 = list1[i][1]
                    second1 = list1[i][2]
                    company = list1[i][3]
                    add = list1[i][4]
                    city = list1[i][5]
                    state = list1[i][6]
                    zip = list1[i][7]
        else:
            print("please enter a number between 100 and 601")

        list2 = [first1, second1, company, add, city, state, zip]
        return list2

    def printer(list3):
        if list3[2] == "":
            print(list3[0] + " " + list3[1])
            print(list3[3])
            print(list3[4] + ", " + list3[5] + " " + list3[6])
        else:
            print(list3[0] + " " + list3[1])
            print(list3[2])
            print(list3[3])
            print(list3[4] + ", " + list3[5] + " " + list3[6])


y = 1
while y == 1:
    cust_id = int(input("Enter customer ID: "))
    print()

    list3 = Customer.getCustomer(cust_id)

    Customer.printer(list3)
    print()
    cont = input("Continue? (y/n)")
    print()
    if cont == 'y':
        y = 1
    elif cont == 'n':
        y = 2
        print("Bye!")







                # print(list2)
        # for id1 in list1[id1][0]:


        # print(list1.index(id))
        # print(list1.index(id + 1))

# findId(cust_id)
#print(list1)
#print(list1[1][0])
#print(cust_id)

