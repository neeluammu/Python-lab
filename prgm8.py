#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


sqarea=lambda a:a*a
a=int(input("Enter side of square:"))
print("Area of square :",sqarea(a))

rectarea=lambda l,b:l*b
l=int(input("Enter length of rectangle"))
b=int(input("Enter breadth of rectangle"))
print("Area of rectangle :",rectarea(l,b))

triarea=lambda base,h:(1/2)*base*h
base=int(input("Enter base of triangle:"))
h=int(input("Enter breadth of triangle:"))
print("Area of triangle :",triarea(base,h))
      


# In[ ]:




