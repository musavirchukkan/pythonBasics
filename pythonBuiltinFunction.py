
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
