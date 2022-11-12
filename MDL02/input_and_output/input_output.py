# Input
name = input("What is your name ?")
print(f'your name is {name}')


#Output -----
# print takes a mandatory argument of type vararg and four optional
# arguments (sep, and, file and flush), all objects are separated by sep,
# converted to string and terminated by end. the final String is displayed by the user.

name = "Wally"
last_name = "Roberto"

print(name, last_name)
print(name, last_name, end="...\n")
print(name, last_name, sep="#")