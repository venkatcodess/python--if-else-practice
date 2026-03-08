balance=int(input("ENTER YOUR BANK BALANCE:"))
amount=int(input("ENTER YOUR WITHDRAWL AMOUNT:"))
if amount>balance:
    print("Insufficient Balance")
elif amount>10000:
    print("Daily limit exceeded")
else:
    print("Transtion sucessfull")