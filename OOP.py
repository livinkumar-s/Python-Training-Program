# Square.

class Square:
    #cons func
    def __init__(self):
        self.shapeName="Square"
        self.width=5
    #Instance Methods
    def printArea(self):
        print(self.width*self.width)


# 2 attribute, 1 method

class Bottle(Square):
    def __init__(self,h,r):
        self.shapeName="Cylinder"
        self.height=h
        self.radius=r
    def printVolume(self):
        print(self.height*(22/7)*self.radius*self.radius)

# self.shapeName="Square"
# self.height=h
#        self.radius
#  self.shapeName="Cylinder"
#         self.width=5

# s1=Square()
# b1=Bottle(4,2)

# print(s1.shapeName)
# print(b1.shapeName)

# 2 attr, 1 method

# sqr1=Square()
# sqr2=Square()
# sqr3=Square()
# sqr4=Square()

# b1=Bottle(20,3)
# b2=Bottle(10,3)

# print(sqr3.shapeName)
# sqr1.printArea()

# b1.printVolume()
# b2.printVolume()

# str1="Hello World"
# str1.upper()

# lis1=[1,2,3,4,5]



# print(type(lis1)) #<class "list">
# print(type(b2)) #<class __main__."Bottle">


# .upper
# .lower 


# calc 
# class Calculator:
#     def __init__(self):
#         self.result=0
#     def add(self,num1,num2):
#         self.result=num1+num2
#         print(self.result)
#     def sub(self,num1,num2):
#         self.result=num1-num2
#         print(self.result)
#     def mul(self,num1,num2):
#         self.result=num1*num2
#         print(self.result)
#     def div(self,num1,num2):
#         self.result=num1/num2
#         print(self.result)

# class AdvancedCalc(Calculator):
#     def __init__(self):
#         self.result=0
#     def square(self,num):
#         self.result=num*num
#         print(self.result)

# c1=Calculator()
# c2=AdvancedCalc()
# c2. 

# Encapsulation

class User:
    def __init__(self,n,p):
        self.userName=n 
        self.password=p 
    
    def login(self,u,p):
        if self.userName==u and self.__password==p:
            print("Success ")
        else:
            print("Invalid Credintials")

u1=User("Pal","12345")

# print(u1.__password)
u1.login("Pal","12345")