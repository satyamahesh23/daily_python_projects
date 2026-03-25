# a = 10
# b = 20

# print(a == b)   # Equal to          → False  (10 is NOT equal to 20)
# print(a != b)   # Not equal to      → True   (10 IS different from 20)
# print(a > b)    # Greater than      → False
# print(a < b)    # Less than         → True
# print(a >= 10)  # Greater or equal  → True   (10 >= 10 is True)
# print(a <= 9)   # Less or equal     → False  (10 <= 9 is False)

age=18
if age>=18:
    print("you can vote")
else:
    print("no need")

# --- if / elif / else (multiple conditions) ---
# elif = "else if" — checks another condition if the previous was False.
# Python checks conditions TOP to BOTTOM and stops at the FIRST True one.

# marks = 75

# if marks >= 90:                   # first check: 90 or above?
#     print("Grade: A")             # runs if marks >= 90
# elif marks >= 75:                 # second check: 75 or above?
#     print("Grade: B")             # runs if first was False AND this is True
# elif marks >= 60:                 # third check: 60 or above?
#     print("Grade: C")
# else:                             # none of the above matched
#     print("Grade: F")             # default case — always runs last

# Output: Grade: B  (because 75 >= 90 is False, but 75 >= 75 is True)

# username="satya"
# password="1234"
# if username=="satya" and password=="1234":
#     print("login success")
# else:
#     print("no")
# day="sunday"
# if day=="sunday"or day=="friday":
#     print("its a weekend")


# day2 mini program

account=1234
account_balance=5000

enter_pin=int(input("enter the pin: "))

if enter_pin==account:
    print("PIN is correct")

action=input("do ypu want to (check/withdraw)? ").lower()
if action=="check":
    print(f"your balance is {account_balance}")
elif action=="withdraw":
    amount=int(input("enter the amount to withdraw : "))
    if amount<=0:
        print("invalid")
    elif amount>account_balance:
        print("inssufficient")
    else:
        account_balance=account_balance-amount
        print(f"{amount} withdraw .remaining :{account_balance}")
else:
    print("wrong PIN")