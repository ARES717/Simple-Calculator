def cal():
    a = input("to start the Programm, Please type Start:")
    if a.lower() == "start":
         print("Welcome to Calculator")
         print("please choose the operation youy want to do:")
         print("1. Addition")
         print("2. Subtraction")
         print("3. Multiplication")
         print("4. Division")
         choice = input("pleae enter your choice:")
         if choice == "1":
              print("you chose Addition")
              print("the result is:", add())
         elif choice == "2":
              print("the result is:", sub())
         elif choice == "3":
              print("the result is:", Mul())
         elif choice == "4":
              print("the result is:", Div())
def add():
     x = int(input("please enter first Number:"))
     y = int(input("please enter second Number:"))
     return x + y
def sub():
     x1 = int(input("pleasem enter first Number:"))
     x2 = int(input("pleaseenter second Number:"))
     return x1 - x2
def Mul():
     x3 = int(input("please enter first Number"))
     x4 = int(input("please enter second Number"))
     return x3 * x4
def Div ():
     x5 = int(input("please enter first Number:"))
     x6 = int(input("please enter second Number:"))
     return x5 / x6
while True:
     cal()    
    
