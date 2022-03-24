
try:
    age = int(input("enter your age : "))
    if age<18:
        raise ValueError("ineligible")
    else:
        print("eligible")

except ZeroDivisionError as z:
    print("exception occur --> "+ str(z))

except ValueError as v :
    print("exception occur --> "+ str(v))

except :
    print("exception occur ")
else:
    print("no exceptions ")

finally:
    print("done !")





