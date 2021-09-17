# 1. know your time
# age= int(input("tell me your age: "))
# print(f"your years left till 90 is {90-age}")
# print(f"your months left till 90 is {(90-age)*12}")
# print(f"your weeks left till 90 is {(90-age)*52}")
# print(f"your days left till 90 is {(90-age)*365}")

# 2. takes a sequence of numbers and determines whether all the numbers are different from each other.
# def sequence(list):
#     if len(list) == len(set(list)):
#         return True 
#     else: return False

# ls= list(input("enter the seqence of number"))
# print(sequence([6,3,5,8,9]))
# print(sequence([5,4,3,8,5]))

# 2. create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
# import random
# char_list= ['a', 'e', 'i', 'o', 'u']
# random.shuffle(char_list)
# print(" ".join(char_list))

# 3. remove and print every third number from a list of numbers until the list becomes empty.
# def remove(list):
#     position= 3-1
#     idx= 0
#     while (len(list)>0):
#        idx= (position+ idx)% len(list)
#        print(list.pop(idx))
#        len(list)-1  

# list= [10,20,30,40,50,60,70,80,90]
# print(remove(list))

# 4. find unique triplets whose three elements gives the sum of zero from an array of n integers.
# def triplet(nums):
#     result = []
#     nums.sort()
#     for i in range(len(nums)-2):
#         if i> 0 and nums[i] == nums[i-1]:
#             continue
#         l, r = i+1, len(nums)-1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#         if s > 0:
#             r -= 1
#         elif s < 0:
#             l += 1
#         else:
#             # found three sum
#             result.append((nums[i], nums[l], nums[r]))
#             # remove duplicates
#             while l < r and nums[l] == nums[l+1]:
#                 l+=1
#             while l < r and nums[r] == nums[r-1]:
#                 r -= 1
#                 l += 1
#                 r -= 1
#             return result

# ls= [1, -6, 4, 2, -1, 2, 0, -2, 0]
# print(triplet(ls)) 

# 5. create the combinations of random 4 digit ATM pin
# import random
# print(random.randrange(1000,10000))

# 6. print a long text, convert the string to a list and print all the words and their frequencies.
# word_str= "nehanshu nirbhay sapna sharma advait sharma"
# word_list= word_str.split(" ")
# print(f"String of word: {word_str}")
# print(f"List of word: {word_list}")
# word_freq= [word_list.count(n) for n in word_list]
# print(f"Pairs (Words and Frequencies:\n {str(list(zip(word_list, word_freq)))}")

#  7. count the number of each character of a given text of a text file.
# import collections
# import  pprint
# file_input= input("file name:")
# with open(file_input, 'r') as info:
#     count =collections.Counter(info.read().upper())
#     value= pprint.pformat(count)
# print(value)

# 8. 
