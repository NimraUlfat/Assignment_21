#20. Creating a Custom Exception
#Assignment:
#Create a custom exception InvalidAgeError. Write a function check_age(age) 
#that raises this exception if age < 18. Handle it with try...except.

#Create a custom exception
class InvalidAgeError(Exception):
    pass

#Define the function that raises the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted.")

#21Handle the exception with try...except
try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid integer.")
