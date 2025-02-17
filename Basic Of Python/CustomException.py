#Rising custom exception in Python
#raise keyword is similar to throw in java
#CustomException class
class CustomException(Exception):
    pass


a = int(input("Enter number bw 1-20: "))
if(a<1 or a>20):
    raise CustomException("number should be bw 1-20")
print("you entered ",a)