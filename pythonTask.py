# name
print("\n*********** Abdul Musavir C ************\n")
# for repeating the same code
while True:
    print("""
    1.Task 1
    2.Task 2
    3.Task 3
    """)
    task = int(input("\nEnter your choice : "))

    # ############## task 1 #####################

    if task == 1:

        while True:
            print("""
            1. Python program to print "Hello World"
            2. Python program to do sum of 'n' numbers, after taking inputs from the user
            3. Write a python program to find the area of a square and rectangle.
            4. Create a string & get the characters of string from 2 to 18 using both positive and negative indexing.
            5. Create and print a list with same and different items.
            6. Access an item from the list using its index.
            7. Access an item from the list using negative index.
            8. Modify an item in the list.
            9. Access the items in the list using slicing.
            10. Create a dictionary and print it.
            11. Change the value of a key.
            """)

            question = int(input("choose your question : "))

            # 1 # Python program to print "Hello World"
            if question == 1:

                print("\nHello World\n")

            # 2 # Python program to do sum of 'n' numbers, after taking inputs from the user
            elif question == 2:
                n = int(input("\nnumber of item to add : "))
                print("\n")
                list = []
                sum = 0
                for i in range(n):
                    element = int(input("enter the item : "))
                    list.append(element)
                    sum = sum+element
                print("entered elements are : ", list)
                print("sum of entered elements is : ", sum, "\n")

            #  3 # Write a python program to find the area of a square and rectangle.
            elif question == 3:
                while True:
                    print("""
                    1.Square
                    2.circle
                    3.rectangle
                    4.triangle""")
                    type = input("\nchoose your option : ")
                    if type == "1":
                        length = int(input("\nenter the length of square : "))
                        area = length*length
                        print("area of square is : ", area)
                    elif type == "2":
                        radius = int(input("\nenter the radius of circle : "))
                        area = 3.14*radius*radius
                        print("area of circle is : ", area)
                    elif type == "3":
                        length = int(
                            input("\nenter the length of rectangle : "))
                        breadth = int(
                            input("enter the breadth of rectangle : "))
                        area = length*breadth
                        print("area of rectangle is : ", area)
                    elif type == "4":
                        base = int(input("\nenter the base of triangle : "))
                        height = int(input("enter the height of triangle : "))
                        area = 0.5*base*height
                        print("area of triangle is : ", area)
                    else:
                        print("invalid option")
                    choise = input("\ndo you want to continue (y/n) : ")
                    if choise == "n":
                        break

            # 4 # Create a string & get the characters of string from 2 to 18 using both positive and negative indexing.
            elif question == 4:
                string = input("\nenter string : ")
                print("positive indexing : ", string[1:17])
                length = len(string)
                print("negative indexing : ", string[-length+1:-length+17])

            # 5 # Create and print a list with same and different items.
            elif question == 5:
                slist = ["apple", "banana", "cherry",
                         "orange", "kiwi", "melon", "mango"]
                print("same items : ", slist)
                dlist = [1, 2, "apple", 3.4, "cherry", {
                    "kiwi", 5, "melon", 6}, (7, 8, "banana", 9)]
                print("\n")
                print("different items : ", dlist, "\n")

            # 6 # Access an item from the list using its index.
            elif question == 6:
                list = ['apple', 2, 'banana', 30, 34,
                        'cherry', 55.65, 'orange', 45]
                print("list : ", list)
                indx = int(input("index of item : "))
                print(list[indx])

            # 7 # Access an item from the list using negative index.
            elif question == 7:
                list = ['apple', 2, 'banana', 30, 34,
                        'cherry', 55.65, 'orange', 45]
                print("list : ", list)
                length = len(list)
                indx = int(input("index of item : "))
                print(list[-length+indx-1])

            # 8 # Modify an item in the list.
            elif question == 8:
                list = ['python', 'java', 'php', 'html', 'css', 'javascript']
                print("list : ", list)
                list.append("c++")
                print("list appended : ", list)
                list.insert(2, "c#")
                print("list inserted : ", list)
                list.remove("java")
                print("list removed : ", list)

            # 9 # Access the items in the list using slicing.
            elif question == 9:
                list = ['python', 'java', 'php', 'html', 'css', 'javascript']
                print(list)
                print("sliced list : ", list[1:3])

            # 10 # Create a dictionary and print it.
            elif question == 10:
                dict = {'name': 'musavir', 'age': '20',
                        'language': 'python', 4: 'index'}
                print("dict : ", dict)

            # 11 # Change the value of a key.
            elif question == 11:
                dict = {'name': 'musavir', 'age': '20',
                        'language': 'python', 4: 'index'}
                print("dict : ", dict)
                dict['age'] = '23'
                print("changed dictionary : ", dict)

            else:
                print("Invalid Question Number, Try Again")
            choice = input(
                "Do you Want to Exit (Y for main menu),enter any key to continue : ")
            if choice == "y":
                break

    # ############## task 2 #################

    if task == 2:

        while True:

            print("""
            1. Create a string & demonstrate the following.
            2. Create a list & demonstrate the following.
            3. Create a tuple & demonstrate the following.
            4. Create a dictionary & demonstrate the following.
            """)

            question = int(input("choose your question : "))

            # 1 # Create a string & demonstrate the functions
            if question == 1:
                # capitalize()
                print("\n capitalize()")
                sentence = "i love PYTHON"
                print("sentence : ", sentence)
                capitalized_string = sentence.capitalize()
                print("capitalized sentence : ", capitalized_string)
                # casefold()
                print("\ncasefold()")
                text = "pYtHon"
                print("text : ", text)
                lowercased_string = text.casefold()
                print("lowercased string : ", lowercased_string)
                # center()
                print("\ncenter()")
                sentence = "Python is awesome"
                print("sentence : ", sentence)
                new_string = sentence.center(25, '*')
                print("new string : ", new_string)
                # count()
                print("\ncount()")
                sentence = "python is awesome"
                count = sentence.count('a')
                print(count)
                # encode()
                print("\nencode()")
                sentence = "python is awesome"
                encoded_string = sentence.encode()
                print(encoded_string)
                # endswith()
                print("\nendswith()")
                sentence = "python is awesome"
                if sentence.endswith("awesome"):
                    print("sentence ends with awesome")
                else:
                    print("sentence does not end with awesome")
                # expandtabs()
                print("\nexpandtabs()")
                sentence = "python\tis\ta\tawesome\tprogramming\tlanguage"
                new_string = sentence.expandtabs(10)
                print(new_string)
                # find()
                print("\nfind()")
                sentence = "python is awesome"
                index = sentence.find('is')
                print(index)
                # format()
                print("\nformat()")
                sentence = "python is awesome"
                new_string = sentence.format()
                print(new_string)
                # format_map()
                print("\nformat_map()")
                sentence = "python is awesome"
                new_string = sentence.format_map({"python": "python"})
                print(new_string)
                # index()
                print("\nindex()")
                sentence = "python is awesome"
                index = sentence.index('is')
                print(index)
                # isalnum()
                print("\nisalnum()")
                sentence = "python is awesome"
                if sentence.isalnum():
                    print("sentence is alphanumeric")
                else:
                    print("sentence is not alphanumeric")
                # isalpha()
                print("\nisalpha()")
                sentence = "python is awesome"
                if sentence.isalpha():
                    print("sentence is alphabetic")
                else:
                    print("sentence is not alphabetic")
                # isdecimal()
                print("\nisdecimal()")
                sentence = "python is awesome"
                if sentence.isdecimal():
                    print("sentence is decimal")
                else:
                    print("sentence is not decimal")
                # isdigit()
                print("\nisdigit()")
                sentence = "python is awesome"
                if sentence.isdigit():
                    print("sentence is digit")
                else:
                    print("sentence is not digit")
                # isidentifier()
                print("\nisidentifier()")
                sentence = "python is awesome"
                if sentence.isidentifier():
                    print("sentence is identifier")
                else:
                    print("sentence is not identifier")
                # islower()
                print("\nislower()")
                sentence = "python is awesome"
                if sentence.islower():
                    print("sentence is lowercase")
                else:
                    print("sentence is not lowercase")
                # isnumeric()
                print("\nisnumeric()")
                sentence = "python is awesome"
                if sentence.isnumeric():
                    print("sentence is numeric")
                else:
                    print("sentence is not numeric")
                # isprintable()
                print("\nisprintable()")
                sentence = "python is awesome"
                if sentence.isprintable():
                    print("sentence is printable")
                else:
                    print("sentence is not printable")
                # isspace()
                print("\nisspace()")
                sentence = "python is awesome"
                if sentence.isspace():
                    print("sentence is space")
                else:
                    print("sentence is not space")
                # istitle()
                print("\nistitle()")
                sentence = "python is awesome"
                if sentence.istitle():
                    print("sentence is title")
                else:
                    print("sentence is not title")
                # isupper()
                print("\nisupper()")
                sentence = "python is awesome"
                if sentence.isupper():
                    print("sentence is uppercase")
                else:
                    print("sentence is not uppercase")
                # join()
                print("\njoin()")
                sentence = "python is awesome"
                new_string = sentence.join(["python", "is", "awesome"])
                print(new_string)
                # lower()
                print("\nlower()")
                sentence = "python is awesome"
                new_string = sentence.lower()
                print(new_string)
                # maketrans()
                print("\nmaketrans()")
                sentence = "python is awesome"
                new_string = sentence.maketrans({"a": "b", "e": "f"})
                print(new_string)
                # partition()
                print("\npartition()")
                sentence = "python is awesome"
                new_string = sentence.partition("is")
                print(new_string)
                # replace()
                print("\nreplace()")
                sentence = "python is awesome"
                new_string = sentence.replace("is", "is not")
                print(new_string)
                # split()
                print("\nsplit()")
                sentence = "python is awesome"
                new_string = sentence.split(" ")
                print(new_string)
                # splitlines()
                print("\nsplitlines()")
                sentence = "python is awesome"
                new_string = sentence.splitlines()
                print(new_string)
                # startswith()
                print("\nstartswith()")
                sentence = "python is awesome"
                if sentence.startswith("python"):
                    print("sentence starts with python")
                else:
                    print("sentence does not start with python")
                # strip()
                print("\nstrip()")
                sentence = "python is awesome"
                new_string = sentence.strip()
                print(new_string)
                # swapcase()
                print("\nswapcase()")
                sentence = "python is awesome"
                new_string = sentence.swapcase()
                print(new_string)
                # title()
                print("\ntitle()")
                sentence = "python is awesome"
                new_string = sentence.title()
                print(new_string)
                # translate()
                print("\ntranslate()")
                sentence = "python is awesome"
                new_string = sentence.translate({"a": "b", "e": "f"})
                print(new_string)
                # upper()
                print("\nupper()")
                sentence = "python is awesome"
                new_string = sentence.upper()
                print(new_string)
                # zfill()
                print("\nzfill()")
                sentence = "python is awesome"
                new_string = sentence.zfill(25)
                print(new_string)

            elif question == 2:
                # 2 # Create a list & demonstrate the following.

                # append()
                print("\nappend()")
                list = ["python", "is", "awesome"]
                list.append("programming")
                print(list)
                # clear()
                print("\nclear()")
                list = ["python", "is", "awesome"]
                list.clear()
                print(list)
                # copy()
                print("\ncopy()")
                list = ["python", "is", "awesome"]
                new_list = list.copy()
                print(new_list)
                # count()
                print("\ncount()")
                list = ["python", "is", "awesome"]
                count = list.count("is")
                print(count)
                # extend()
                print("\nextend()")
                list = ["python", "is", "awesome"]
                new_list = list.extend(["programming", "language"])
                print(new_list)
                # index()
                print("\nindex()")
                list = ["python", "is", "awesome"]
                index = list.index("is")
                print(index)
                # insert()
                print("\ninsert()")
                list = ["python", "is", "awesome"]
                new_list = list.insert(1, "is not")
                print(new_list)
                # pop()
                print("\npop()")
                list = ["python", "is", "awesome"]
                new_list = list.pop()
                print(new_list)
                # remove()
                print("\nremove()")
                list = ["python", "is", "awesome"]
                new_list = list.remove("is")
                print(new_list)
                # reverse()
                print("\nreverse()")
                list = ["python", "is", "awesome"]
                new_list = list.reverse()
                print(new_list)
                # sort()
                print("\nsort()")
                list = ["python", "is", "awesome"]
                new_list = list.sort()
                print(new_list)

            elif question == 3:
                # 3 # Create a tuple & demonstrate the following.

                # count()
                print("\ncount()")
                tuple = ("python", "is", "awesome")
                count = tuple.count("is")
                print(count)
                # index()
                print("\nindex()")
                tuple = ("python", "is", "awesome")
                index = tuple.index("is")
                print(index)

            elif question == 4:
                # 4 # Create a dictionary & demonstrate the following.

                # clear()
                print("\nclear()")
                dictionary = {"python": "is", "is": "awesome"}
                dictionary.clear()
                print(dictionary)
                # copy()
                print("\ncopy()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.copy()
                print(new_dictionary)
                # fromkeys()
                print("\nfromkeys()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.fromkeys(
                    ["python", "is", "awesome"], "programming")
                print(new_dictionary)
                # get()
                print("\nget()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.get("python")
                print(new_dictionary)
                # items()
                print("\nitems()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.items()
                print(new_dictionary)
                # keys()
                print("\nkeys()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.keys()
                print(new_dictionary)
                # values()
                print("\nvalues()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.values()
                print(new_dictionary)
                # pop()
                print("\npop()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.pop("python")
                print(new_dictionary)
                # popitem()
                print("\npopitem()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.popitem()
                print(new_dictionary)
                # setdefault()
                print("\nsetdefault()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.setdefault("python", "programming")
                print(new_dictionary)
                # update()
                print("\nupdate()")
                dictionary = {"python": "is", "is": "awesome"}
                new_dictionary = dictionary.update({"python": "programming"})
                print(new_dictionary)
            else:
                print("Invalid Question Number, Try Again")
            choice = input(
                "\nDo you Want to Exit (Y for main menu),enter any key to continue : ")
            if choice == "y":
                break

    # ############## task 3 ##############

    if task == 3:

        while True:
            print("""
            1. Arithmetic operators
            2. Assignment operators
            3. Comparison operators
            4. Logical operators
            5. Identity operators
            6. Membership operators
            7. Bitwise operators
            """)

            question = int(input("choose your question : "))

            if question == 1:
                # 1 # Arithmetic operators
                print("Examples of Arithmetic Operator")
                a = int(input("Enter 1st number: "))
                b = int(input("Enter 2nd number: "))

                # addition
                print('Addition of numbers (a+b)')
                add = a + b
                print(add)
                # subtraction
                print("Subtraction of numbers (a-b)")
                sub = a - b
                print(sub)
                # multiplication
                print("Multiplication of number (a*b)")
                mul = a * b
                print(mul)
                # division
                print("Division(float) of number (a/b)")
                div1 = a / b
                print(div1)
                # division
                print("Division(floor) of number (a//b)")
                div2 = a // b
                print(div2)
                # modulus
                print("Modulo of both number (a%""b)")
                mod = a % b
                print(mod)
                # exponent
                print("Power of number (a**b)")
                p = a ** b
                print(p)

            elif question == 2:
                # 2 # Assignment operators
                print("Examples of Assignment Operator")
                print("""
                =	 x = 5	        x = 5	
                +=	 x += 3	        x = x + 3	
                -=	 x -= 3	        x = x - 3	
                *=	 x *= 3	        x = x * 3	
                /=	 x /= 3	        x = x / 3	
                %=	 x %= 3	        x = x % 3	
                //=	 x //= 3	x = x // 3	
                **=	 x **= 3	x = x ** 3	
                &=	 x &= 3	        x = x & 3	
                |=	 x |= 3	        x = x | 3	
                ^=	 x ^= 3	        x = x ^ 3	
                >>=	 x >>= 3	x = x >> 3	
                <<=	 x <<= 3	x = x << 3
                """)

                y = int(input("Enter value of x: "))
                x = y
                print("x = ", x)
                x += 3
                print("x+=3 : ", x)
                x -= 3
                print("x-=3 : ", x)
                x *= 3
                print("x*=3 : ", x)
                x /= 3
                print("x/=3 : ", x)
                x %= 3
                print("x%=3 : ", x)
                x //= 3
                print("x//=3 : ", x)
                x **= 3
                print("x**=3 : ", x)

            elif question == 3:
                # 3 # Comparison operators
                print("""
                ==	Equal	                        x == y	
                !=	Not equal	                x != y	
                >	Greater than            	x > y	
                <	Less than	                x < y	
                >=	Greater than or equal to	x >= y	
                <=	Less than or equal to	        x <= y	

                """)
                print("Examples of Comparison Operators")
                a = int(input("Enter a number: "))
                b = int(input("Enter another number: "))

                # a > b
                print("a > b : ", a > b)

                # a < b
                print("a < b : ", a < b)

                # a == b
                print("a == b : ", a == b)

                # a != b
                print("a != b : ", a != b)

                # a >= b
                print("a >= b : ", a >= b)

                # a <= b
                print("a <= b : ", a <= b)

            elif question == 4:
                # 4 # Logical operators

            else:
                print("Invalid Question Number, Try Again")
            choice = input(
                "\nDo you Want to Exit (Y for main menu),enter any key to continue : ")
            if choice == "y":
                break
