num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num2):
    f1=num1
else: 
    f1=num2
if(num3>num4):
    f2=num3
else:
    f2=num4    
    
if(f1>f2):
    print(f1)
else:
    print(f2)     





sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if(sub1<33 and sub2<33 and sub3<33):
    print("You are fail due to less than 33% marks in one of the subject")
elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total marks less than 40%")
else:
    print("Congratulations! You are pass")                  




text=input("Enter the text: ")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True        
elif("subscribe this" in text):
    spam = True
else: 
    spam = False
if(spam):
    print("This text is spam")
else:
    print("This text is not spam")  





username=input("Enter your username: ")
if(len(username)<=10):
    print("True")
else:
    print("False")           





names = ["shruti","harshita","harsh","aditya","devesh","kartikey"]
name = input("Enter your name to check: ")

if(name in names):
    print("Your name is in the list")
else:
    print("Your name is not in the list")          





marks = int(input("Enter your marks: "))

if(marks>=90):
    grade = "Ex"
elif(marks>=80):
    grade = "A"
elif(marks>=70):
    grade = "B"
elif(marks>=60):
    grade = "C"
elif(marks>=50):
    grade = "D" 
else:
    grade = "F"
print("Your grade is " + grade)



 