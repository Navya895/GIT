# salary = 2e3
# print(salary)
# x = complex(5,2)
# print(x)
# #sequence
# #2. string
# print("Hello")
# print("""SVKM
#       NMIMS
#       Shirpur""")
# #3. list:  ordered collection of element, mutable

# lst = [2,3,4,5]
# print(lst)
# li = [2,4, "Hello", True, 10.5, "Hello"]
# print(li)
# print(li[0])
# print(li[0:4])
# #2. tuple: ordered collection of element; allow duplicate value; support indexing and slicing; tuple immutable
# t = (1, 2, 3, "Python")
# print(t)
# print(t[-1])
# print(t[3])
# print(t[0:3])
# # 3. range: represent sequence of number
# ran = range(5)
# print(ran)
# print(list(ran))
# r = range(1,11,2)
# print(list(r))
# rang = range(10,0,-1)
# print(list(rang))
# for i in range(0,6):
#     print(i, end= " ")
# #range function with length
# fruits = ["apple", "banana", "pears"]
# for i in range(len(fruits)):
#     print(i, fruits[i])
# fs={1,2,3}
# fs.add(4)
# print(fs)
# vowel = {'a','e','i','o','u'}
# f = frozenset(vowel)
# print(f)
# #mapping : dict
# d = {
#     "name": "john",
#     "age": 20
# }
# print(d)
# #boolean  
# x= True
# y= False
# print(10>5)
# print(20<10)
# #binary
# #bytes: immutable
# b =b"Hello"
# print(b)
# x = 10
# bin_no = bin(x)
# print(bin_no)
# print(5&3)
# #WAP t orpint even number between 1 to 20 
# for i in range (2, 21, 2):
#     print(i)

# #WAP to print sum of 1 to 10 even number
# sum = 0
# for i in range (2, 11, 2):
#     sum+=i
# print(sum)
# #WAP to print the sum of numbers between n1 and n2
# n1 = int(input("Enter the starting number: "))
# n2 = int(input("Enter the ending number: "))
# sum = 0
# for i in range(n1, n2):
#     sum+= i
# print(sum)

# #A to Z
# for i in range(65, 91):
#     print(chr(i), end=" ")

# # WAP to ask user if they want to print capital or small alphabet
# choice = input("\nEnter 's' for small alphabet and 'c' for capital alphabet: ")
# if choice == 's':
#     for i in range(97, 122):
#         print(chr(i), end= " ")
# elif choice == 'c':
#     for i in range(65, 91):
#         print(chr(i), end=" ")
# else:
#     print("invalid choice1")
# #WAP to print  factorial of a number
# def cal_fac_rec(num):
#     if num < 0:
#         return "factorial can't be calculated for negative character"
#     elif num == 0 or num == 1:
#         return 1
#     else:
#         return num * cal_fac_rec(num-1)

# num = int(input("Enter the  number"))
# print(f"the factorial of {num} is {cal_fac_rec}")
# #match
# while True:
#     print("\nMenu")
#     print("\n1. Even Odd")
#     print("\n2. Factorial")
#     print("\n3. EXIT")
#     ch = int(input("\nEnter your choice: "))
#     match ch:
#         case 1:
#             num = int(input("\nEnter a even or odd number: "))
#             if num%2 == 0:
#                 print("\nEVEN NUMBER")
#             else:
#                 print("\nODD NUMBER")
#         case 2:
#             num = ("\nEnter the number you want the factorial of: ")
#             if num < 0:
#                 print("\nThe factorial of negative number doesn't exists")
#             elif num == 0 or num == 1:
#                 print(" the factorial is 1")
#             else:
#                 mul = 1
#                 for i in range(1,num):
#                     mul*= num
#                 print(f"the factorial of {num} is {mul}")
#         case 3:
#             print("EXITING PROGRAM")
#             break

#STRING
# x = "hello HI my name is Navya"
# print(x.count("a"))

#walrus operator(:=)
# print(x=10) #error
# print(x := 10)

# x = [5, 10, 15, 20, 25, 30]
# i = -1
# while((i: =i+1)< (n:= len(x))):
#     print(x[i], end=" ")
# if((name := input("Enter Name"))=="Admin"):
#     print("Welcome")
# if(c:=len("Banana")):
#     print(c)
# if(marks:= 75)>=35:
#     print("Pass")
# print(a) if((a:=10)<(b:=20)) else print(b)  #important 


#more about integers
#convert integer to string
# num=100
# str_num = str(num)
# print(str_num)
# print(type(str_num))
# bin_num = bin(num)
# print(bin_num)
# b = "1010"
# int_num = int(b,2)
# print(int_num)
# % is npt used for srithematic operator
# a = 5.5
# b= 2.5
# print(a+b)
# x = 3.141516
# print(x,2)
# l=[1,2,34,5,6,7]
# print(l)
# fruits=["Apple","Banana","cherry"]
# fruits.append("Mango")
#extend()merge 2 list
#pop delte element from a particulsr index
# clear() make the list empty
# nested=[["Hello", 1, 2, 3],[4,5,6]]
# nested[0].remove["Hello"]
#sort
# num = [1, 2, 3, 6, 8, 9, 20, 15, 45, 36]
# num.sort()
# num.sort(reverse= True)
# li = []
# for i in range(1,6):
#     li.append(i*i)
# print(li)
# squares = [i*i for i in range(1,6)]
# print(squares)
# sentence = "python is very very easy"
# first_letter = [for i in s]
# find maximum and minmum in list
# x = [10, 20, 30, 40, 50]
# print(max(x))
# print(min(x))

# y = ['Raj', 'Vishal', 'A']
# print(max(y))
# print(min(y))

# x = ['Hllo', 'ab']
# print(max(x, default= "No element"))
# print(max(x, key=len, default = "No element"))
# x = [43, 88, 56, 32, 90]
# max = x[0]
# for i in x:
#     if(i>max):
#         max=i
# print(max)

# # a=[]
# # for i in range(5):
# #     num = int(input("Enter the number you wsnt to append: "))
# #     a.append(num)
# # print(a)
# x.insert(1, 38)
# print(x)
# a = {1,2,3}
# b = {1, 2, 3}
# print(id(a))
# print(id(b))
# c = (1,2,3)
# d = (1, 2, 3)
# print(id(c))
# print(id(d))
# a = [10,20,30]
# b = [10,20,30]
# c= a
# d = b.copy()
# print(a==b)
# a = ['hello', 'student']
# b = ' '.join(a)
# print(b)
# lst = [1,2,2,3]
# print(set(lst))
# def add(a,b):
#     print(a+b)
# # a = int(input("Enter A: "))
# # b = int(input("Enter B: "))
# # add(a,b)
# add(int(input()),int(input()))
# def add(a,b, c= None):
#     if c==None:
#         print("Sum of 2 num: ", a+b)
#     else:
#         print("Sum of 3 num: ", a+b+c)
# add(2,3)
# def add(*a):
#     print(a)
# add(10, 20, 30, 40)
# def add(x,y,*a):
#     print(x)
#     print(y)
#     print(a)
# add(10, 20, 30, 40)
# def add(**a):
#     print(a)
# add(x=5, y=10)
# def fun(x,/,y):
#     print(x,y)
# fun(10, y=20)
# def fun(x):
#     print(x)
# def fun2():
#     print(a)
# a= 30
# fun(a)
# fun2()
# def a():
#     laptop=50
#     b(laptop)
# def b(laptop):
#     print(laptop)
# a()
# def outer():
#     print("This is an outer function: ")
#     def inner():
#         print("This is an inner function: ")
#     inner()
# outer()
# def msg():
#     def x100linecode():
#         print("100 line of codes")
#     print("Some codes")  
#     x100linecode()
# msg()
# def add(a:int, b:int) ->int:
#     print(a+b)
# add(5,10.5)
# print(add.__annotations__)

# lambda: anonymous function
# square = lambda x: x*x
# print(square(5))
#write a lambda fumction to add 10 to a number
# print((lambda x: x+10)(5))
# #write a lambda func to reutrn maximum of 2 number
# print((lambda x,y: max(x,y))(5,10))
# #write a lambda function to check if a number is even
# print((lambda x: x%2==0)(10))
# print((lambda x:x.upper())("name"))
# x = lambda no: [i*i for i in range(1, no+1)]
# print(x(5))
# add = lambda: int(input("Enter A:")) + int(input("Enter B:"))
# print(add())

#strin len
print((lambda x: len(x))("Name"))
#reverse string
print((lambda x: x[::-1])("NAVYA"))
#palindrome string
print((lambda x: x==x[::-1])("coc"))
#first character of string
print((lambda x: x[0])("NAVYA"))
#concatenate string
print((lambda x,y: x + y)('Hello ', 'Student'))
#replace space with hypen
print((lambda x: x.replace(' ', '-'))("Heloo student i am good"))
print((lambda x: "Empty" if len(x)==0 else "not empty "))
print((lambda x: x[-1])('20457'))
print((lambda x: x[-1].isdigit())('hii9'))