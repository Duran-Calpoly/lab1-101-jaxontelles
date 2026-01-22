def calculate_average(num1, num2, num3):
  amount = 3
  average = (num1 + num2 + num3)/(amount)
  return(average)
  
print(calculate_average(10,20,30))

def add_tax(bill_total):
  tax = (bill_total)*(0.10)
  total = bill_total + tax
  return(total)

print(add_tax(100.00))

def greet_user(name):
  return f"Hello {name}"

print(greet_user("jaxon"))
