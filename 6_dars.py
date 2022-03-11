# 10-dars IF ELSE SHARTLARI VA TARMOQLANISH
# sana: 25/02/2022
# mualif: Sanjar

# avtolar = ['audi','bmw','volvo','kia','hyundai']

# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

 
# ism = 'Ali'

# ism.lower() == 'ali'

# ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")

# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz!')
# else: # ask holda
#     print('Kirish mumkin emas!')


# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")


# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2022-yil<18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2022-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")


# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 50, 40 # x=25 va y=50
# print("x>y") if x>y else print("x<y")

# AMALIYOT

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())


# #Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car!='gm':
#     print(car.title())
#   else:
#     print(car.upper()) 

# login = input("Xush kelibsiz!")
# if login.lower() == 'admin':
#     print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {login.lower()}!")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y: print(f"Sonlar teng: {x}={y}")

# son = float(input("Istalgan son kiriting:"))
# print("Son manfiy") if son<0 else print("Son musbat")

# son = float(input("Istalgan son kiriting: "))
# print(son**(1/2) if son>0 else ("Musbat son kiriting"))




