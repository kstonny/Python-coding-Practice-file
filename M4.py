class book:

    def __init__(self,au,pub,p,r):
        self.author=au
        self.publisher=pub
        self.price=p
        self.royality=r


    def getauthor(self):
        return self.author
    def getpublisher(self):
        return self.publisher
    def getprice(self):
        return self.price
    def getroyality(self):
        return self.royality

    def setprice(self,p):
        self.price=p

    def setpublisher(self,pub):
        self.publisher=pub
    def setauthor(self,au):
        self.author= au
    def setroyality(self,r):
        self.royality=r

    def authorroyality(self,copies):
        if copies>0 and copies<501:
            self.royality=copies*self.price*10/100
        if copies>500 and copies<1001:
            self.royality=500*self.price*10/100+(copies-500)*self.price*125/1000
        if copies>1000:
            self.royality=(500*self.price*10/100)+(500*self.price*125/1000)+(copies-1000)*self.price*15/100
        return self.royality

a=book("karan","telisko",1000,0)
a.authorroyality(1100)


print("Author's Name",a.getauthor(),"Book Price",a.getprice(),"Publisher",a.getpublisher())
print("Author royality",a.getroyality())



class ebook(book):
    def __init__(self,e_format,au,pub,p,r):
        super().__init__(au,pub,p,r)
        self.e_format=e_format

    def authorroyality(self,copies):
        royl = super().authorroyality(copies)
        self.royality=royl-royl*12/100
        return self.royality

b=ebook("PDF","karan","telisko",1000,0)
b.authorroyality(1100)

print("Ebook Royality",b.getroyality())

