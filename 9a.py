#!/usr/bin/env python
# coding: utf-8

# In[22]:


class rectangle:
    def __init__(self):
        self.length=int(input("Enter length:"))
        self.breadth=int(input("Enter breadth:"))
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if(self.area()==other.area()):
            print("same area")
        else:
            print("not same area")
rect1=rectangle()
rect2=rectangle()
print("Area of rectangle 1:",rect1.area())
print("perimeter of rectangle 1",rect1.perimeter())
print("Area of rectangle 2:",rect2.area())
print("perimeter of rectangle 2",rect2.perimeter())
rect1.compare(rect2)
    


# In[20]:


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if(self.area()==other.area()):
            print("same area")
        else:
            print("not same area")
    rect1=rectangle(5,10)
    rect2=rectangle(2,11)
    
    print("Area of rectangle 1:",rect1.area())
    print("perimeter of rectangle 1",rect1.perimeter())
    print("Area of rectangle 2:",rect2.area())
    print("perimeter of rectangle 2",rect2.perimeter())
    rect1.compare(rect2)
    


# In[ ]:




