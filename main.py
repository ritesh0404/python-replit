##name = input('whats the name?')

## To comment multiple line: crtl + /

# name =  'Ritesh'
# print('Hello ' + name)
a = 1
b = 10
c = 3
d,e,f = 6,7,8

# print (a+b)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##Data Types#

##++++ Fundamental Data Types
## int
# print('INT Data Type Results::')
# print(type(a-b)) #display type
# print (a-b)
# print(b ** c ) #b to the power of c
# print(b // 3) #b devide by 3 : quotient is 
# print(b % c) # b / c give remainder as
# print(round(3.4))

## float
# print('FLOAT Data Type Results::')
# print(type(a/b))
# print(a/b)
# print(float(str(10)))

##complex

##binary
# print('Binary number Results::')
# print(bin(5))
# print(type(bin(5)))
# print(int('0b101', 2))
# print(bin(0))

## bool
# is_cool = False
# print(is_cool)
# print(bool(0))
# print(bool(1))


## str
name1 = 'Ram Narayan'
name2 = "Sita Narayani"
# long_name3 = '''Hello
# Hi
# How 
# Are 
# You??
#  )O O(
#    ~
#   \\//  
#  ??'''
# print(name1)
# print(name2)
# print(long_name3)
# string concatenation
# print (name1 +name2)
# comb_name = name1 + name2
# print(comb_name)
# print(type(str(100)))
## Escapr Sequence (whatever comes after \ is a string)
# print('It\'s a wonder full day in \"Delhi.\" ')
## #Escapr Sequence (add a tab using \t )
# print('It\'s a wonder \t full day in \"Delhi.\" ')
## #Escapr Sequence (start new line  \n)
# print('It\'s a wonder full day in \n"Delhi.\" ')
## formatted Strings
# cus_name = 'Radha Krihna'
# cus_type = 'God'
# age = 999000009999
# print(f'Hello {cus_name} ji. \nYour customer type is {cus_type}. \nAs man knows you are at least there from {age} years protecting us. Thank You!') 
##[start:stop:stepover] - string indexes  ; - means to start at end
## parts of string cant be changed i..e. immutable - can be reassigned
# family_name = 'anjua kayasth'
# print(family_name[1:7]) #prints from second to 6th
# print(family_name[:5])
# print(family_name[::])
# print(family_name[::2])
# print(family_name[::-1])

## list Data Type ---------##
## list can be mutated
## list slicing
# list_first_name = [
#                     'Ram', 
#                     'Lakshman', 
#                     'Bharat', 
#                     'Shatraghun'
#                   ]
# list_last_name = [
#                   'Narayan', 
#                   'Man', 
#                   'Bhushan', 
#                   'Sinha'
#                  ]

# print(list_first_name[::-1])
# print(len(list_first_name))

# print(list_first_name[:3])
# print(list_first_name)

# list_fname2 = list_first_name  # both refers same address - so both change if anyone changes
# list_fname3 = list_first_name[:] # it creates new seperate list and both have different address
# print(list_first_name)
# print(list_fname2)
# list_fname2[0] = 'Ayodhya'
# print(list_first_name)
# print(list_fname2)

# list_fname3[0] = 'Janak'
# print(list_first_name)
# print(list_fname3)

##List functions------##
# amazon_country = ['India',
#                   'UK',
#                   'France',
#                   'Australia',
#                   'USA']
# print(amazon_country)

# amazon_country_append = amazon_country.append('Germany')
# print(amazon_country)
# print(amazon_country_append)

# amazon_country_ins = amazon_country.insert(1, 'Canada')
# print(amazon_country)

# amazon_country_extend = amazon_country.extend(['Pakistan', 'Sri Lanka'])
# print(amazon_country)

# print('POP Results::')
# ac_pop1 = amazon_country.pop(2)
# print(amazon_country)
# print(ac_pop1)
# ac_pop2 = amazon_country.pop()
# print(amazon_country)
# print(ac_pop2)

# amazon_country_extend = amazon_country.extend(['Pakistan', 'Sri Lanka'])
# print(amazon_country)

# print('Remove Results::')
# ac_rem1 = amazon_country.remove('Pakistan')
# print(amazon_country)
# print(ac_rem1)

# amazon_country_extend = amazon_country.extend(['Pakistan', 'Sri Lanka'])
# print('Clear Results::')
# ac_clr1 = amazon_country.clear()
# print(amazon_country)
# print(ac_clr1)

## methods index, count, in, sort, reverse, range, join, unpacking
# basket = ['a', 'b', 'c', 'd', 'e', 'f', 'e']

# print(basket.index('e'))
# print(basket.index('e',0,5))
# print(basket.count('e'))
# print('d' in basket)
# print('z' in basket)

# basket.sort()
# print(basket)

basket = ['a', 'b', 'z', 'c', 'd', 'e', 'f', 'e']
# print(basket)
# print(sorted(basket))

# basket.sort()
# print(basket)

# new_basket = sorted(basket)
# print(new_basket)

# new_basket.reverse()
# print(new_basket)

# print(basket[::-1])
# print(basket[:])

# print(list(range(1,100)))
# print(list(range(100)))

# sentence =  ' '.join(basket)
# print(sentence)

# sentence =  '@'.join(basket)
# print(sentence)

# sentence =  ''.join(basket)
# print(sentence)

# a,b,c, *others = [1,2,3,4,5,6,7]
# print(a)
# print(others)
# a,b,c, *others, d = [1,2,3,4,5,6,7]
# print(d)
# print(others)

# weapon = None
# print(weapon)

##Matrix - multi dimentional array like structure 

# matrix_example1 = [
#   [
#     [1,2,3,4,5,6,7,8,9,10],
#     ['R','I','T','E', 'S','G','H']
#   ]
# ]
# print(matrix_example1[0][1][2])
# print(len(matrix_example1[0]))

# new_matrix2 = matrix_example1.append(1)
# print(matrix_example1)

## tuple ~~~ like immutable List ~~~~~~~~~##
# my_tuple = (1,2,3,4,5,6,6,6,6,6,6)
# print(my_tuple)
# ## my_tuple[0] = 9 ## cant be modified
# print(9 in my_tuple)
# print(my_tuple.count(6))
# print(my_tuple.index(6))
# print(len(my_tuple))


## set ~~~~~~~~  unordered collection of unique objects ###

my_set = {1,2,3,4,5,6,6,6,7}

# print(my_set)
# print(my_set.add(100))
# print(my_set)
# print(my_set.add(2))
# print(my_set)

# my_list5 = [1,1,1,1,2,2,2,4,4,4]
# my_set5  = set(my_list5)
# print(my_set5)

# my_list6 = list(my_set5)
# print(my_list6)

# my_set1 = {1,2,3,6,6,6,7}
# my_set2 = {1,2,9,4,5,6,88,6,7}
# my_set3 = {11,12,13}

# print(my_set1.difference(my_set2)) 
# print(my_set1.discard(6)) 
# print(my_set1)

# print(my_set1.difference_update(my_set2)) 
# print(my_set1)

# print(my_set2.difference_update(my_set1)) 
# print(my_set2)

# print(my_set1 | my_set2)  #join
# print(my_set1.union(my_set2))  #join
# print(my_set1 & my_set2)  #intersection
# print(my_set1.intersection(my_set3))
# print(my_set1.isdisjoint(my_set2))
# print(my_set1.isdisjoint(my_set3))
# print(my_set1.issubset(my_set2))
# print(my_set1.issuperset(my_set3))


# dict


## +++ Classes (customised data Types)

##Specialised Data Types (from Libs)

##None
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##Operator Presedence (BODMAS) ##
# print ('Operator Presedence Results::')
# print ((20 - 3) * 4 )
# print (20 - 3 * 4 )

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## snake_case
## Variable should be starting with lower case or 
## underscore (private variable) and dont use
## key words or othe standards

## two underscore should not be used consequetively

## Constants should be in capitals as standard
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##Augmented Assignment Operator
# print('Augmented Assignment Operator Results::')
# some_value = 2
# print(some_value)
# some_value += 5
# print(some_value)
# some_value -= 10
# print(some_value)

##~~~~  Methods in Python.. start with .(dot) ~~#
# quote = 'bhagwan sab ko sad-buddi de'

# print(quote.capitalize())
# print(quote.find('12'))
# print(quote.find('d'))
# print(quote.replace('d', '1122'))

# quote2 = quote.replace('d', '1122')
# print(quote)
# print(quote2)


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##Exercise  Calculate Age
# import datetime

# current_date = datetime.date.today()
# current_year = current_date.year # Extract current year only

# name_user = input('Appka naam kya hain?')
# birth_year = input('Appka Janam kis varsh me huan?')
# birth_month = input('Appka Janam kis mahine me huan?')
# birth_day = input('Appka Janam kis tareekh ko huan?')
# current_age = (int(current_year)) - (int(birth_year))
# print(f'{name_user}, App abhin {current_age} varsh ke ho.')

##Exercise - User and Password message

# user_name_full = input(' Kirpya apna naam batayen?')
# password = input(f'Shri {user_name_full}, apna password type kare.')

# password_encrypt = ('*' * len(password))

# print(f'Shri {user_name_full}, aapka password \'{password_encrypt}\' hain aur ye {len(password)} aksharo ka hain.')


##~~ Dictionary~~~~~~unordered key/value concept~~~#

# dictionary = {
#   'a': 1,
#   'b': 2,
# }
# print(dictionary['a'])
# print(dictionary)

# dictionary1 = {
#   'a': [1,2,4],
#   'b': 'hello',
#   'c': False
# }
# print(dictionary1['a'][1])
# print(dictionary1)

my_list1 = [
  {
  'name': ['Ram','Shyam'],
  'age':  [23,21],
  'Religion': 'Hindu'
  },
  {
  'name': ['Rahim','Shekh'],
  'age':  [33,31],
  'Religion': 'Muslim'
  }
]
# print(my_list1)
# print(my_list1[0])
# print(my_list1[1]['Religion'])

# print(my_list1[0].get('Religion'))
# print(my_list1[0].get('Gender', 'Male'))

# my_list2 = dict(name='Ram')
# print(my_list2)

# print('Sex' in my_list1)
# print('age' in my_list1[0].keys())
# print('Hindu' in my_list1[0].values())
# print(my_list1[1].items())

# my_list3 = my_list1.copy()

# my_list1.clear()
# print(my_list1)
# print(my_list3)

# my_list4 = my_list1[0].copy()
# print(my_list4)

# print(my_list4.pop('Religion'))
# print(my_list1)
# print(my_list1[0].pop('Religion'))

# my_list4.update({'Religion':'Sanatan'})
# print(my_list4)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

## 26 MAy 2021
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Python Basics 2
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~Conditional Logics ~~~~~~~~~~~~~~~~~~~~~~~~~#

# is_prem = True
# is_not_moh  = True

# if is_prem and is_not_moh:
#   print('Krishna and Radha Love, and not moh. ')
#   print('Radhe Radhe')
# elif is_not_moh:
#   print('Krishna and Radha moh, and not love. ')
#   print('Radhe Radhe')
# else:
#   print('Radhe Radhe Radhe')

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Truthy and Falsy

# print(bool('')) #false
# print(bool('hello')) #true
# print(bool(0)) #false
# print(bool(123)) #true

# is_prem = 'YesYes Krishna ji loves radha'
# is_not_moh  = 'No No'

# if is_prem and is_not_moh:
#   print('Krishna and Radha Love, and not moh. ')
#   print('Radhe Radhe')
# elif is_not_moh:
#   print('Krishna and Radha moh, and not love. ')
#   print('Radhe Radhe')
# else:
#   print('Radhe Radhe Radhe')
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Ternary Operator
## action_if_true if condition else action_if_false

# is_prem = 'YesYes Krishna ji loves radha'
# is_not_moh  = ''

# naam_bolo = 'Radhe Radhe' if (is_prem and is_not_moh) else 'Radhe Krishna'
# print(naam_bolo)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Short Circuiting - AND and OR operator - both terminates as soon as it satifies some condition for whole

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Logical Operator - <,>, ==, >=, <=, !=, and, or, not

# is_magician = True
# is_expert = True

# out_msg = 'Expert Magician' if (is_magician and is_expert) else ('You are Getting There' if (is_magician) else 'You Need Magic Powers') 

# print(out_msg)

# if is_magician and is_expert:
#   print('Expert MAgician')
# elif is_magician and not is_expert:
#   print('Getting There')
# else:
#   print('Need MAgical Powers')

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## == compares values
## is compares memory location
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Loops

# for num in {1,2,3,4,5,6,7,8,9}:
#   print(f'Table for {num} is ::')
#   for num2 in {1,2,3,4,5,6,7,8,9,10}:
#     print(f' {num} * {num2} = {num*num2}')
#   print(f'End of Table for {num}.')
#   print(f'+++++++++++++++++++++++')

# for alpha in 'JAi Shri Radhe Krishna':
#   print(alpha)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## iteratives in a Dictionary

# user = {
#   'Forename': 'Ritesh',
#   'Surname': 'Kumar',
#   'Age': 33,
#   'Sex': 'Male'

# }
# print('for items in user')
# for items in user:
#   print(items)

# print('for items in user.items')
# for items in user.items():
#   print(items)

# print('for items in user.keys')
# for items in user.keys():
#   print(items)

# print('for items in user.values')
# for items in user.values():
#   print(items)

# print('for k, v in user')
# for k, v in user.items():
#   print(k, v)

# my_list6 = [
#   {
#     'Forename': 'Ritesh',
#     'Surname': 'Kumar',
#     'Age': 33,
#     'Sex': 'Male'
#   },
#   {
#     'Forename': 'Jitesh',
#     'Surname': 'Kumar',
#     'Age': 34,
#     'Sex': 'Male'
#   },
#   {
#     'Forename': 'Titesh',
#     'Surname': 'Cumar',
#     'Age': 35,
#     'Sex': 'Male'
#   }
# ]

# for a,b in my_list6[2].items():
#   print(a,b)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# mylist7 = [1,2,3,4,5,6,7,8,9]
# sumx1 = 0
# for numx1 in mylist7:
#   sumx1 = numx1  + sumx1
#   print(sumx1)
# print(sumx1)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## range()
# print(range(100))

# for num in range(100):
#   print(f'Table for {num} is ::')
#   for num2 in {1,2,3,4,5,6,7,8,9,10}:
#     print(f' {num} * {num2} = {num*num2}')
#   print(f'End of Table for {num}.')
#   print(f'+++++++++++++++++++++++')

# for _ in range(0,10,3):
#   print('Ritesh')

# for nunu in range(10,0,-2):
#   print(nunu)  

# for _ in range(2):
#   print(list(range(10)))


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##enamurate - gives the IndexError
# for index,number in enumerate(list(range(1,100))):
#   if number == 50:
#     print(f'Index for {number} is {index}.')

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## While

# item2 = 4
# while item2 < 50:
#   print(item2)
#   item2 += 1
# else:
#   print('done with else!!')

# item2 = 4
# while item2 < 50:
#   print(item2)
#   item2 += 1
#   break
# else:
#   print('done with else!!')
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# while True:
#   comment = input('Password of at leats 10 letter : ')
#   if (len(comment) < 11):
#     print('Password is less than 10 letters!! Try Again')
#   else:
#     print('PAssword Accepted!! ')
#     break

# while True:
#   comment = input('Password of at leats 10 letter : ')
#   if (len(comment) < 11):
#     print('Password is less than 10 letters!! Try Again')
#     continue
#   else:
#     break
  
#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# picture2 = []    

# for row in range(len(picture)):

#   index = 0
#   picture2 = [] 
#   while index < len(picture[row]):
#     if picture[row][index] == 0:
#       picture2.append(' ')
#     else:
#       picture2.append('*')
#     index += 1
#   print(picture2[:])

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# fill = '*'
# empty = ' '
# for row in picture:
#   for pixel in row:
#     if pixel:
#       print(fill, end='')
#     else:
#       print(empty, end='')
#   print('')

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##Exercise
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'a']
# dup_list = []
# for value in some_list:
#   if (dup_list.count(value) > 0):
#     continue
#   if (some_list.count(value) > 1):
#     dup_list.append(value)

# print(dup_list)    

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'a']
# dup_list = []
# for value in some_list:
#   if some_list.count(value) > 1:
#     if value not in dup_list:
#       dup_list.append(value)

# print(dup_list)    

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Functions ~~~~~~~~~~
# def say_hello():
#   print('hello')

# say_hello()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##parametres is when function is defined; Arguments are the actual values given

# def love(param1, param2):  ## parametrs
#   print(f'{param1} loves :) {param2}')

# love('Radha', 'Kishan')  ## positional arguments
# love(param2='Radha',param1='Kishan') ## keyword arguments

# def love1(param1='God', param2='Human'):  ## parametrs
#   print(f'{param1} loves :) {param2} @@@')

# love1('Radha', 'Kishan')  ## positional arguments
# love1()  ## Default parameters

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# def sum(a, b):
#   return a + b   ## function exists with Return

# print(sum(2,3))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# age = input("What is your age?: ")

# if int(age) < 18:
# 	print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
# 	print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
# 	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

# def checkDriverAge(age=0):
#   if int(age) < 18:
# 	  print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
# 	  print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
# 	  print("Congratulations on your first year of driving. Enjoy the ride!")  

# checkDriverAge()
# checkDriverAge(92)
# ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

## Methods are always owned by something before dot(.)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##docstrings

# def test1(a):
#   '''
#   This is a sample function that tells the importance of docstring
#   which will be visible after hovering over the function. Try it.:)
#   starting comment with 3 marks and end ing with 3 marks.
#   '''
#   print('££££££')

# test1(1)


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##    *args and **kwargs

# def test2(*args):
#   print(*args)
#   print(args)
#   return sum(args)

# print(test2(1,2,3,4,5,6,7,7))

# def test3(*args, **kwargs):
#   print(*args)    ## returns individual args
#   print(args)     ## returns tuples as values
#   print(*kwargs)  ## gives key values 
#   print(kwargs)   ##give dictionary
#   return sum(args)

# print(test3(1,2,3,4,5,6,7,7, n1=88, n2=99))
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## Rule of params: params, *args, default params, **kwargs 
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# def highest_num(li):
#   '''
#   To print the highest number in a list
#   '''
#   print(li)
#   val = 0
#   for item in li:
#     if (item > val):
#       val = item
#   print(f'Highest Number is {li} is : {val}.')

# # highest_num([10,1,-22,3,4,5,11])
# ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# def highest_even(li):
#   '''
#   To print the highest even number in a list
#   '''
#   val = 0
#   li_even = []
#   for item in li:
#     if (item % 2) == 0:
#       li_even.append(item)
  ##return max(li_even)    
  # if  len(li_even):
  #   highest_num(li_even)    
  # else:
  #   print('No even number is list')    

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  

# highest_num([10,1,-22,3,4,5,11])
# print(highest_even([10,1,-22,3,4,5,11]))
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## End for 27 May 2021


## Walrus Function

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#