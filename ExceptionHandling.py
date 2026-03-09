print(1)
print(2)
print(3)
# print(4+"Hello")
# print(6/0)

# try:
#     print(int("Hello"))
# except ValueError:
#     print("Invalid conversion")


try:
    inp1=int(input("Enter your first number: "))
    inp2=int(input("Enter your second number: "))
    print(inp1/inp2)
except ZeroDivisionError:
    print("Provide valid input...!")
except ValueError:
    print("Numbers only...")
finally:
    print("Over")

print("5")
print("6")
print("7")

# print(5)
# print(4

# if True:
# print("Hi")

# print(5)