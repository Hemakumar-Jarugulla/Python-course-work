'''
class Instagram:
    def __init__(self):
        self._post=[]
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
    
hemanth = Instagram()

print(hemanth.accesspost)
hemanth.accesspost='class and object'
print(hemanth.accesspost)
    

class whatsappv1:
    def message(self):
        print("You can send  messages to people")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

hemanth=whatsappv1()
print("h1- Hemanth")
hemanth.message()

sekhar=whatsappv2()
print("h2- Sekhar")
sekhar.message()
sekhar.calls()


class whatsappv1:
    def message(self):
        print("You can send  messages to people")
        
class whatsappv2:
    def calls(self):
        print("You can do video/audio calls")
class whatsappv3:
    def media(self):
        print("You can share your photos/videos")
class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

hemanth=whatsappv4()
print("v4- Hemanth")
hemanth.message()
hemanth.calls()
hemanth.media()
hemanth.status()

class whatsappv1:
    def message(self):
        print("You can send  messages to people")
        
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")
class whatsappv3(whatsappv2):
    def media(self):
        print("You can share your photos/videos")
class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

hemanth=whatsappv4()
print("v4- Hemanth")
hemanth.message()
hemanth.calls()
hemanth.media()
hemanth.status()

hemanth=whatsappv3()
print("v3- Hemanth")
hemanth.message()
hemanth.calls()
hemanth.media()

hemanth=whatsappv2()
print("v2- Hemanth")
hemanth.message()
hemanth.calls()

hemanth=whatsappv1()
print("v1- Hemanth")
hemanth.message()

class whatsappv1:
    def message(self):
        print("You can send  messages to people")
        
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")

class whatsappv4():
    def gif(self):
        print("You can send messages with stickers to people")

hemanth=whatsappv3()
print("v3")
hemanth.stickers()
hemanth.message()

hemanth=whatsappv2()
print("v2")
hemanth.emojis()
hemanth.message()

class whatsappv1:
    def message(self):
        print("You can send  messages to people")
        
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")

class whatsappv4(whatsappv2,whatsappv3):
    def gif(self):
        print("You can send messages with gif to people")

hemanth=whatsappv4()
print("v4- Hemanth")
hemanth.gif()
hemanth.stickers()
hemanth.emojis()

hemanth=whatsappv3()
print("v3- Hemanth")
hemanth.stickers()
hemanth.message()

hemanth=whatsappv2()
print("v2- Hemanth")
hemanth.message()
hemanth.emojis()

hemanth=whatsappv1()
print("v1- Hemanth")
hemanth.message()

class wpv1():
    def status(self):
        print("You can upload images/videos")
class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")
class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")
hemanth=wpv3()
hemanth.status()
'''
class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2:
    def status(self):
        print("You can react and reply")
class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("You can like and reshare")
hemanth=wpv3()
hemanth.status()



