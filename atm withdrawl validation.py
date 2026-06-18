balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Transaction Successful")
    else:
        print("Amount should be multiple of 100")
else:
    print("Insufficient Balance")
