# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:07:50 2024

@author: marku
"""

"""

    Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
    Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


"""

#1 done
def shuffle_list(list_in):
    import random
    list_out = list_in.copy()
    random.shuffle(list_out)
    return(list_out)

#2 done
def shuffle_list(list_in):
    import random
    return(random.sample(range(0,9), 7))
    