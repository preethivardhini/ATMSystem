import time
print("Please insert your ATM Card")
time.sleep(5)
password=2875
pin=int(input("Enter 4-Digit ATM Pin:"))
Balance=10000
if pin==password:
  while True:
    print("""
    1==Balance
    2==Withdraw Balance
    3==Deposit Balance
    4==Transfer
    5==pin change
    6==Exit
    """
    )
    try:
      option=int(input("Please enter your choice"))
    except:
      print("Please enter a valid option")
    
    if option==1:
      print(f"Your current Balance is {Balance}")

    if option==2:
      withdraw_amount=int(input("Please enter withdraw amount"))
      Balance=Balance - withdraw_amount
      print(f"{withdraw_amount} is debited from your account")
      print(f"Your updated Balance is {Balance}")

    if option==3:
      deposit_amount=int(input("Please enter deposit_amount"))
      Balance=Balance+deposit_amount
      print(f"{deposit_amount} is credited to your account")
      print(f"Your updated Balance is {Balance}")

    if option==4:
      transfer_account_details=int(input("Please enter account details"))
      transfer_amount=int(input("Please enter transfer_amount"))
      print(f"{transfer_amount} is credited to {transfer_account_details}")
      Balance=Balance - transfer_amount
      print(f"Your updated Balance is {Balance}")

    if option==5:
      pin_change=int(input("Please enter account number"))
      pin_change=int(input("Please enter otp:"))
      pin_change=int(input("Enter new pin:"))  
      pin_change=int(input("Confirm new pin:"))

    if option==6:
      break
else:
      print("Wrong Pin please try again")    