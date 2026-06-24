'''
class Flipcart:
    discount=10
    products=['laptop','phone','mouse','charger']

    @classmethod
    def showProducts(cls):
        print(cls.products)
        
    def login(self,username,password):
        self.username=username
        self.password=password
        print(f'welcome to the flipkart {self.username}')
    @staticmethod
    def banner():
        print("10% discount is going on flipkart,shop now!")
hemanth = Flipcart()
hemanth.login('hemanth','hemanth@123')
hemanth.banner()
hemanth.showProducts()

Flipcart.showProducts()
Flipcart.banner()
# constructor
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.followers=[]
        print(f'welcome to the Instagram,{self.username}')
        
hemanth=Instagram('hemanth','hemanth@123')
'''

class Instagram:
    def __init__(self,username,password):
        self.username=username
        self._password=password
        self._followers=[]
        
    def getpassword(self):
        return self._password
    
    def setpassword(self,newpassword):
        self._password = newpassword

       
hemanth=Instagram('hemanth','hemanth@123')

print("Before username:",hemanth.username)
hemanth.username = 'sekhar'
print("After username:",hemanth.username)

print("Before password:",hemanth.getpassword())
hemanth.setpassword('Sekhar@123')
print("After password:",hemanth.getpassword())





