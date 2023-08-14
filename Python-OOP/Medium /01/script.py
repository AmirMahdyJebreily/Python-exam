class veichel: # به معنی وسیله نقلیه

    def __init__(self, speed, model):
        self.speed = speed
        self.model = model
        pass

    # یک متن برای وقتی که کلاس را به رشته تبدیل می کنیم در نظر بگیرید که در آن خصوصیات وسیله نقلیه را نوشته باشد
    # str = رشته

    def move():
        pass # وسله نقلیه باید حرکت کنه !

class car(veichel): # ماشین
    
    def move():
        pass # ماشین هم حرکت میکنه! اما نه مثل بقیه وسیله های نقلیه
        # drive = رانندگی کردن

class boat(veichel): # قایق
     
    def move():
        pass # قایق هم حرکت میکنه! اما نه مثل بقیه وسیله های نقلیه
        # sail = روی دریا شنا کردن

class plain(veichel): # هواپیما
     
    def move():
        pass # هواپیما هم حرکت میکنه! اما نه مثل بقیه وسیله های نقلیه
        # fly = پرواز کردن


peykan = car(120, "Javanan")
tourist_boat = boat(345, "C120")
boeing = plain(1200, "715")


# همه وسایل نقلیه باید حرکت کنند