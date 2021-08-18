#Love calculator
Male_name= input("Enter your name:").lower()
Female_name= input("Enter your name:").lower()

combined_name= Male_name + Female_name 
t= combined_name.count("t")
r = combined_name.count("t")
u = combined_name.count("t")
e = combined_name.count("t")
true= t+r+u+e

l = combined_name.count("t")
o = combined_name.count("t")
v= combined_name.count("t")
e = combined_name.count("t")
love=l+o+v+e

score= int(str(true))+int(str(love))

if (score<10 or score>90):
    print(f"your score is {score}, you go together like coke and mentos")
elif(score>=40 and score<=50):
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}")
