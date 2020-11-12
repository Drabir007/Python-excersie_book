#!/usr/bin/env python
# coding: utf-8

# In[15]:


# 1
def function1(n, m):
    if n % m == 0:
        return (True)
    else:
        return (False)


print(function1(10, 2))
print(function1(10, 3))


# In[16]:


# 3


def minmax(data):
    if len(data):
        min = data[0]
        max = data[0]
    for i in data:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max


print(minmax([1, 2, 3, 4]))


# In[17]:


# 4

def function(n):
    total = 0
    for i in range(1, n):
        total = total + (i * i)
    return total


print(function(3))
print(function(5))


# In[19]:


# 5

def function2(n):
    return sum(i * i for i in range(1, n))


print(function2(4))


# In[64]:


# 6

def sumsquer(n):
    total = 0

    for i in range(1, n + 1, 2):
        total += (i * i)
    return total


print(sumsquer(4))


# In[70]:


# 6
def sumoddsquares(k):
    return sum(x * x for x in range(1, k) if x % 2 == 1)


print(sumoddsquares(4))


# In[72]:


# 7

def function6(n):
    return sum(i * i for i in range(1, n + 1, 2))


print(function6(4))

# In[74]:


# 9
print(list(range(50, 90, 10)))

# In[75]:


# 10

print(list(range(8, -10, -2)))

# In[76]:


# 11
print([2 ** i for i in range(9)])


# In[ ]:


# 12


# In[1]:
# At a lemonade stand, each lemonade costs $5.
#
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
#
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
#
# Note that you don't have any change in hand at first.
#
# Return true if and only if you can provide every customer with correct change.

def functions(change):
    five = ten = 0
    for x in change:
        if x == 5:
            five += 1
        elif x == 10 and five:
            ten += 1
            five -= 1
        elif x == 20 and five and ten:
            five -= 1
            ten -= 1
        elif x == 20 and five >= 3:
            five -= 3
        else:
            return False
    return True


# In[ ]:
# leetcode problem 169. Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


def majority(num):
    x = len(num) // 2
    for i in num:
        count = sum(1 for i in num if i == num)
        if count > x:
            return num


