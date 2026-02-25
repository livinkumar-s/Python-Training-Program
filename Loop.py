#while loop --->print("Hello world") 10 times
#5 times

# True--> until 5th execution, False--> 6th execution

# i=0

# while i>5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("----------------")
#     i-=1

# No of Execution ---->1,2,3,4,5...inf
# i=0,-1,-2...

# str1="Hello"
# print(str1[5])
# print(len(str1))


# for char in range(3,20,3):
#     print(char)

# print(list(range(100,150)))

# for i in range(100, 0, -1):
#     print(i)
 
# i=0 #0,...25,26

# while i<100:
#     if i>25:
#         continue
#     print(i)
#     i+=1

# no of execution --> infinite

# for i in range(100):
#     print(i)
#     if i==50:
#         continue

# 1-100

# for i in range(1,101):
#     print(i)


# secretnum=33
# inp 
# check

# 5th ---> 5 times 
# 60th --> 60 times


# secretnum=33
# notFound=True 

# while notFound:
#     inp=int(input("Guess the number: "))
#     if inp==secretnum:
#         print("You won")
#         notFound=False
#     else:
#         print("Try again")


secretnum=33

while True:
    inp=int(input("Guess the number: "))
    if inp==secretnum:
        print("You won")
        break
    else:
        print("Try again")
    