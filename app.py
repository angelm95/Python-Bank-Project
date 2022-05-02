from banking_pkg import account



def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
name=input("Enter name to register : ")
pin=input("Enter pin : ")
balance=0
print(name)
print(f'You registered with a starting balance of {balance}')
pin_to_validate=0
name_to_validate=""

database = {"user":"password"}

while True:
    pin_to_validate=input("Enter password")
    name_to_validate=input("Enter name")
    if pin_to_validate == pin and name_to_validate == name:
        print("Login Sucessful")
        break

while True:
  atm_menu(name)
  choice = input("Make your choice : ")
  if(choice =="1"):
    account.show_balance(balance)
    
  elif(choice == "2"):
    balance = account.deposit(balance)
    
  elif(choice == "3"):
    balance = account.withdraw(balance)
    
  elif(choice == "4"):
    account.logout()
    break
  else:
    print("Wrong choice !! ")


  



