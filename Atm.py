class Atm:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def cashwithdrawl(self):
        balance = 100
        print("Thank you for choosing [Cash Withdrawl].")
        withdrawl = int(input("Please put in your desired amount."))
        balance = balance + withdrawl
        print("Your balance is now $" + str(balance) + ".")
    
    def balanceinquiry(self):
        balance = 100
        print("Thank you for choosing [Balance Inquiry].")
        print("Your balance is $" + str(balance) + ".")
    
def main():
    cardnumber = input("Put in your cardnumber.")
    pinnumber = input("Put in your pinnumber.")
    option = int(input("Choose your option now. Please only enter 1 or 2."))
    newuser = Atm(cardnumber,pinnumber)
    if(option == 1):
        newuser.cashwithdrawl()
    elif(option == 2):
        newuser.balanceinquiry()
    else:
        print("I'm sorry, we did not understand your request.")

    
if __name__ == "__main__":
    main()