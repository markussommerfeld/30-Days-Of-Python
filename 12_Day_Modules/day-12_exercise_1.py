# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:07:50 2024

@author: marku
"""

"""

Writ a function which generates a six digit/character random_user_id.

  print(random_user_id());
  '1ee33d'

    Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

    Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""
#1 done
def random_user_id():
    import string
    import random
    N = 6

    # using random.choices()
    # generating random strings
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=N))

    # print result
    #print("The generated random string : " + str(res))
  
    
    return(res)
#2 done
def user_id_gen_by_user():
    
    import string
    import random
    n_char, n_ID = input('Input number of characters and number if IDs: ').split()

    # using random.choices()
    # generating random strings
    for i in range(int(n_ID)):
        res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=int(n_char)))
        print(res)
#3 done
def rgb_color_gen():
    import random
    
    rgb_out = [random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255)]
    return(rgb_out)

    