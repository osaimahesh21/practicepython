
x = 10 # Assigns the value 10 to the variable x
def add():     #Defines a function named addd 
    global x
    x = 3  # creates a new local variable x with in the function and assigns the value 3 
    x = x + 3 # modifing the local variable x by adding 3 to it 
add()
print("x=",  x)

name = "Mahesh"
age = "25"
technology = "Python "

print(f"My name is {name} and I am {age} years old ,I am {technology} devolper ")


fruits = ["apple", "banana", "orange"]
print(*fruits, sep=", ")

fruits = ["apple", "banana", "orange"]
print(*fruits, sep=",,,,,,, ")

persons = ["Mahesh", "Manoj", "Sanjay"]

print(*persons, sep="###")


print("Hello")


x = 5 
def add ():
    x = 3 
    x = x + 5
    print(x)
add()
print(x)

text = "abcdefghijklmnop"
print(text[1:6:2])