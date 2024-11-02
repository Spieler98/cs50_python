import validator_collection as validator

s = input("Email: ")
try:
    if validator.email(s, ):
        print("Valid")
except:
    print("Invalid")