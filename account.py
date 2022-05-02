def show_balance(balance):
  print("Your current balance is : $",balance)

def deposit(balance):
    amountd=float(input("Enter amount to deposit : "))
    return balance + amountd
 
def withdraw(balance):
    amountw=float(input("Enter amount to withdraw : "))
    return balance-amountw

def logout():
    print(f'goodbye')
