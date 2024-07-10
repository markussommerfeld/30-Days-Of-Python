# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:07:50 2024

@author: marku
"""

"""

    Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
    Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
    Write a function generate_colors which can generate any number of hexa or rgb colors.

   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   
 """

#1 done
def list_of_hexa_colors(n_hex):
    import string
    import random
    N = 6
    hex_out = []
    # using random.choices()
    # generating random strings
    # srt_rand_a_f = string.ascii_lowercase[random.randrange(1, 7)]
    for idx in range(n_hex):
        hex_out.append('#' + ''.join(random.choices(string.ascii_lowercase[:6] +
                                     string.digits, k=N)))
    return(hex_out)
#2 done
def list_of_rgb_colors(n_rgb):
    import random
    rgb_out = []
    for idx in range(n_rgb):

        rgb_out.append([random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255)])
    return(rgb_out)

#3 done
def generate_colors (color_type = 'rgb',n_color = 1):
    
    if color_type.lower() == 'rgb':
        color_list = list_of_rgb_colors(n_color)
    elif color_type.lower() == 'hex':
        color_list = list_of_hexa_colors(n_color)
    else:
        print('input wrong!')
        color_list = []
    return(color_list)
    
    