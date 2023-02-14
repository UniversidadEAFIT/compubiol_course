#!/usr/bin/env python
# coding: utf-8

# # Taller 1

# 2
# ![image.png](attachment:image.png)
# 

# 3
# ![image.png](attachment:image.png)

# In[5]:


#String
def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  return str[2:]+str[:2]

#List
def middle_way(a, b):
  c=[a[1],b[1]]
  return c

def has23(nums):
  if nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3:
    return True
  else:
    return False


# 4
# ![image.png](attachment:image.png)
# ![image.png](attachment:image.png)
# ![image.png](attachment:image.png)

# In[4]:


#5
#Warmup-1
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

#Logic-1
def cigar_party(cigars, is_weekend):
  if 40<=cigars<=60 and not is_weekend:
    return True
  else:
    if 40<=cigars and is_weekend:
      return True
    else:
      return False

