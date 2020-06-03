#!/usr/bin/env python
# coding: utf-8

# In[13]:


def reverse(S):
    new_list = []
    for i in range(len(S)-1, -1, -1):
        new_list.append(S[i])
    s = "".join(new_list)
    return s
reverse("junyiacademy")


# In[12]:


def reverse_sentense(S):
    new_list = []
    flag = 0
    for i in range(len(S)):
        if S[i] == " ":
            s = reverse(S[flag:i+1])
            new_list.append(s)
            flag = i+1
        elif i == len(S)-1:
            s = reverse(S[flag:])
            new_list.append(" "+ s)
        else:
            continue
    a = "".join(new_list)
    return a
reverse_sentense('flipped class room is important')


# In[15]:


def count_num(num):
    list = []
    for i in range(1, num+1):
        if i % 15 == 0:
            list.append(i)
        else:
            if i % 3 == 0 or i % 5 == 0:
                continue
            else:
                list.append(i)
    return len(list)
count_num(15)



