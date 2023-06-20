a="Good Morning, "
b=input("Enter your number: ")
c=a+b
print(c)





letter="Dear <|Name|>, \nYou are Selected! \n<|Date|>"
a=input("Enter your name: ")
b=input("Enter date: ")
letter=letter.replace("<|Name|>",a)
letter=letter.replace("<|Date|>",b)
print(letter)





a="Hi, my name is  Ronnie!"
print(a.find("  "))





a="Hi, my name is  Ronnie!"
a=a.replace("  "," ")
print(a)





letter = "Dear Harry, This Python course is nice! Thanks!"
print(letter)
formatted_letter = "Dear Harry,\n\tThis Python course is nice!\nThanks!"
print(formatted_letter)