#Introduction in f-String , String formatting in Python

#Old style String formatting
letter = ("My name is {}."
          "\nIm from {}.")
name = input("Enter your name : ")
place = input("Enter where are you from : ")
print(letter.format(name,place))

#new Style using f-String
name = input("Enter your name : ")
place = input("Enter where are you from ")
print(f"Hello My name is {name}. Im from {place}")

price = 12.00010
print(f"For only {price:.2f} dollars") # :.2f for only 2 value after .

#if we pass {{name}} {{place}} it will highlight with {name} {place}
print(f"We can use f-String like this way : Im {{name}} Im from {{place}}")

