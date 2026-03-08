# Python ATM Withdrawal Program

This program simulates an ATM withdrawal using if-elif-else conditions.

## Python Code

```python
balance = int(input("Enter your bank balance: "))
amount = int(input("Enter your withdrawal amount: "))

if amount > balance:
    print("Insufficient Balance")
elif amount > 10000:
    print("Daily Limit Exceeded")
else:
    print("Transaction Successful")
```

## Example Output

```
Enter your bank balance: 5000
Enter your withdrawal amount: 2000
Transaction Successful
```
