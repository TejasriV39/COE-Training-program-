class Bank:
    print("Welcome to ABC Bank")
    balance=10000
    def options(self):
        print("-----------------------------------------------------------")
        print("1.Deposit\n 2.Withdraw\n 3.Balance Enquiry\n 0.Exit")
        case = int(input("Choose the correct option: "))
        if(case==1):
            obj.deposit()
        elif(case==2):
            obj.withdraw()
        elif(case==3):
            obj.bal_enquiry()
        else:
            obj.exit()
    def validate(self):
        count = 1
        while (count <= 3):
            pin = int(input("Enter the pin number"))
            if pin==309:
                obj.options()
            else:
                if count<3:
                    print("Invalid pin, Try again")
                else:
                    print("Your account has been blocked, try again later")
            count+=1
    def deposit(self):
        deposit_amt=int(input("Enter the amount to be deposited"))
        if deposit_amt >= 100 and deposit_amt % 100 == 0 and deposit_amt <= 50000:
            self.balance += deposit_amt
            print(f"New balance: {self.balance}")
        else:
            print("The minimum deposit amount is 100")
    def withdraw(self):
        withdrawl_amt=int(input("Enter the amount to be withdrawn"))
        new_balance=self.balance-500
        if withdrawl_amt >= 100 and withdrawl_amt % 100 == 0 and withdrawl_amt <=new_balance and withdrawl_amt<=20000:
            self.balance -=withdrawl_amt
            print(f"New balance: {self.balance}")
        else:
            print("Withdrawl Failed")
    def bal_enquiry(self):
        print(f'Your account balance is: ₹{self.balance}')
    def exit(self):
        print("Thank you for using our services, Visit again.")
        exit()

obj=Bank()
obj.validate()
