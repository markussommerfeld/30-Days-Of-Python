# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:31:28 2024

@author: marku
"""

"""
given list of emails and URL. Return a dicttionary where keys is a URL and the value is how many emails have the same domain.
Ignore non existing URL
"""

#count_email_domains(
#    emails = ['foo@a.com','bar@a.com','bla@c.com','test@d.com']),
#    urls = ['www.a.com','www.b.com','www.c.com']

### PLAN ###
# 1. get domain of emails
# 2. get domain of urls
# 3. count number of emails
# 4. output dictionary


#%%
"""
Given a string of moores code that contains a list of '.' and '-'.
You are allowed to make one move and replace '..' with '--'.
Return all possible mores code you can get after a single move. 
If you cannot do any move return an empty array.

Example:
Input = '....'
Output = ['--..','.--.','..--']
"""

# def morse_code(str_in):
    
#     return(list_out)