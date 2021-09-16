# # 0. Find the idle weight
# weight= int(input("enter your weight(kg): "))
# height= float(input("enter your height(m): "))

# bmi= round(weight/(height*height))

# print(f"your bmi is {bmi}")
# if (bmi>25):
#     print(
#         f"you are over weight\n reduce your weight to {round(21.7*(height*height))}")

# # 1. print current date and time
# import datetime
# print(datetime.datetime.now())

# # 2. accepts the user's first and last name and print them in reverse order with a space between them
# first_name=input("enter the first name")
# last_name= input("enter the last name")
# print(f"hello {last_name} {first_name}") 

# # 3. Print a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
# values= input("enter some comma-seprated values")
# list= values.split(",")
# tuple= tuple(list)
# print("list:", list)
# print("tuple:",tuple)

# # 4. accept a filename from the user and print the extension of that.
# filename= input("enter the filename with extension")
# extension= filename.split(".")
# print(f"it is a .{extension[-1]} file")

# # 5. display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)

# # 6. print the calendar of a given month and year.
# import calendar
# month= int(input("enter the month"))
# year= int(input("enter the year"))
# print(calendar.month(year, month))

# # 7. calculate the sum of three given numbers, if the values are equal then return three times of their sum
# def sum_thrice(x, y, z):

#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))

# # 8. count the number 4 in a given list
# def count_the_four(list):
#   count=0
#   for l in list:
#     if l==4:
#       count= count + 1 
#   return count
# print(count_the_four([1,4,2,4]))
# print(count_the_four([1,4,2,4,3,4]))

# # 9. test whether a passed letter is a vowel or not.
# def find_vowel(chr):
#   vowel= ["a","e","i","o",'u']
#   if chr in vowel:
#     print("it is a vowel")
#   else:
#     print("it is a constrains")
# print(find_vowel("a"))
# print(find_vowel("b"))

# # 10. print out all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for x in numbers:
#   if x ==237:
#     print(x)
#     break;
#   elif x%2==0:
#     print(x)

# # 11. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# def sum(x,y):
#   sum= x + y

#   if sum>15 and sum<20:
#     print(sum)
#     return(20)
#   else:
#     return (sum)
# print(sum(10, 7))
# print(sum(15, 15))

# # 12.  get height and the width of console window.
# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

# print('Number of columns and Rows: ',terminal_size())

# # 13. find the available built-in modules
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))

# # Random: 14. Head or tails
# import random 

# def toss(n):
#   number= random.randint(0,1)
#   print (number)
#   if number == n:
#     print("and you win")
#   else:
#     print("oops!! you loss")

# call=input("your call:")
# num = 0
# call= call.lower()
# if call == "head":
#   num = 1
# elif call == "tail":
#   num = 0
# else:
#   print("call correctly")
# print(toss(num))

# # Random: 14. who will the bill
# import random 

# names= ["Angela","Ben","Jenny","michael", "Chole"]
# # number= random.randint(0,4)
# print(f"{random.choice(names)} will pay the bill") 


