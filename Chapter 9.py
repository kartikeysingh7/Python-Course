f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()




def game():
    return 44677
score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()   
if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
        
        
        

for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')
                
                
                
                
with open("sample.txt") as f:
    content = f.read()
content = content.replace("donkey", "$%^@$^#")
with open("sample.txt", "w") as f:
    f.write(content)
    
    
    
    
words = ["donkey", "kaddu", "mote"]
with open("sample.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("sample.txt", "w") as f:
        f.write(content)
        
        
        
        
with open("log.txt") as f:
    content = f.read()
if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")
    
    
    
    
content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}") 
        i+=1
        
        
        
        
with open("this.txt") as f:
    content = f.read()
with open("copy.txt", 'w') as f:
    f.write(content)
    
    
    
    
file1 = "log.txt"
file2 = "this.txt"
with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2= f.read()
if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")
    
    
    
    
filename = "sample.txt"
with open(filename, "w") as f:
    f.write("")
    
    
    
    
import os
oldname = "sample2.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()
with open(newname, "w") as f:
    f.write(content)
os.remove(oldname)