names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)
    except (KeyboardInterrupt, EOFError):
        break
    

print("\nAdieu, adieu, to ", end="")

if len(names) == 1:
    print(names[0])
elif len(names) == 2:
    print(names[0], "and", names[1])
else:
    print(", ".join(names[:-1]), "and", names[-1])