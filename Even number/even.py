
even_number = []

num = 0

while num < 4:
  integer = int(input("Enter an even integer: "))
  if integer % 2 == 0:
    even_number.append(integer)
    num += 1
  else:
    print("You entered an odd number, try again")
  
print("You entered even numbers: ",(even_number))