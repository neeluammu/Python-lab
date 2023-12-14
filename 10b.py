#!/usr/bin/env python
# coding: utf-8

# In[4]:


f1=open("file.txt","r")
f2=open("copy.txt","w")
content=f1.readlines()
for i in range(0,len(content)):
    if(i%2!=0):
        f2.write(content[i])
    else:
        pass
f2.close()
f2=open("copy.txt","r")
content1=f2.read()
print(content1)
f1.close()
f2.close()


# In[ ]:




