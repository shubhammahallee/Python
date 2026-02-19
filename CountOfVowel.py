letter = input("Enter letter: ").lower()

count = 0

for char in letter:
    if(char =="a" or char =="u" or char =="o" or char =="i" or char =="e"):
        count +=1
print(count)    
