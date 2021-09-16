import random
#1
# call= input("give a call: ").lower()
#toss= random.randint(0,2)
#if (call=="head" and toss==1):
#    print("wallah, its head")
#elif (call=="tail" and toss==0 ):
#    print("wallah, its tail")
#elif (call=="head" and toss==0 ):
#    print("uhh, you lost")
#elif (call == "tail" and toss == 1):
#    print("uhh, you lost")
#else:
#    print("check your call spealling")

#2
#random.seed(321)

#randomInteger= random.randint(1,10)
#print(randomInteger)

#randomFloat= random.random()*5
#print(randomFloat)

#3
Banker_Names= {"Anglena", 'ben', 'jenny', 'michael','chole'}

print(type(Banker_Names))
person= random.randint(Banker_Names)

print(person)