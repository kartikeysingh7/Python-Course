def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))




def farh(cel):
    return (cel *(9/5)) + 32
c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))




print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")




n! = (n-1)! * n 
sum(n) = sum(n-1) + n




n = 3
for i in range(n):
    print("*" * (n-i))
    
    
    
    
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Harry is a good      "
n = remove_and_split(this, "Harry")
print(n)
print(this)
print(this.strip())
