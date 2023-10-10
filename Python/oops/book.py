class Book:
    book_name:str
    author:str
    price:int
    pages:int

    def __init__(self,book_name,author,price,pages):
        self.book_name=book_name
        self.author=author
        self.price=price
        self.pages=pages
        # initializing instance variable

    def get(self):
        print(self.book_name,self.author)

    # def __str__
        return self.book_name+str(seld,price)

obj=Book("aadujeevitham","baneyamen",580,691)

print()

# obj2=Book("aarachar","meera",200,250),
# print(obj.book_name)


