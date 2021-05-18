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

my_set1 = {1,2,3,4,5,6,6,6,7}
my_set2 = {1,2,9,4,5,6,88,6,7}


## dict
# print(type(a/b))
# print(a/b)

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

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#