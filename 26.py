# 6. Banking System Using Functions
#  Functions for:
# o Deposit
# o Withdraw
# o Check Balance

balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("withdrawn:", amount)
    else:
        print("Insufficient Balance!")

def check_balance():
    print("Current Balance:", balance)


# Example Usage
deposit(1000)
withdraw(500)
check_balance()
