# اسکریپت شماره ۰۱ - وسیله ها حرکت میکنن ! (متوسط) (۰.۷۵ نمره)
خب ما اینجا یهسری وسیله نقلیه داریم (ٰveichel) که هر کدوم ویژگی های سرعت و مدل رو دارن و حرکت می کنند. دقت کنید که قایق شنا می کنه هواپیما پرواز میکنه و ماشین رانندگی میکنه !
راهنمایی های شما هم این \پایینه

## راهنمای اول - یادآوری ارثبری و چندریختی ها
وقتی شما یک کلاس دارید، کلاس های دیگه هم میتونن از این کلاس شما ارثبری کنند. یعنی چی ؟    
یعنی یک کلاس (یک شئ یا یک چیز در پایتون) میتونه خصوصیات، رفتار ها و قابلیت های یک کلاس دیگه رو داشته باشه، بدون اینکه براش تعریف کنیم !

مثل اینجا

```py
class Pen:
    بقیه کد ها
```
اینجا ما یک کلاس خودکار داریم. معمولا توی این کلاس ها میایم و مفهوم خودکار رو توصیف می کنیم
اینجوری : 

```py
class Pen:
    خودکار رنگ داره
    شکل داره
    مارک و مدل داره
    کارای مختلف میتونه انجام بده
```
یا به شکل واقعا پایتونیش اینجوری :   

```py
class Pen:
    color = "Blue"
    body_shape = "capsule"
    brand = "کیان"
    def write(self,something):
        print(something, "with", self.color, "color")
        # خروجی: [...something...] with Blue color
```

یا :   

```py
class Pen:
    def __init__(self):
        self.color = "Blue"
        self.body_shape = "capsule"
        self.brand = "کیان"

    def write(self,something):
        print(something, "with", self.color, "color")
        # خروجی: [...something...] with Blue color
```

حالا اگر بخوایم میتونیم یک خودکار جدید بسازیم بدون اینکه چیزی از این کد ها اونجا کپی کنیم :

```py
class Kian(Pen)
```

الان `Kian` برای کامپیوتر به عنوان فرزند کلاس `Pen` شناخته میشه. مثل شما که فزند پدرتون هستید و خصوصیاتشو به ارث بردید، کلاس `Kian` هم خصوصیات والدشو به ارث می بره. در نتیجه الان این کلاس جدید خصوصیات همون `Pen` رو داره! پس ما میتونیم اینجا خیلی راحت بگیم : 
   
```py
pen1 = Kian()
print(pen1.color)
```
این به ما خروجی مقدار `Blue` رو میده چون خاصیت `Pen` این بود که رنگش Blue باشه

## راهنمای دوم - سایت های خارجی
همانطور که گفته بودم! من اینجا دیگر چیزی را به شما تدریس نمی کنم! میتوانید از این لینک ها استفاده کنید تا مباحث را متوجه شوید!

- [Inheritance in Python - GeeksforGeeks](https://www.geeksforgeeks.org/inheritance-in-python/)  
- [Python Inheritance - W3Schools.com](https://www.w3schools.com/python/python_inheritance.asp)