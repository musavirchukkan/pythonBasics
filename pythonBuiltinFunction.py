
# ################   STRING FUNCTIONS   ################

# converts first character to uppercase and others to lowercase
sentence = "i love PYTHON"
capitalized_string = sentence.capitalize()
print(capitalized_string)


# returns the centered padded string of length 25
sentence = "Python is awesome"
new_string = sentence.center(25, '*')
print(new_string)


# convert all characters to lowercase
text = "pYtHon"
lowercased_string = text.casefold()
print(lowercased_string)


# number of occurrence of 'p'
message = 'python is popular programming language'
print('Number of occurrence of p:', message.count('p'))


# check if the message ends with fun
message = 'Python is fun'
print(message.endswith('fun'))


# '\t' replaced with whitespace characters
str = 'xyz\t12345\tabc'
result = str.expandtabs()
print(result)


# The encode() method returns an encoded version of the given string.
title = 'Python Programming'
print(title.encode())


# check the index of 'fun'
message = 'Python is a fun programming language'
print(message.find('fun'))


# find the index of is
text = 'Python is fun'
result = text.index('is')
print(result)


# string contains either alphabet or number
name1 = "Python3"
print(name1.isalnum())

# string contains alphabet ( string.isalpha())
# string contains decimal number ( string.isdecimal())
# string contains number ( string.isnumeric())
# string contains whitespace ( string.isspace())
# string contains punctuation ( string.ispunct())
# string contains digits ( string.isdigit())
# string contains valid identifier ( string.isidentifier())
# string contains lowercase ( string.islower())
# string contains uppercase ( string.isupper())
# string contains printable characters ( string.isprintable())
# string contains titlecase ( string.istitle())


# join elements of text with space
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
print(' '.join(text))


# The string ljust() method returns a left-justified string of a given minimum width.
string = 'cat'
width = 5
fillchar = '*'
# print left justified string of minimum width 5
print(string.ljust(width))
# print left justified string and fill the remaining spaces
print(string.ljust(width, fillchar))
# The string rjust() method returns a right-justified string of a given minimum width.
print(string.rjust(width, fillchar))


# convert message to lowercase
message = 'PYTHON IS FUN'
print(message.lower())

# convert message to uppercase
message = 'python is fun'
print(message.upper())

# converts lowercase to uppercase and vice versa
name = "JoHn CeNa"
print(name.swapcase())


# remove leading and trailing whitespaces
message = '     Learn Python  '
print('Message:', message.strip())
# remove trailing whitespace from title (message.rstrip())
# remove leading whitespace from title (message.lstrip())


# method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator
string = "Python is fun"
# 'is' separator is found
print(string.partition('is '))


# replace Characters
text = 'bat ball'
replaced_text = text.replace('b', 'c')
print(replaced_text)


# split the text from space
text = 'Python is a fun programming language'
print(text.split(' '))


# ################   LIST FUNCTIONS   ################

# append element to the list
list = ['Python', 'is', 'a', 'fun']
list.append('programming')
print(list)

# Remove all elements from the list
list = ['Python', 'is', 'a', 'fun']
list.clear()
print(list)

# copy the list
list = ['Python', 'is', 'a', 'fun']
list_copy = list.copy()
print(list_copy)

# return the number of time the value occurs in the list
list = ['Python', 'is', 'a', 'fun', 'Python']
print(list.count('Python'))

# Add elements of list2 to the end of list1
list1 = ['Python', 'is', 'a', 'fun']
list2 = ['programming', 'language']
list1.extend(list2)

# postion of element in the list
list = ['Python', 'is', 'a', 'fun']
print(list.index('is'))

# add element to the list at the specified position
list = ['Python', 'is', 'a', 'fun']
list.insert(1, 'programming')
print(list)

# remove element from the list
list = ['Python', 'is', 'a', 'fun']
list.remove('fun')
print(list)

# remove element from the list at the specified position
list = ['Python', 'is', 'a', 'fun']
list.pop(1)
print(list)

# reverse the list
list = ['Python', 'is', 'a', 'fun']
list.reverse()
print(list)

# sort the list
list = ['Python', 'is', 'a', 'fun']
list.sort()
print(list)

###############   Dictionary Functions   ################

# add key and value to the dictionary
dictionary = {'name': 'John', 'age': '27'}
dictionary['address'] = 'USA'
print(dictionary)

# remove all elements from the dictionary
dictionary = {'name': 'John', 'age': '27'}
dictionary.clear()
print(dictionary)

# Copy the dictionary
dictionary = {'name': 'John', 'age': '27'}
dictionary_copy = dictionary.copy()
print(dictionary_copy)

# Return a dictionary with specific key and value
x = ('key1', 'key2', 'key3')
y = 0
dictionary = dict.fromkeys(x, y)
print(dictionary)

# Returns the value of the specified key
dictionary = {'name': 'John', 'age': '27'}
print(dictionary.get('name'))

# Returns a list containing a tuple for each key value pair
dictionary = {'name': 'John', 'age': '27'}
print(dictionary.items())

# Returns a list containing the dictionary keys
dictionary = {'name': 'John', 'age': '27'}
print(dictionary.keys())

# remove key and value from the dictionary
dictionary = {'name': 'John', 'age': '27'}
dictionary.pop('age')
print(dictionary)

# remove last inserted key and value from the dictionary
dictionary = {'name': 'John', 'age': '27'}
dictionary.popitem()
print(dictionary)

# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
dictionary = {'name': 'John', 'age': '27'}
dictionary.setdefault('address', 'USA')
print(dictionary)

# Updates the dictionary with the specified key-value pairs
dictionary = {'name': 'John', 'age': '27'}
dictionary.update({'address': 'USA'})
print(dictionary)

# Returns a list of all the values in the dictionary
dictionary = {'name': 'John', 'age': '27'}
print(dictionary.values())


# ################   TUPLE FUNCTIONS   ################

# tuple is immutable
tuple = ('Python', 'is', 'a', 'fun')
print(tuple)

# Returns the number of times a specified value occurs in a tuple
tuple = ('Python', 'is', 'a', 'fun', 'Python')
print(tuple.count('Python'))

# Searches the tuple for a specified value and returns the position of where it was found
tuple = ('Python', 'is', 'a', 'fun', 'Python')
print(tuple.index('Python'))


# ################   SET FUNCTIONS   ################

# set is an unordered collection of distinct elements
set = {'Python', 'is', 'a', 'fun'}
print(set)

# add element to the set
set = {'Python', 'is', 'a', 'fun'}
set.add('programming')
print(set)

# remove element from the set
set = {'Python', 'is', 'a', 'fun'}
set.remove('fun')
print(set)

# remove element from the set at the specified position
set = {'Python', 'is', 'a', 'fun'}
set.pop()
print(set)

# remove all elements from the set
set = {'Python', 'is', 'a', 'fun'}
set.clear()
print(set)

# copy the set
set = {'Python', 'is', 'a', 'fun'}
set_copy = set.copy()
print(set_copy)

# Returns a set containing the difference between two or more sets
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set3 = set1.difference(set2)
print(set3)

# Removes the items in this set that are also included in another, specified set
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set1.difference_update(set2)
print(set1)

# Remove the specified item
set = {'Python', 'is', 'a', 'fun'}
set.discard('fun')
print(set)

# Returns a set containing the intersection of sets
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set3 = set1.intersection(set2)
print(set3)

# Returns a set containing the intersection of sets
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set1.intersection_update(set2)
print(set1)

# Returns whether two sets have a intersection or not
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
print(set1.isdisjoint(set2))

# Returns whether another set contains this set or not
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
print(set1.issubset(set2))

# Returns whether this set contains another set or not
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
print(set1.issuperset(set2))

# Returns a set with the symmetric differences of two sets
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set3 = set1.symmetric_difference(set2)
print(set3)

# Returns a set with the symmetric differences of two sets
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set1.symmetric_difference_update(set2)
print(set1)

# Returns a set with the union of sets
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set3 = set1.union(set2)
print(set3)

# Update the set with another set, or any other iterable
set1 = {'Python', 'is', 'a', 'fun'}
set2 = {'programming', 'language'}
set1.update(set2)
print(set1)
