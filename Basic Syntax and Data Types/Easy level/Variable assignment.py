# Assign the value 10 to a variable named x and print it.
# x=10
# print("x=",x)
# user input 
while True:
    x=input("Enter a number: ")
    if x.isdigit():
        x=int(x)
        print(f"Entered number is : {x} and datatype is {type(x)}")
        break
    else:
        print("Try again") 