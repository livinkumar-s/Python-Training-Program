from AuthApp import Auth

auth=Auth()

while 1:
    print('''1---> SignUp
2--->Login
0--->Exit''')
    inp=int(input("Choose an Option: "))

    if inp==0:
        break
    elif inp==1:
        u=input("UserName: ")
        p=input("Password: ")
        e=input("Email: ")
        auth.signUp(u,p,e)
    elif inp==2:
        p=input("Password: ")
        e=input("Email: ")
        auth.login(e,p)
