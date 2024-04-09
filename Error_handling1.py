import time
for i in range(10):
  time.sleep(1)
     

try:
    a=int(input("Enter your age:"))
    print(a)
    c=a/0
except(ValueError):
  print("Age cannot be a string!")
except(ZeroDivisionError):
  print("Division by zero is not possible.")
finally:
    # To free up resources used by the above code.
    pass
  
