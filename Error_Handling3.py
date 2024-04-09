def sum(a,b):
  try:
    print("file open")
    c=a+b
    return c
  except Exception:
    print("Something is not Correct!")
  finally:
    print("File Closed!")

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
sum(a,b)
