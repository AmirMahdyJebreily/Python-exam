import re

emailValidationPattern = r"\w+@\w+(\.\w+)*"

class User: 

    # کنید Encapsulate ایمیل و رمز عبور را
    # اصول SOLID رو هم رعایت کنید

    def __init__(self,id , name, password, email):

        self.id = id,
        self.name = name

        # لاگین بودن یا نبودن کاربر رو مشخص کن ! (این مورد امتیازی است)

        self.__password = password # سعی کنید یادتون بیاد چرا اسم این خصوصیت رو اینجوری تعریف کردم

        # جای خالی برای ایمیل
    
    def Login(self,username, password): # توضیح بدین چرا یکی از این دوتا اضافست (این مورد امتیازی می باشد)

        # اگر رمز عبور درست بود روی صفحه چاپ کنه که کاربر لاگین کرده

        pass

    def __str__(self):
        return "یه چیزی که بعدا به کار میاد ..."


# یک مجموعه از کاربران


username = input("Enter your username here :")        
password = input("Enter your password here :")

# دونه دونه چک کنه ببینه نام کاربری کدوم آیتم لیست با نام کاربری وارد شده برابره ؟
# همونو لاگین کنه 