#
# def check_prime (a):
#     flag = False
#     div_by = 0
#     if a == 2:
#         flag = True
#     else:
#         for n in range(2, a):
#             if a % n == 0:
#                 flag = False
#                 div_by = n
#                 break
#             else:
#                 flag = True
#     if not flag:
#             print('it is not a prime number')
#             print(f'because it is divisible by {div_by}')
#     else:
#             print('it is a prime number')
#     return
#
# check_prime(3367)
#
# -----------------------------------------------
#calculator
#
# operator_list = ['+','-','*','/']
# problem= input('enter your problem: ').replace(' ', '')
# for operator in operator_list:
#     if operator in problem:
#         num1 , num2 = problem.split(operator)
#         if operator == '+':
#             answer = float(num1) + float(num2)
#         elif operator == '-':
#             answer = float(num1) - float(num2)
#         elif operator == '*':
#             answer = float(num1) * float(num2)
#         elif operator == '/':
#             answer = float(num1) / float(num2)
# print(f'the solution for {problem} is {answer}')
#
# ------------------------------------------
#guess game
# import random
# random_num = random.randint(1, 100)
# x= input('''guess the number between 1 and 100
#     you have 6 chances : ''')
# for chance in range(1,7):
#     if int(x) == random_num:
#         print('you win')
#         break
#     elif chance == 6:
#         print (f'''sorry. you lost
#     The right answer was {random_num}''')
#     elif int(x) > random_num:
#         x = input(f'''Greater than the answer. Try again
#     you have {6-chance} chance(s) left  : ''')
#     elif int(x) < random_num:
#         x = input(f'''Lesser than the answer. Try again
#     you have {6-chance} chance(s) left   : ''')
#------------------------------------------------------------
#fizzbuzz
# for i in range (1,101):
#     if i%3 == 0 and i%5 == 0:
#         print('fizzbuzz')
#     elif i%5 ==0 :
#         print('buzz')
#     elif i%3 ==0 :
#         print('fizz')
#     else:
#         print(i)
#------------------------------------------------------------
#palindrome check
#
#input_phrase = input(f"enter your phrase : ")
# input_phrase = input_phrase.replace(' ','')
# print (input_phrase)
# phrase_length = len(input_phrase)
# print (phrase_length)
# a=0
# b=-1
# for run in range(1,int(phrase_length/2)+1):
#     print (f'run number {run}')
#     if input_phrase[a]==input_phrase[b]:
#         print (input_phrase[a])
#         print (input_phrase[b])
#         is_palindrome = True
#         a += 1
#         b += -1
#     else:
#         is_palindrome = False
#         break
# if is_palindrome == True:
#     print('it is a palindrome')
# elif is_palindrome == False:
#     print('it is not a palindrome')
#--------------------------------------------------------------
# basic unit converter
#
# choice = input('''What would you like to convert?
# type 'a' for kilometers to miles or vice versa or
# type 'b' for celcius to fahrenheit or vice versa:
#     ''')
#
# if choice == 'a':
#     x = input('type the value to be converted: ')
#     km_mile = input ('type the unit of the value eg. km or m : ')
#     if km_mile == 'km' :
#         answer = round(float(x) * 0.621371)
#         print (f'it is {answer} miles')
#     elif km_mile == 'm' :
#         answer = round(float(x) * 1.60934)
#         print (f'it is {answer} kilometers')
# elif choice == 'b':
#     x = input('type the value to be converted: ')
#     cel_fahr = input ('type the unit of the value eg. c or f : ')
#     if cel_fahr == 'c' :
#         answer = round((float(x) * 1.8) +32)
#         print (f'it is {answer} fahrenheits')
#     elif cel_fahr == 'f' :
#         answer = round((float(x)-32) * 5/9)
#         print (f'it is {answer} celcius')
# else:
#     print('choice is wrong')
#
# -----------------------------------------------------------
#
#temperature conversion
#
# input_string = input('''Hello, please input the value and unit to be converted, separated by a space
# (example "36 c" or "98 f" or "310 k") :  ''')
# units = ['k','c','f']
# x,y = input_string.split(' ')
# z = input('to which unit you want the value to be converted : ')
# for unit in units:
#     if unit in input_string:
#         if y== 'c' and z == 'k':
#             answer = round(float(x) + 273.15, 2)
#         elif y== 'c' and z == 'f':
#             answer = round(float(x) * 1.8 + 32, 2)
#         elif y== 'f' and z == 'c':
#             answer = round((float(x) - 32) * 5 / 9, 2)
#         elif y == 'f' and z == 'k':
#             answer = answer = round((float(x) - 32) * 5/9 + 273.15, 2)
#         elif y == 'k' and z == 'c':
#             answer = round(float(x) - 273.15, 2)
#         elif y == 'k' and z == 'f':
#             answer = round((float(x) - 273.15) * 1.8 + 32, 2)
#         print(f'{input_string} is converted to {answer} {z}')
#
#---------------------------------------------------------------
#
#Simple interest calculator
#
# p = input('''welcome to the simple interest calculator!
# please write the Principle amount: ''')
# n = input('please write the term period in year(s): ')
# r = input('please write the rate of interest per anum: ')
# si = round((float(p)*float(n)*float(r))/100,2)
# print(f'The simple interest for the entered values would be {si}')
#
#----------------------------------------------------------------------
#
# joke generator
# import random
# jokes = {1:"I used to steal soap, but I'm clean now.",
#          2:"Why do tigers have stripes? They don't want to be spotted.",
#          3:"My boss told me to have a good day. So I didn't go to work.",
#          4:"I once got fired from a keyboard factory. They said I wasn't putting in enough shifts.",
#          5:"I used to be afraid of hurdles. But I got over it.",
#          6:"Why do dragons sleep during the day? So they can hunt knights.",
#          7:"I went shopping for a pair of camouflage pants. But I couldn't find any.",
#          8:"Bacon and eggs walk into a diner. The host says, “Sorry, we don’t serve breakfast here.”",
#          9:"I told a chemistry joke once. I didn't get much of a reaction.",
#          10:"My dad was hit on the head with a can of soda. Luckily, it was a soft drink.",
#          11:"What do you call people who sleep in their socks? Tiny"}
# rand = random.randint(1,len(jokes))
# print(jokes[rand])
#--------------------------------------------------------------------------------------
#
#odd or even checker
#
# num = input('give a number to check whether it is odd or even: ')
# try :
#     if int(num)%2 == 0 :
#         print(f"{num} is an even number")
#     elif int(num)%2 != 0 :
#         print (f"{num} is an odd number")
# except ValueError:
#     print('number incorrect')
#---------------------------------------------------------------------
# Character counter
# input_string = input('Enter a string: ').replace(' ', '')
#
# # Create a dictionary to count characters
# char_count = {}
#
# for char in input_string:
#     if char.isalpha():
#         char_count[char] = char_count.get(char,0)+1
#
# for char,count in char_count.items():
#     print(f'the {char} has occurred {count} times')
#
# ------------------------------------------------------------------------
#
#magic eight ball
# import random
# answers = ['yes','no','may be']
# input('please ask your (yes/no) questions: ')
# for trial in range(0,11):
#     randomnumber = random.randint(0, 2)
#     input(f'''{answers[randomnumber]}
# next question : ''')
# print('thank you for playing "magic eight ball"')
#------------------------------------------------------------------------
#bmi calculator
#
# weight = input('enter your weight and unit with space in between (eg: 75 kg or 129 lbs) : ')
# height = input('enter your height and unit with space in between (eg: 167 cm or 65 in or 1.5 m) : ')
# try:
#     weight_value, weight_unit = weight.split(' ')
#     height_value, height_unit = height.split(' ')
#     if weight_unit == 'lbs':
#         weight_value = float(weight_value) * 0.453592
#     if height_unit == 'cm':
#         height_value = float(height_value) / 100
#     elif height_unit == 'in':
#         height_value = float(height_value) * 0.0254
#     #print (weight_value, height_value)
#     bmi = float(weight_value) / (float(height_value) * float(height_value))
#     if bmi < 18.5:
#         print('You seem to be Underweight')
#     elif bmi < 25:
#         print('You seem to be Normal')
#     elif bmi < 28:
#         print('You seem to be Overweight')
#     else:
#         print('You seem to be Obese')
# except ValueError:
#     print('Your input seems to be Invalid')
#------------------------------------------------------------------------------------
#grocery list
# no_of_items = input(f'''hello, welcome to the grocery list program
# how many items do you have in mind?
# ''')
# grocery_list = {}
# for item_no in range(1,int(no_of_items)+1):
#     item = input(f'enter your item and press enter: ')
#     grocery_list[item_no] = grocery_list.get(item_no, '') + item
# print(f'here is your list')
# for key, value in grocery_list.items():
#           print(f'{key}: {value}')
#------------------------------------------------------------------------------------
#Reversing a string
#
# input_string = (input("Enter a string: "))
# reversed_string = input_string[::-1]
# print(reversed_string)
#------------------------------------------------------------------------------
# fibonacci
# a,b=0,1
# x= int(input(f'how many numbers do you want from the fibonacci sequence: '))
# for i in range (1, x+1):
#     if i == 1:
#         print(a, end=', ')
#     elif i == 2:
#         print(b, end=', ')
#     else:
#         answer = a+b
#         print(answer, sep= ', ', end= ', ')
#         a, b = b, answer
#-----------------------------------------------------------
#max numbers
# number_list = []
# num_of_items = int(input(f'how many numbers do you have? : '))
# print(f'start writing your numbers. press enter after each value')
# for i in range (1, num_of_items+1):
#     next_item = int(input(f'write the number : '))
#     number_list.append(next_item)
# print(f'''
# The max of the values you entered is {max(number_list)}''')
#-------------------------------------------------------------------
#rock paper scissor
# import random
# print('''welcome to rock paper scissor
# Type ROCK / PAPER / SCISSOR to make your choice
# ''')
# no_of_rounds = int(input('How may rounds would you like to play : '))
# game_choices=['ROCK', 'PAPER', 'SCISSOR']
# sys,user = 0,0
# for round_no in range(1,no_of_rounds+1):
#     print(f'''
#     ROUND {round_no}''')
#     user_input1 = input('What is your choice among ROCK, PAPER, SCISSOR: ').upper()
#     random_value = random.randint(0,2)
#     print(f'''        Your choice : {user_input1}
#         System choice : {game_choices[random_value]}''')
#     if user_input1 == game_choices[random_value]:
#         print(f'DRAW. score: system {sys}   you {user}')
#     elif user_input1 == 'ROCK' and game_choices[random_value] == 'PAPER':
#         sys += 1
#         print(f'SYSTEM WINS. score: system {sys}   you {user}'
#               f'')
#     elif user_input1 == 'ROCK' and game_choices[random_value] == 'SCISSOR':
#         user += 1
#         print(f'YOU WIN. score: system {sys}   you {user}'
#               f'')
#     elif user_input1 == 'PAPER' and game_choices[random_value] == 'ROCK':
#         user += 1
#         print(f'YOU WIN. score: system {sys}   you {user}')
#     elif user_input1 == 'PAPER' and game_choices[random_value] == 'SCISSOR':
#         sys += 1
#         print(f'SYSTEM WINS. score: system {sys}   you {user}')
#     elif user_input1 == 'SCISSOR' and game_choices[random_value] == 'ROCK':
#         sys += 1
#         print(f'SYSTEM WINS. score: system {sys}   you {user}')
#     elif user_input1 == 'SCISSOR' and game_choices[random_value] == 'PAPER':
#         user += 1
#         print(f'YOU WIN. score: system {sys}   you {user}')
# if user > sys:
#     print(f'''Great!!!
#     you have played {no_of_rounds} rounds
#     you scored {user} points and you WIN!!!''')
# elif user == sys:
#     print(f'''
# It is a Draw. Would you like to play again''')
# else:
#     print(f'''
# you played {no_of_rounds} rounds
# you scored {user} points
# Sorry, you LOST''')
#-------------------------------------------------------
# sudoku solver
s_num=[1,2,3,4,5,6,7,8,9]

in1 = input(f'''WELCOME TO THE SUDOKU PUZZLE
please enter the FIRST row
(with zeroes for the empty boxes):
''')
in2 = input(f'''
please enter the SECOND row:
''')
in3 = input(f'''
please enter the THIRD row:
''')
in4 = input(f'''
please enter the FOURTH row:
''')
in5 = input(f'''
please enter the FIFTH row:
''')
in6 = input(f'''
please enter the SIXTH row:
''')
in7 = input(f'''
please enter the SEVENTH row:
''')
in8 = input(f'''
please enter the EIGHTH row:
''')
in9 = input(f'''
please enter the NINTH row:
''')


a11,a12,a13,b14,b15,b16,c17,c18,c19=int(in1[0]),int(in1[1]),int(in1[2]),int(in1[3]),int(in1[4]),int(in1[5]),int(in1[6]),int(in1[7]),int(in1[8])
a21,a22,a23,b24,b25,b26,c27,c28,c29=int(in2[0]),int(in2[1]),int(in2[2]),int(in2[3]),int(in2[4]),int(in2[5]),int(in2[6]),int(in2[7]),int(in2[8])
a31,a32,a33,b34,b35,b36,c37,c38,c39=int(in3[0]),int(in3[1]),int(in3[2]),int(in3[3]),int(in3[4]),int(in3[5]),int(in3[6]),int(in3[7]),int(in3[8])
d41,d42,d43,e44,e45,e46,f47,f48,f49=int(in4[0]),int(in4[1]),int(in4[2]),int(in4[3]),int(in4[4]),int(in4[5]),int(in4[6]),int(in4[7]),int(in4[8])
d51,d52,d53,e54,e55,e56,f57,f58,f59=int(in5[0]),int(in5[1]),int(in5[2]),int(in5[3]),int(in5[4]),int(in5[5]),int(in5[6]),int(in5[7]),int(in5[8])
d61,d62,d63,e64,e65,e66,f67,f68,f69=int(in6[0]),int(in6[1]),int(in6[2]),int(in6[3]),int(in6[4]),int(in6[5]),int(in6[6]),int(in6[7]),int(in6[8])
g71,g72,g73,h74,h75,h76,i77,i78,i79=int(in7[0]),int(in7[1]),int(in7[2]),int(in7[3]),int(in7[4]),int(in7[5]),int(in7[6]),int(in7[7]),int(in7[8])
g81,g82,g83,h84,h85,h86,i87,i88,i89=int(in8[0]),int(in8[1]),int(in8[2]),int(in8[3]),int(in8[4]),int(in8[5]),int(in8[6]),int(in8[7]),int(in8[8])
g91,g92,g93,h94,h95,h96,i97,i98,i99=int(in9[0]),int(in9[1]),int(in9[2]),int(in9[3]),int(in9[4]),int(in9[5]),int(in9[6]),int(in9[7]),int(in9[8])

a = {11: a11, 12: a12, 13: a13, 21: a21, 22: a22, 23: a23, 31: a31, 32: a32, 33: a33}
b = {14: b14, 15: b15, 16: b16, 24: b24, 25: b25, 26: b26, 34: b34, 35: b35, 36: b36}
c = {17: c17, 18: c18, 19: c19, 27: c27, 28: c28, 29: c29, 37: c37, 38: c38, 39: c39}
d = {41: d41, 42: d42, 43: d43, 51: d51, 52: d52, 53: d53, 61: d61, 62: d62, 63: d63}
e = {44: e44, 45: e45, 46: e46, 54: e54, 55: e55, 56: e56, 64: e64, 65: e65, 66: e66}
f = {47: f47, 48: f48, 49: f49, 57: f57, 58: f58, 59: f59, 67: f67, 68: f68, 69: f69}
g = {71: g71, 72: g72, 73: g73, 81: g81, 82: g82, 83: g83, 91: g91, 92: g92, 93: g93}
h = {74: h74, 75: h75, 76: h76, 84: h84, 85: h85, 86: h86, 94: h94, 95: h95, 96: h96}
i = {77: i77, 78: i78, 79: i79, 87: i87, 88: i88, 89: i89, 97: i97, 98: i98, 99: i99}

print(a)

for num in range(11,100):
    if a.get(num) == 0:
        for n in range (1,10):
            if any(value != n for key, value in a.items()):
                a[num] = n
                break
print(a)

