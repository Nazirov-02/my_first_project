import json
import os
from menegers import read,write
def add_elon():
    mahsulot = input("mahsulotingiz nomini kiriting: ")
    narxi = input("mahsulot narxi kiriting: ")
    miqdori = input("mahsulot miqdori kiriting: ")
    name = input("elon beruvchining ismini kiriting: ")
    number = input("Bog'lanish uchun e'lon beruvchining no'merini kiriting: ")
    id = input("mahsulot IDsini kiriting: ")
    if os.path.exists("products.json"):
       data = read(file="products.json")
       for i in data.keys():
           if i == id:
               print("bunday id li mahsulot alloqachon mavjud !")
               return add_elon()
    else:data = dict()



    data[id] = {"nomi":mahsulot,
                     "narxi":narxi,
                     "miqdori":miqdori,
                     "admin":name,
                     "number":number,
                     "ID":id}
    write(file = "products.json",data = data)
    print("mahsulot muvaffaqiyatli saqlandi !")
    return main()


def read_p():
    k = 1
    if os.path.exists("products.json"):
      data = read("products.json")
      for i in data.values():
        print("""NO ID  Nomi    Narxi    Miqdori      admin       raqami""")
        print(f"{k})\t{i["ID"]}\t{i["nomi"]}\t{i["narxi"]} so'm\t{i["miqdori"]}\t\t{i['admin']}\t{i['number']}")
        k += 1
      return main()
    print("mahsulotlar hozircha mavjud emas !")
    return main()
def delet():
    k = 1
    data = read("products.json")
    for i in data.values():
        print("""NO ID  Nomi    Narxi    Miqdori      admin       raqami""")
        print(f"{k})\t{i["ID"]}\t{i["nomi"]}\t{i["narxi"]} so'm\t{i["miqdori"]}\t\t{i['admin']}\t{i['number']}")
        k += 1
    p = input("Olib tashlamoqchi bo'lgan mahsulotingizni ID raqamini kiriting: ")
    if p in data.keys():
            data.pop(p)
            write(file="products.json", data=data)
            print("Muvaffaqiyatli bajarildi")
            return main()
    print("bunday id li mahsulot mavjud emas !")
    return main()

def delete_all(file):
    os.remove(file)
    print("muvofaqqiyatli amalga oshirildi !")
    return main()


def main():
    n = input("""Ximatlar
    1. Hamma elonlarni ko'rish
    2. Yangi e'lon berish
    3. E'lonni o'chirib tashlash
    4. Hamma elonlarni o'chirib tashlash
    5. exit
    >>>>: """)
    if n == "1":
        return read_p()
    elif n == "2":
        add_elon()
    elif n == "3":
       return delet()
    elif n == "4":
        delete_all(file = "products.json")
    elif n == "5":
        print("Ilovadan foydalanganingiz uchun rahmat !\a ")

if __name__ == "__main__":
    main()