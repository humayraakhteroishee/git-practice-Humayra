from datetime import date
from utils import add, subtract, multiply, devision


print("Name: Humayra Akhter Oishee")
print("Today's date:", date.today())

print("(a+b)= ", add(78, 59))
print("(a-b)= ", subtract(79, 59))
print("(a*b)= ", multiply(79, 59))
print(f"(a/b)= {devision(79, 59): .2f}")
print(f"devision by zero= ", devision(79, 0))
