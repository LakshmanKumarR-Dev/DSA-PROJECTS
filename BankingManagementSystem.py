import collections

class Customer:
    def __init__(self, acc_no, name, bal=0):
        self.acc_no = acc_no
        self.name = name
        self.bal = bal
        self.trns_his = collections.deque()

    def add_trans(self, trans_type, amount):
        self.trns_his.append((trans_type, amount))

class Node:
    def __init__(self, cus):
        self.cus = cus
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_cus(self, cus):
        new = Node(cus)
        new.next = self.head
        self.head = new

    def find_cus(self, acc_no):
        temp = self.head
        while temp:
            if temp.cus.acc_no == acc_no:
                return temp.cus
            temp = temp.next
        return None

    def display_cus(self):
        temp = self.head
        customers = []
        while temp:
            customers.append(f"Account No: {temp.cus.acc_no}, Name: {temp.cus.name}, Balance: {temp.cus.bal}")
            temp = temp.next
        return "\n".join(customers) if customers else "No customers"

class Bank:
    def __init__(self):
        self.customers = LinkedList()
        self.trans_stack = collections.deque()

    def add_cus(self, acc_no, name, bal=0):
        new_customer = Customer(acc_no, name, bal)
        self.customers.add_cus(new_customer)
        print(f"Customer {name} added successfully.")

    def deposit(self, acc_no, amount):
        temp = self.customers.find_cus(acc_no)
        if temp:
            temp.bal += amount
            temp.add_trans("Deposit", amount)
            self.trans_stack.append(("Deposit", amount))
            print(f"Deposited {amount} to account {acc_no}\nNew Balance: {temp.bal}")
        else:
            print("Customer not found.")

    def withdraw(self, acc_no, amount):
        temp = self.customers.find_cus(acc_no)
        if temp:
            if temp.bal >= amount:
                temp.bal -= amount
                temp.add_trans("Withdraw", amount)
                self.trans_stack.append(("Withdraw", amount))
                print(f"Withdrew {amount} from account {acc_no}\nNew Balance: {temp.bal}")
            else:
                print("Insufficient balance.")
        else:
            print("Customer not found.")

    def display_all(self):
        dis = self.customers.display_cus()
        print(dis)

    def trans_history(self):
        if self.trans_stack:
            print("Transaction History:")
            for i in self.trans_stack:
                print(f"{i[0]} : {i[1]}")
        else:
            print("No transactions.")

system = Bank()

while True:
    print("\nBanking System Menu:")
    print("1. Add Customer")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display All Customers")
    print("5. View Transaction History")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        bal = float(input("Enter Initial Balance: "))
        system.add_cus(acc_no, name, bal)

    elif choice == '2':
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))
        system.deposit(acc_no, amount)

    elif choice == '3':
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        system.withdraw(acc_no, amount)

    elif choice == '4':
        system.display_all()

    elif choice == '5':
        system.trans_history()

    elif choice == '6':
        print("Exiting Banking System.")
        break

    else:
        print("Invalid choice. Please try again.")
