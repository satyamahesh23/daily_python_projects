import time
second=int(input("enter seconds to count down: "))
while second>0:
    print(second)
    time.sleep(1)
    second=second-1
print("times up")
print("\a")

# How it works

# input() asks for the seconds, and int() turns the typed text into a number.
# The while loop runs as long as seconds is more than 0.
# Inside the loop, it prints the number, waits 1 second, and subtracts 1.
# When the number reaches 0, the loop stops and prints “Time’s up!” and beeps.