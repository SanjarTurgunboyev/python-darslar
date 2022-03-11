# 15-DARS. LUG'AT ELEMENTLARI BILAN ISHLASH:
# sana: 27/02/2022
# mualif: Sanjar


# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shashmshiyev',
#     'yosh':'22',
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())


# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


# telefonlar = {
#     'ali':'iohone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")


# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# print(mahsulotlar.keys())

# # print('Do\'kondagi mahsulotlar:')
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())

# # print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())


# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do`koningizga {buyum} ham olib keling")

# print("Do`konimizdagi mahsulotlotalar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print('Foydalanuvchilar quyidagi telefonlarni ishlatadi:')
# for tel in telefonlar.values():
#     print(tel)


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'asil':'realme 6i',
#     'aziz':'iphone x',
#     'shavkat':'realme 6i',
#     'sanjar':'mi 10 pro'
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatadilar:')
# for tel in telefonlar.values():
#     print(tel)


# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)


# toys = {'ball','car','lamp','ball','bear','car'}

# python_words = {
#     'float':'O`nlik son',
#     'string':'matn',
#     'integer':'Butun son',
#     'boolean':'Mantiqiy qiymat',
#     'for':'Biror qiymatni qayta-qayta bajarish tsikli',
#     'in':'sharlarni tekshirish operatori'
#     }

# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print("Dunyo davlatlar:")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())


# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz bizda bu haqida ma\'lumot y/`oq')
# else:
#     print(F"{country.upper()}ning poytaxti {capital.title()} shahri")
        

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }


# print('3 ta taom byurtma bering.')
# byurtmalar = []
# for n in range(3):
#     byurtmalar.append(input(f"{n+1}-taom:").lower())
    
# for byurtma in byurtmalar:
#     if byurtma in menu:
#         print(F"{byurtma.title()} {menu[byurtma]} so`m")
#     else:
#         print(F"Kechirasiz, bizda {byurtma} yo`q.")
        













