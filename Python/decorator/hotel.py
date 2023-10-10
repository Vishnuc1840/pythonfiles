class Hotel:
    items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"alfahm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},
    ]


    def create(self,*args,**kwargs):
        self.items.append(kwargs)
        return f"{kwargs} created"


    def retrieve(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
    
        return obj

    def destroy(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")][0]
        self.items.remove(obj)
        return f"{obj} has been removed"

    def update(self,id=None,*args,**kwargs):
        obj=self.retrieve(id=id)
        obj.update(kwargs)
        return f"{obj} has been updated"
obj=Hotel()
print(obj.create(id=106,name="noodles",price=180))
print(obj.retrieve(id=102))
print(obj.destroy(id=103))
print(obj.update(id=102,name="ghee roast",price=180))



def update(self,*args,**kwargs):
    obj=self.retrieve(id==id)
    obj,update(kwargs)
    return f"{obj} hasbeen updated"

print(obj.update(id=103,name="kuzhimandi"))
