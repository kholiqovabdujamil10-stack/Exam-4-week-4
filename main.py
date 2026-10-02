# B1 
# mutable ин алишшаванда ва unmutable ин алишнашаванда мебошад 
# масалан tuple unmutable аст чунки алиш намешавад 
# вале лист mutable мубошад чунки даруни листро мо метавонем алиш кунем 

# масалан lict = [1,2,3,4]
# lict.append(4)
# мо метавонем иваз кунем вале то tuble ин хатто мешавад

# tuple = (1,2,3,4)
# tuple.append(4)
# хатто мебарорад


# B2
# try ин кодеро менависа ки метона хато дошта боша
# exept барои хатоо бошад ягон шарта ичро мекунад
# ва finally бошад барои дар охири барномаи мо ягон чизро баровардан аст ва вакте барномаи мо кор мекунад дар охираш чизе ки мо дар finally додаги астем мебарорад


# B3
# фарки tuple аз лист дар инхо мебошад:
# tuple(алишнашаванда, метонем ягон чизро добавит кунем е удалит кунем)
# list(алишшаванда, наметонем ягон чизро добавит кунем е удалит кунем)
# tuple барои навистани коде ки алиш набояд шавад даркор аст 


# B4
# int = 2(ракам)
# float = 2.4444(ракам бо бакия )
# str = "Abdullo"(текст)
# bool = True е False

# B5
# def fibonacci(n):
#     al = []
#     a = 1
#     b = 1
#     for i in range(n):
#         al.append(a)
#         a,b = b,a + b
#     return al
# print(fibonacci(10))


# B6
# numbers = [i for i in range(1, 51) if i%2==0 and i%3==0]
# print(numbers)

# B7
# with open("text.txt", "r") as file:
#     lines = file.readlines()
# print(len(lines))

# B8
# def word_count(text):
#     text = text.lower()
#     text = text.replace("!", "")
#     text = text.replace(",", "")
#     text = text.replace(".", "")
#     words = text.split()
#     result = {}
#     for i in words:
#         if i in result:
#             result[i] += 1
#         else:
#             result[i] = 1
#     return result
# a = word_count("Hello, hello! Python is great. Python is fun.")
# print(a)

# B9
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Недостаточно средств")
#     def __str__(self):
#         return f"Owner: {self.owner}, Balance: {self.balance}"
# account = BankAccount("Alice", 1000)
# account.deposit(500)
# account.withdraw(2000)
# print(account)


# B10
# from datetime import *
# def timing_decorator(func):
#     def inner(*args, **kwargs):
#         a = datetime.now()
#         func(*args, **kwargs)
#         b = datetime.now()
#         print(f"Function was working {b-a} seconds")
#     return inner
# @timing_decorator
# def calc():
#     total = 0
#     for i in range(1,1000000+1):
#         total+=i
#     print(f"The sum of numbers from 1 to 1000000 is : {total}")
# calc()

# B11
# def process_grades(filename):
#     with open("text.txt", "r") as file:
#         a = file.readlines()
